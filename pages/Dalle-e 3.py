

import streamlit as st
import openai  # Importer le module OpenAI correctement

st.title("Dalle-e 3")
st.write("Veuillez entrer une description de l'image que vous souhaitez générer")
description = st.text_input("Veuillez saisir votre description :")
st.write(description)
st.sidebar.title("Mariama Diallo")

cle = st.sidebar.text_input("Veuillez saisir votre clé OpenAI")

# OpenAI pour générer des images
from openai import OpenAI


client = OpenAI(api_key=cle)




image = client.images.generate(
    model="dall-e-2",
    prompt=description,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)
st.image(image_url)
