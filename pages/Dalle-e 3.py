import streamlit as st
from openai import OpenAI

st.title("Dalle-e 3")
st.write("Veillez entré une description de l'image que vous souhaiter générer ")
description = st.text_input("veillez saisir votre déscription :")
st.write(description )
st.sidebar.title("Mariama Diallo")

cle=st.sidebar.text_input("Veiller saisir votre clé")
# OpenAI pour générer des images



client = OpenAI(api_key=cle)


# Testez ici plusieurs variation du prompte
prompt = "A cute baby sea otter"



image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)




