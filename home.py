import streamlit as st 
import pandas
st.set_page_config(layout='wide')
col1,col2 = st.columns(2)

content = """Hey, This is Jaya Prakash Badavath, I'm presently pursuing my Bachelors in Ai&Ml.
I'm a passionate python Programmer.I have worked for small scale and medium firms and businesses in
our locality as a freelancer.
"""  
with col1:
    st.image('photo.png')
with col2:
       st.title('Jaya Prakash')
       
   
       st.info(content)


st.subheader("Some of the apps that I made are:")

col3,empty,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv',sep=';')

with col3:
    for index,items in df[10:].iterrows():
        st.header(items['title'])
        st.write(items['description'])
        st.image(items['image'])
        st.write(f"[Source code]({items['url']})")
        
with col4:
    for index,items in df[:10].iterrows():
        st.header(items['title'])
        st.write(items['description'])
        st.image(items['image'])
        st.write(f"[Source code]({items['url']})")