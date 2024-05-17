import streamlit as st
from PIL import Image
from rembg import remove 

def remove_bg(image, widget):
    bytes_data = Image.open(image)
    output = remove(bytes_data)
    widget.title('foto sem fundo')
    widget.image(output)


st.title('Upload de arquivo')
image = st.file_uploader('Escolha uma imagem', type=['png', 'jpg', 'jpeg'])

col_a, col_b = st.columns(2)

if image is not None:
    col_a.title('foto original')
    col_a.image(image)
    st.button('Reover fundo', on_click=remove_bg, args=(image, col_b))