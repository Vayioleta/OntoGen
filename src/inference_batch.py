import os
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration
from difflib import get_close_matches

# === CONFIGURACIÓN ===
MODEL_DIR = os.path.abspath("models/ontotransformer-retrained")
CSV_INPUT_PATH = "data/productos_reales.csv"              # Entrada real
CSV_CATEGORIAS_VALIDAS = "data/categorias_validas.csv"   # Lista de categorías válidas
CSV_SALIDA_CONOCIDOS = "out/clasificados_conocidos.csv"
CSV_SALIDA_DESCONOCIDOS = "out/clasificados_desconocidos.csv"

# === CARGA ===
print("📦 Cargando modelo y tokenizer...")
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
model.eval()

print("📄 Cargando productos reales y categorías válidas...")
df = pd.read_csv(CSV_INPUT_PATH).dropna().reset_index(drop=True)
categorias_validas = pd.read_csv(CSV_CATEGORIAS_VALIDAS)["categoria"].tolist()

# === INFERENCIA Y VALIDACIÓN ===
def inferir(texto_input):
    entrada = "clasifica: " + texto_input.strip()
    input_ids = tokenizer(entrada, return_tensors="pt", padding=True, truncation=True).input_ids
    outputs = model.generate(input_ids=input_ids, max_length=64, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def validar_categoria(predicha):
    match = get_close_matches(predicha, categorias_validas, n=1, cutoff=0.85)
    return match[0] if match else None

conocidos = []
desconocidos = []

print("🔍 Clasificando productos...")
for _, row in df.iterrows():
    texto = row["input"]
    predicha = inferir(texto)
    categoria_valida = validar_categoria(predicha)

    if categoria_valida:
        conocidos.append({"input": texto, "predicha": predicha, "categoria_final": categoria_valida})
    else:
        desconocidos.append({"input": texto, "predicha": predicha})

# === GUARDAR RESULTADOS ===
os.makedirs("out", exist_ok=True)
pd.DataFrame(conocidos).to_csv(CSV_SALIDA_CONOCIDOS, index=False)
pd.DataFrame(desconocidos).to_csv(CSV_SALIDA_DESCONOCIDOS, index=False)

print(f"✅ Clasificados conocidos: {len(conocidos)} → {CSV_SALIDA_CONOCIDOS}")
print(f"⚠️ Desconocidos: {len(desconocidos)} → {CSV_SALIDA_DESCONOCIDOS}")