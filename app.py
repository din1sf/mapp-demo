import streamlit as st
import pandas

st.title('Demo App')

input_file = st.file_uploader('Upload file',type='csv')
if input_file is not None:
    st.write('File uploaded')
    df = pandas.read_csv(input_file, delimiter=',')    

    st.dataframe(
    df,
    hide_index=True,
    column_config={
        "id": st.column_config.TextColumn(label="ID"),
        "owner": st.column_config.TextColumn(label="Owner"),
        "action": st.column_config.TextColumn(label="Action"),
    },
    width=800,
    )
    st.button('Action Button')
             




