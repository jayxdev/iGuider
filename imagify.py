import streamlit as st
import random
from PIL import Image

# return image object of the given number to display in the streamlit app in question and answer section
def imageify(n):
	img=Image.open("res/img/"+str(n)+".png")
	st.image(img,width=350)
	n=n+1
	return n



