import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'Quelles sont vos couleurs préférées',
    ['Vert', 'Jaune', 'Rouge', 'Bleu', 'Noir', 'Blanc', 'Marron', 'Violet', 'Rose', 'Orange', 'Gris', 'Beige'],
    ['Jaune', 'Rouge']
)
st.write('Vous avez sélectionné:', options)
