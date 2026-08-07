# educational-notebooks

A small collection of educational Jupyter notebooks, organized by topic.

## Notebook catalogue

<!-- NOTEBOOK_TABLE_START -->
| Category | Topic | Notebook | Level | Description | Tags |
| --- | --- | --- | --- | --- | --- |
| datasets | Exploring FineWeb-Edu | [Open](notebooks/datasets/exploring-fineweb-edu.ipynb) | Beginner | Stream a small sample from FineWeb-Edu and explore its text, quality scores, and source domains without downloading the full dataset. | Datasets, Hugging Face, NLP |
| interpretability | Orthogonality in High Dimensions | [Open](notebooks/interpretability/orthogonality-in-high-dimensions.ipynb) | Beginner | Explore why random vectors become nearly orthogonal in high dimensions, how optimization can push vectors apart, and how this geometry relates to the Johnson–Lindenstrauss lemma. | Interpretability, Linear Algebra, High-Dimensional Geometry, Johnson–Lindenstrauss |
| tokenization | Byte Pair Encoding | [Open](notebooks/tokenization/byte-pair-encoding.ipynb) | Beginner | Learn how Byte Pair Encoding builds a vocabulary by repeatedly merging frequent symbol pairs. | NLP, Tokenization |
| transformers | Attention | [Open](notebooks/transformers/attention.ipynb) | Intermediate | Explore scaled dot-product attention with a small NumPy example. | Transformers, Deep Learning |
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
