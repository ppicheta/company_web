import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv', sep=',')

st.title('The Best Company')
content1 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content1)

st.header('Our Team')

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:5].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[5:9].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[9:].iterrows():
        st.header(row['first name'] + row['last name'])
        st.write(row['role'])
        st.image('images/' + row['image'])
