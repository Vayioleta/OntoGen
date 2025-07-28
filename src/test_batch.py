import os
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_DIR = os.path.abspath("models/ontotransformer-retrained")
CSV_PATH = "data/productos_train.csv"

print("\U0001F4E5 Cargando modelo y tokenizer...")
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
model.eval()

print("\U0001F4C4 Cargando CSV...")
df = pd.read_csv(CSV_PATH).dropna().reset_index(drop=True)

def inferir(texto_input):
    entrada = "clasifica: " + texto_input.strip()
    input_ids = tokenizer(entrada, return_tensors="pt", padding=True, truncation=True).input_ids
    outputs = model.generate(input_ids=input_ids, max_length=64, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Evaluar primeros 5 ejemplos
print("\n\U0001F50D Evaluando ejemplos reales:\n")
for i in range(min(5, len(df))):
    entrada_cruda = df.loc[i, "input"].replace("clasifica: ", "")
    salida_esperada = df.loc[i, "output"]
    salida_generada = inferir(entrada_cruda)

    print(f"\U0001F4DD Entrada: {entrada_cruda}")
    print(f"✅ Esperado: {salida_esperada}")
    print(f"\U0001F52E Generado: {salida_generada}")
    print("—" * 50)
