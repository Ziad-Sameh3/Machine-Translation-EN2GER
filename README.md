# 🌍 Machine Translation EN→GER

This project is a neural machine translation (NMT) system that translates English sentences into German using Transformer-based models.

---

## 📌 Features

* ✅ Trained on parallel English-German data
* ✅ Built with Hugging Face Transformers
* ✅ Uses `MarianMTModel` and `sentencepiece` tokenizer
* ✅ Evaluation metrics: Multi Cross Entropy
* ✅ Exportable and deployable model

---

## 📁 Project Structure

```plaintext
├── machine-translation-en2ger.ipynb   # Main notebook for training and inference
├── translation.py                     # Script for performing translation
├── tokenizer/                         # Contains SentencePiece tokenizer files
├── Deployment.png                     # Preview of deployment architecture
├── README.md                          # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Machine-Translation-EN2GER.git
cd Machine-Translation-EN2GER
```

### 2. Install requirements

```bash
pip install -r requirements.txt
# or manually
pip install transformers datasets sentencepiece evaluate
```

### 3. Run the Notebook

Use the Jupyter Notebook:

```
machine-translation-en2ger.ipynb
```

Or run the script:

```bash
python translation.py
```

---

## 📦 Download the Pretrained Model

> 🔽 **[Download the model weights](./path-to-model/tf_model)**

Make sure to place the model inside the correct directory structure for inference.

---



## 📷 Deployment

<img src="Deployment.png" alt="Model Deployment" width="600"/>

---

## 🤖 Model Architecture

Uses the pretrained [`Helsinki-NLP/opus-mt-en-de`](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) model based on **MarianMT**, fine-tuned with custom parallel corpora.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.


