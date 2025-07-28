import os
import time
import pandas as pd
from datasets import Dataset
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Seq2SeqTrainingArguments,
    DataCollatorForSeq2Seq,
    Trainer, 
    TrainingArguments
)

# === CONFIGURACIÓN ===
TRANSFORMERS_CACHE = os.path.abspath("./models")
os.environ["TRANSFORMERS_CACHE"] = TRANSFORMERS_CACHE
os.makedirs(TRANSFORMERS_CACHE, exist_ok=True)

CSV_PATH = "data/productos_train.csv"
MODEL_NAME = "google-t5/t5-small"
OUTPUT_DIR = os.path.join("models", "ontotransformer-retrained")
VALID_CATEGORIES_PATH = "data/categorias_validas.csv"

print("📄 Cargando CSV...")
df = pd.read_csv(CSV_PATH)
df = df.dropna().reset_index(drop=True)
df["input"] = "clasifica: " + df["input"]

print(f"✅ Dataset cargado con {len(df)} ejemplos")

# === VALIDACIÓN CONTRA CATEGORÍAS VÁLIDAS ===
print("🔎 Validando categorías de salida...")
valid_cats = pd.read_csv(VALID_CATEGORIES_PATH)["categoria"].tolist()
df_invalid = df[~df["output"].isin(valid_cats)]

if not df_invalid.empty:
    categorias_no_validas = sorted(set(df_invalid["output"]))
    print("❌ Categorías no válidas encontradas en el dataset:")
    for cat in categorias_no_validas:
        print("  -", cat)
    df_invalid.to_csv("data/categorias_invalidas_detectadas.csv", index=False)
    raise ValueError("❌ Detén el entrenamiento: revisa 'categorias_invalidas_detectadas.csv'.")
else:
    print("✅ Todas las categorías son válidas.")

print("📦 Cargando tokenizer y modelo base...")
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME, cache_dir=TRANSFORMERS_CACHE)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME, cache_dir=TRANSFORMERS_CACHE)

# Conversión a Dataset de HuggingFace
dataset = Dataset.from_pandas(df)

max_input_length = 80
max_target_length = 64

def preprocess_function(examples):
    inputs = tokenizer(examples["input"], max_length=max_input_length, truncation=True, padding="max_length")
    targets = tokenizer(examples["output"], max_length=max_target_length, truncation=True, padding="max_length")
    labels = [
        [token if token != tokenizer.pad_token_id else -100 for token in target]
        for target in targets["input_ids"]
    ]
    inputs["labels"] = labels
    return inputs

print("🔄 Preprocesando dataset...")
tokenized_dataset = dataset.map(preprocess_function, batched=True, load_from_cache_file=False)

training_args = Seq2SeqTrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    num_train_epochs=30,
    learning_rate=5e-4,
    logging_dir="logs",
    logging_strategy="steps",
    logging_steps=1,
    save_strategy="no",
    predict_with_generate=True,
    report_to="none"
)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# === ENTRENADOR ===
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

print("\n🚀 Iniciando entrenamiento supervisado...")
trainer.train()

print("💾 Guardando modelo...")
os.makedirs(OUTPUT_DIR, exist_ok=True)
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"✅ Modelo guardado en: {OUTPUT_DIR}")
