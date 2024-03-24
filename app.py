import streamlit as st
import pandas

st.title('Demo App')


input_file = st.file_uploader('Upload file',type='csv')
if input_file is not None:
    st.write('File uploaded')
    df = pandas.read_csv(input_file, delimiter=';')
    st.write(df)




