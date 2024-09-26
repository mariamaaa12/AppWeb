

import streamlit as st
import openai  # Importer le module OpenAI correctement

st.title("Dalle-e 3")
st.write("Veuillez entrer une description de l'image que vous souhaitez générer")
description = st.text_input("Veuillez saisir votre description :")
st.write(description)
st.sidebar.title("Mariama Diallo")

cle = st.sidebar.text_input("Veuillez saisir votre clé OpenAI", type="password")

# Vérifiez que la clé est bien fournie
if cle:
    openai.api_key = cle  # Assigner la clé API correctement

    # Vérifiez que l'utilisateur a entré une description
    if description:
        # Appeler l'API pour générer une image avec DALL-E
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="512x512"
        )

        # Récupérer l'URL de l'image générée
        image_url = response['data'][0]['url']
        st.image(image_url, caption=f"Image générée pour : {description}")

    else:
        st.write("Veuillez entrer une description pour générer une image.")
else:
    st.write("Veuillez entrer votre clé API dans la barre latérale.")
