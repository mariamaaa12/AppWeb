import streamlit as st

st.title("Dalle-e 3")
st.write("Veillez entré une description de l'image que vous souhaiter générer ")
description = st.text_input("veillez saisir votre déscription :")
st.write(description )
st.sidebar.title("Mariama Diallo")

cle=st.sidebar.text_input("Veiller saisir votre clé")




