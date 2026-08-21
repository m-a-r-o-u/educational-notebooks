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
| language-models | 03 — Tokens and Embeddings | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/03-tokens-and-embeddings.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/03-tokens-and-embeddings.ipynb) | Beginner | Turn text into token IDs, build an embedding matrix, look up vectors with NumPy and PyTorch, and track shapes through batches and sequences. | Language Models, Tokenization, Embeddings, NumPy, PyTorch |
| language-models | 04 — Understanding Embedding Space | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/04-understanding-embedding-space.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/04-understanding-embedding-space.ipynb) | Beginner | Measure similarity with dot products and cosine similarity, find nearest neighbors, explore semantic directions, and visualize embedding spaces. | Language Models, Embeddings, Similarity, Vector Geometry, Visualization |
| language-models | 05 — From Hidden State to Probabilities | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/05-from-hidden-state-to-probabilities.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/05-from-hidden-state-to-probabilities.ipynb) | Beginner | Transform a model's hidden state into vocabulary logits, implement numerically stable softmax, and inspect the resulting next-token probabilities. | Language Models, Unembedding, Logits, Softmax, Probabilities |
| language-models | 06 — Sampling and Temperature | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/06-sampling-and-temperature.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/06-sampling-and-temperature.ipynb) | Beginner | Turn next-token probabilities into generated text, compare greedy decoding with sampling, and control randomness using temperature. | Language Models, Generation, Sampling, Temperature, Decoding |
| language-models | 07 — Why Attention? From Static to Contextual Embeddings | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/07-why-attention-from-static-to-contextual-embeddings.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/07-why-attention-from-static-to-contextual-embeddings.ipynb) | Beginner | Discover why one fixed vector per token is not enough, then construct and visualize simple context-dependent updates by hand. | Language Models, Embeddings, Context, Attention, Visualization |
| language-models | 08 — Queries, Keys, and Attention Scores | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/08-queries-keys-and-attention-scores.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/08-queries-keys-and-attention-scores.ipynb) | Beginner | Project embeddings into queries and keys, compute every query–key dot product, and visualize the resulting relevance scores. | Language Models, Attention, Queries, Keys, Matrix Multiplication |
| language-models | 09 — From Scores to Attention Patterns | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/09-from-scores-to-attention-patterns.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/09-from-scores-to-attention-patterns.ipynb) | Beginner | Convert query–key scores into attention weights using scaling, causal masking, and row-wise softmax. | Language Models, Attention, Softmax, Causal Masking, Visualization |
| language-models | 10 — Values and Contextual Embeddings | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/10-values-and-contextual-embeddings.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/10-values-and-contextual-embeddings.ipynb) | Beginner | Add value projections to attention weights, compute weighted sums, and build a complete single-head attention operation. | Language Models, Attention, Values, Contextual Embeddings, Weighted Sums |
| language-models | 11 — Multi-Head Attention and the Transformer Block | [GitHub](https://github.com/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/11-multi-head-attention-and-the-transformer-block.ipynb) or [Colab](https://colab.research.google.com/github/m-a-r-o-u/educational-notebooks/blob/main/notebooks/language-models/11-multi-head-attention-and-the-transformer-block.ipynb) | Beginner | Build multi-head causal self-attention in PyTorch, inspect distinct heads, combine them with an output projection, and place attention inside a minimal Transformer block. | Language Models, Transformers, Multi-Head Attention, PyTorch, Residual Connections |
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
