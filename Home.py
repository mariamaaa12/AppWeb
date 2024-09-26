import streamlit as st

# pour les titre
st.title("Mon Formulaire")

# Texte
st.write("Ceci est un formulaire de contact")

# Champ de saisi
user_input =st.text_input("Tapez votre texte : ")

st.write(user_input)

# image

st.image("https://www.google.com/imgres?q=eemi&imgurl=https%3A%2F%2Fwww.eemi.com%2Fuploads%2F2023%2F06%2Fsized%2FCampus-de-Paris-scaled-aspect-ratio-690-690-scaled-380x380.jpg&imgrefurl=https%3A%2F%2Fwww.eemi.com%2F&docid=dtSDTqB1srHmXM&tbnid=6hQXnPWtQ61KiM&vet=12ahUKEwjP1921zOCIAxXbTKQEHV0XLagQM3oECBgQAA..i&w=380&h=380&hcb=2&ved=2ahUKEwjP1921zOCIAxXbTKQEHV0XLagQM3oECBgQAA")
