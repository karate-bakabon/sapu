import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

st.title('サプーアプリ')
st.caption('これはテスト')

image=Image.open('./data/PNG.png')
st.image(image,width=200)
