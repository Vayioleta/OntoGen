import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

MODEL_DIR = os.path.abspath("/../models/ontotransformer-retrained")

print("📥 Cargando modelo y tokenizer...")
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
model.eval()

def inferir(texto_input):
    prefijo = "clasifica: "  # ← ¡Muy importante!
    entrada = prefijo + texto_input.strip()

    input_ids = tokenizer(entrada, return_tensors="pt", padding=True, truncation=True).input_ids
    outputs = model.generate(
        input_ids=input_ids,
        max_length=64,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=2
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    print("\n🧪 Ingreso para inferencia")
    entrada = input("📝 Ingresa un texto de entrada: ")
    resultado = inferir(entrada)
    print(f"\n🔮 Resultado:\n{resultado}")
