import streamlit as st
st.title('Streamlit basics')
st.header('Welcome to streamlit')
st.subheader('This is a simple subheader')
st.text('you can write a plain text here')

from PIL import Image
img=Image.open('streamlit.png')
st.image(img,width=200)

st.button("click me for no reason")

if(st.button("About")):
    st.text('Welcome ')

name=st.text_input("enter your name","Type here..")
if(st.button("Submit")):
    result=name.title()
    st.success(result)