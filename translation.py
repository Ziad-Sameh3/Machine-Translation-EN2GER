import streamlit as st
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM


# Load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("tokenize/")
    model = TFAutoModelForSeq2SeqLM.from_pretrained("tf_model/")
    return tokenizer, model


tokenizer, model = load_model()

# Streamlit app
st.title("Machine Translation English to German App")
input_text = st.text_area(
    "English Text:", "", placeholder="Enter Text", key="input_text"
)


if st.button("Translate"):
    tokenized = tokenizer([input_text], return_tensors="np")
    output = model.generate(**tokenized, max_length=128)

    with tokenizer.as_target_tokenizer():
        translation = tokenizer.decode(output[0], skip_special_tokens=True)

    st.subheader("Translation")
    st.success(translation)
