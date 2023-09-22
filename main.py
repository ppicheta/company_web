import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

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
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[5:9].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[9:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])
