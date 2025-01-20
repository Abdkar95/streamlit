import streamlit as st

st.header("C'est mon premier Streamlit App")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')