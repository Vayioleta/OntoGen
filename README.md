<!-- Language toggle -->

<p align="right">
  <a href="/README.md"> English</a> | <a href="/docs/Readme_es.md"> Español</a> | <a href="/docs/Readme_jp.md"> 日本語  </a>
</p>

# 🧠 OntoGen

This project is inspired by the paper *"Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation"* to implement a product categorization system based on neural machine translation models like T5.

---

## 🧭 Index

* [ℹ️ More Information](/docs/model.md)

# 🧠 OntoGen: Semantic Product Categorization via Machine Translation

This project is based on the paper **"Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation"**, implementing a product classification system using neural machine translation models such as T5.

---

## 📑 Paper Results

| Model                | RDC Dataset    | Ichiba Dataset |
| -------------------- | -------------- | -------------- |
| DBN+KNN (Classifier) | 73.85 (F1)     | 82.05 (F1)     |
| Transformer (NMT)    | 73.83 (F1)     | **84.74 (F1)** |
| Seq2Seq+Transformer  | **74.19 (F1)** | **84.26 (F1)** |

* The translation-based model was **consistently equal or superior**.
* With less training data, it **degrades less in performance**.
* **Generates new paths** that enrich the original taxonomy.

---

## 🔍 Product Translation Example

**Input:** "Epson WorkForce Pro Inkjet Printer"

**Expected output:**

```
Electronics → Printing → Printers
```

**Alternative output generated:**

```
Office → Printing → Printers
```

Both are valid, showing the model’s **ability to understand the product’s context**.

---

## 🚀 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/vayioleta/ontoGen.git
cd ontoGen
```

2. **Create and activate a virtual environment**:

```bash
conda create -n ontogen python=3.10 -y
conda activate ontogen
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## 📂 Expected File Structure

* `data/productos_train.csv` — Training dataset
* `data/productos_reales.csv` — Real descriptions to classify
* `data/categorias_validas.csv` — List of valid categories

---

## ⚙️ How to Use

### 🔧 Train the model

```bash
python src/train.py
```

This trains the model using `data/productos_train.csv` and validates against `data/categorias_validas.csv`.

### 🔎 Single (1-to-1) Inference

```bash
python src/inference.py
```

Prompts input from the console and returns the predicted category.

### 🧪 Batch Inference

```bash
python src/inference_batch.py
```

Reads from `data/productos_reales.csv`, predicts categories, and saves:

* `out/clasificados_conocidos.csv`
* `out/clasificados_desconocidos.csv`

### ✅ Accuracy Evaluation (with known labels)

```bash
python src/test_batch.py
```

Compares predictions with true labels in `output` and reports accuracy.

---

## ✍️ Notes

* All CSV files must be UTF-8 encoded.
* Categories in `productos_train.csv` must match exactly with those in `categorias_validas.csv`.
* The prefix "clasifica: " is automatically added during training and inference.

---

## 📚 Scientific Reference

The OntoGen approach is inspired by the idea of reformulating product classification as a sequential translation problem, following the methodology described in:

> Li, M. Y., Kok, S., & Tan, L. (2018).
> *Don’t Classify, Translate: Multi-Level E-Commerce Product Categorization Via Machine Translation*.
> arXiv preprint [arXiv:1812.05774](https://arxiv.org/abs/1812.05774)

This work proposes the use of machine translation models (such as Transformer-based ones) to convert product descriptions into hierarchical taxonomy paths in e-commerce, rather than using traditional classifiers.
