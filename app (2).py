import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load BLIP model and processor
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Streamlit UI
st.title("Image Captioning Model")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Generating description...")

    # Preprocess the image
    inputs = processor(images=image, return_tensors="pt")

    # Generate the caption
    with torch.no_grad():
        output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    st.success("Generated Caption:")
    st.write(f"**{caption}**")
