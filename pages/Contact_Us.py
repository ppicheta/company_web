import streamlit as st
from email_class import Gmail
import pandas as pd


gmail = Gmail('neonrobot9@gmail.com', 'pash ggce smtl hxzi ') 
st.header('Contact Me')
df = pd.read_csv('topics.csv')

with st.form(key="email_form"):
    user_email = st.text_input('Your email address')
    message_subject = st.text_input('Subject of your message')
    option_list = st.selectbox('Please select a topic:', df)
    message = st.text_area('Your message')
    message_email = f"""
        {message}\n{user_email}
        """
        
    button = st.form_submit_button()
    if button:
        gmail.send_email(message_subject, message_email)
        st.info("Your email was sent successfully")

