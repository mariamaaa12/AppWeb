import streamlit as st

# pour les titre
st.title("Mon Formulaire")

# Texte
st.write("Ceci est un formulaire de contact")

# Champ de saisi
user_input =st.text_input("Tapez votre texte : ")

st.write(user_input)
