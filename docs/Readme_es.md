# 🧠 OntoGen

Este proyecto se inspira en el paper "Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation" para implementar un sistema de clasificación de productos basado en modelos de traducción automática como T5.

---

## 🧭 Índice

- [ℹ️ Más información](/docs/model.md)

# 🧠 OntoGen: Clasificación Semántica de Productos via Traducción Automática

Este proyecto se inspira en el paper **"Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation"** para implementar un sistema de clasificación de productos basado en modelos de traducción automática como T5.

---

## 📑 Resultados del Paper

| Modelo                 | Dataset RDC    | Dataset Ichiba |
| ---------------------- | -------------- | -------------- |
| DBN+KNN (Clasificador) | 73.85 (F1)     | 82.05 (F1)     |
| Transformer (NMT)      | 73.83 (F1)     | **84.74 (F1)** |
| Seq2Seq+Transformer    | **74.19 (F1)** | **84.26 (F1)** |

* El modelo basado en traducción automática fue **consistentemente superior o igual**.
* Con menos datos de entrenamiento, **degrada menos su rendimiento**.
* **Crea nuevas rutas** que enriquecen la taxonomía original.

---

## 🔍 Ejemplo de Traducción de Producto

**Input:** "Epson WorkForce Pro Inkjet Printer"

**Salida esperada:**

```
Electrónica → Impresión → Impresoras
```

**Salida alternativa generada:**

```
Oficina → Impresión → Impresoras
```

Ambas son válidas, mostrando la **capacidad del modelo para comprender el contexto** del producto.



## 🚀 Instalación

1. **Clona el repositorio**:
```bash
git clone https://github.com/vayioleta/ontoGen.git
cd ontoGen
```

2. **Crea un entorno virtual y activa**:
```bash
conda create -n ontogen python=3.10 -y
conda activate ontogen
```

3. **Instala dependencias**:
```bash
pip install -r requirements.txt
```

---

## 📂 Estructura esperada de archivos

- `data/productos_train.csv` — Dataset de entrenamiento
- `data/productos_reales.csv` — Descripciones reales a clasificar
- `data/categorias_validas.csv` — Lista de categorías válidas

---

## ⚙️ Cómo usar

### 🔧 Entrenamiento del modelo
```bash
python src/train.py
```
Esto entrena el modelo con los datos de `data/productos_train.csv` y valida contra `data/categorias_validas.csv`.

### 🔎 Inferencia individual (1 a 1)
```bash
python src/inference.py
```
Se solicita una entrada por consola y devuelve la categoría predicha.

### 🧪 Inferencia por lote (batch)
```bash
python src/inference_batch.py
```
Toma los datos desde `data/productos_reales.csv`, predice categorías y guarda:
- `out/clasificados_conocidos.csv`
- `out/clasificados_desconocidos.csv`

### ✅ Evaluación de precisión (con etiquetas conocidas)
```bash
python src/test_batch.py
```
Compara las predicciones con los valores reales de `output` y reporta accuracy.

---

## ✍️ Consideraciones
- Todos los archivos CSV deben estar en codificación UTF-8.
- Las categorías en `productos_train.csv` deben coincidir exactamente con las de `categorias_validas.csv`.
- El prefijo "clasifica: " se agrega automáticamente durante el entrenamiento e inferencia.

---

## 📚 Referencia científica

El enfoque de OntoGen está inspirado en la idea de reformular la clasificación de productos como un problema de traducción secuencial, siguiendo la metodología descrita en:

> Li, M. Y., Kok, S., & Tan, L. (2018).  
> *Don’t Classify, Translate: Multi-Level E-Commerce Product Categorization Via Machine Translation*.  
> arXiv preprint [arXiv:1812.05774](https://arxiv.org/abs/1812.05774)

Este trabajo propone utilizar modelos de traducción automática (como los basados en Transformers) para convertir descripciones de productos en rutas jerárquicas dentro de taxonomías de e-commerce, en lugar de usar clasificadores tradicionales.
