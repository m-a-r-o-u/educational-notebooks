# educational-notebooks

A small collection of educational Jupyter notebooks, organized by topic.

## Notebook catalogue

<!-- NOTEBOOK_TABLE_START -->
| Category | Topic | Notebook | Level | Description | Tags |
| --- | --- | --- | --- | --- | --- |
| datasets | Exploring FineWeb-Edu | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/datasets/exploring-fineweb-edu.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/datasets/exploring-fineweb-edu.ipynb) | Beginner | Stream a small sample from FineWeb-Edu and explore its text, quality scores, and source domains without downloading the full dataset. | Datasets, Hugging Face, NLP |
| interpretability | Orthogonality in High Dimensions | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/interpretability/orthogonality-in-high-dimensions.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/interpretability/orthogonality-in-high-dimensions.ipynb) | Beginner | Explore why random vectors become nearly orthogonal in high dimensions, how optimization can push vectors apart, and how this geometry relates to the Johnson–Lindenstrauss lemma. | Interpretability, Linear Algebra, High-Dimensional Geometry, Johnson–Lindenstrauss |
| language-models | 01 — From Text to Next-Token Prediction | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/01-from-text-to-next-token-prediction.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/01-from-text-to-next-token-prediction.ipynb) | Beginner | Build a tiny language model from text, inspect its possible next tokens, and generate new text one token at a time. | Language Models, GPT, Next-Token Prediction, Generation |
| language-models | 02 — Tensors, Weights, and Layers | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/02-tensors-weights-and-layers.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/02-tensors-weights-and-layers.ipynb) | Beginner | Build the minimal numerical foundations of deep learning with NumPy and PyTorch: tensors, shapes, matrix multiplication, weights, biases, linear layers, and a tiny training loop. | Deep Learning, NumPy, PyTorch, Tensors, Linear Layers |
| tokenization | Byte Pair Encoding | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/tokenization/byte-pair-encoding.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/tokenization/byte-pair-encoding.ipynb) | Beginner | Learn how Byte Pair Encoding builds a vocabulary by repeatedly merging frequent symbol pairs. | NLP, Tokenization |
| transformers | Attention | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/transformers/attention.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/transformers/attention.ipynb) | Intermediate | Explore scaled dot-product attention with a small NumPy example. | Transformers, Deep Learning |
<!-- NOTEBOOK_TABLE_END -->

## Usage

Install the project dependency, then regenerate this catalogue whenever notebooks
are added or changed:

```bash
python -m pip install .
python scripts/update_readme.py
```

Every notebook belongs somewhere under `notebooks/`. Its first folder is used as
the category, and its first Markdown cell can include optional metadata:

```markdown
# Notebook title

**Description:** A short explanation of the notebook.
**Level:** Beginner
**Tags:** Python, Fundamentals
```
