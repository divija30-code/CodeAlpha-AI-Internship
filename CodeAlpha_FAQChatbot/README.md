# FAQ Chatbot

## Overview

This project is an FAQ Chatbot built using Python, Flask, NLTK, and Scikit-learn.

The chatbot answers frequently asked questions by comparing the user's query with stored FAQs using NLP preprocessing and cosine similarity.

---

## Features

- FAQ dataset in JSON
- NLP preprocessing
- Tokenization
- Stopword removal
- TF-IDF Vectorization
- Cosine Similarity
- Flask Web Interface
- Fast responses

---

## Technologies

- Python
- Flask
- NLTK
- Scikit-learn
- HTML
- CSS

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/FAQ-Chatbot.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download NLTK data

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Project Workflow

1. Load FAQs
2. Preprocess text
3. Convert to TF-IDF vectors
4. Compute cosine similarity
5. Return best matching answer

---

## Example

User:

```
Explain machine learning
```

Bot:

```
Machine Learning is a subset of AI that enables computers to learn from data.
```

---

## Future Improvements

- Voice Input
- Speech Output
- Deep Learning Intent Classification
- Database Integration
- Chat History
- Multi-language Support
