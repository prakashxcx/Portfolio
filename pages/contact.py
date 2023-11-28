import streamlit as st 
from send_email import send_email

st.header('CONTACT ME')
with st.form(key='Contact'):
    email= st.text_input("Enter your Email...")
    messege = st.text_area('Your messege...')
    messege = messege + '\n' + email
    button = st.form_submit_button('Submit')
    if button:
        send_email(messege)
        st.info("your email sent successfully")