# 🧠 OntoGen（オントジェン）

本プロジェクトは、論文「Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation」に着想を得て、T5などのニューラル機械翻訳モデルを用いた製品分類システムの実装を目的としています。

---

## 🧭 目次

* [ℹ️ 詳細情報](/docs/model.md)

# 🧠 OntoGen：機械翻訳によるセマンティック製品分類

本プロジェクトは、論文 **「Don't Classify, Translate: Multi-Level E-Commerce Product Categorization via Machine Translation」** を参考にして、T5のような機械翻訳モデルを使った製品分類システムを実現します。

---

## 📑 論文の結果

| モデル                 | RDCデータセット      | Ichibaデータセット   |
| ------------------- | -------------- | -------------- |
| DBN+KNN（分類器）        | 73.85 (F1)     | 82.05 (F1)     |
| Transformer（NMT）    | 73.83 (F1)     | **84.74 (F1)** |
| Seq2Seq+Transformer | **74.19 (F1)** | **84.26 (F1)** |

* 翻訳ベースのモデルは**常に同等またはそれ以上の精度**を示しました。
* 少ない学習データでも**精度の低下が小さい**です。
* **新しい分類パスを生成し、元のタクソノミーを拡張**する能力があります。

---

## 🔍 製品翻訳の例

**入力例:**
`Epson WorkForce Pro Inkjet Printer`

**期待される出力:**

```
電子機器 → プリンター → プリンタ本体
```

**生成された別の出力例:**

```
オフィス用品 → プリンター → プリンタ本体
```

どちらも妥当な分類であり、**製品の文脈を理解するモデルの能力**を示しています。

---

## 🚀 インストール手順

1. **リポジトリをクローン**:

```bash
git clone https://github.com/vayioleta/ontoGen.git
cd ontoGen
```

2. **仮想環境を作成・有効化**:

```bash
conda create -n ontogen python=3.10 -y
conda activate ontogen
```

3. **依存関係をインストール**:

```bash
pip install -r requirements.txt
```

---

## 📂 必要なファイル構成

* `data/productos_train.csv` — 学習用データセット
* `data/productos_reales.csv` — 分類対象の製品記述
* `data/categorias_validas.csv` — 有効なカテゴリ一覧

---

## ⚙️ 使い方

### 🔧 モデルの学習

```bash
python src/train.py
```

`data/productos_train.csv` を用いて学習し、`data/categorias_validas.csv` で検証を行います。

### 🔎 単体推論（1対1）

```bash
python src/inference.py
```

コンソールから製品記述を入力し、予測されたカテゴリを返します。

### 🧪 バッチ推論

```bash
python src/inference_batch.py
```

`data/productos_reales.csv` を読み込み、予測を実行して次のファイルに保存します:

* `out/clasificados_conocidos.csv`
* `out/clasificados_desconocidos.csv`

### ✅ 精度評価（正解ラベル付き）

```bash
python src/test_batch.py
```

予測結果を正解ラベルと比較し、正答率（accuracy）を算出します。

---

## ✍️ 注意点

* すべてのCSVファイルはUTF-8でエンコードされている必要があります。
* `productos_train.csv` のカテゴリは `categorias_validas.csv` と完全に一致している必要があります。
* 学習および推論時に `"clasifica: "` プレフィックスが自動的に追加されます。

---

## 📚 学術的参考文献

OntoGenのアプローチは、製品分類を逐次的な翻訳問題として再構築するという発想に基づいています。以下の論文に詳しく説明されています：

> Li, M. Y., Kok, S., & Tan, L. (2018).
> *Don’t Classify, Translate: Multi-Level E-Commerce Product Categorization Via Machine Translation*.
> arXiv preprint [arXiv:1812.05774](https://arxiv.org/abs/1812.05774)

この研究では、従来の分類器ではなくTransformerベースの機械翻訳モデルを用いて、製品の説明文をeコマースの階層的なタクソノミーに変換する手法が提案されています。
