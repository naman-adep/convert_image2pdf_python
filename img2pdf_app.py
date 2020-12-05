#Import modules
import streamlit as st 
import img2pdf
import os

#Title
st.title("Image to PDF convertor")

#Select box
img_file = st.selectbox('Select a file', os.listdir('.'))

#Convert from Image to PDF
if st.button("Convert"):
	filename = os.path.join('.', img_file)
	st.write('You selected `%s`' % filename)
	pdf_file = open('output.pdf','wb')
	pdf_file.write(img2pdf.convert(filename))
	pdf_file.close()
	st.write('Converted file is saved as output.pdf')


