from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My Webpage", page_icon = ":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img1 = Image.open("images/tmu-logo-full-colour.png")

with st.container():
    st.subheader("Hi, I am Syed :wave:")
    st.title("Software Engineering Student")
    st.write("Passionate about learning all about programming and computers in general")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Projects")
        st.write("##")
        st.write("""
                 
                 
                 """)
        st.write("Coming Soon...")
        st.write("[Github](https://github.com/syedk04)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Education")
    st.write("##")
    image_column, text_column = st.columns((1,2)) # text column 2x big as image column
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("Courses Completed")
        st.write("""
                 Algorithms and Data Structures \n
                 Object Oriented Analysis Design \n
                 Electric Networks \n
                 Software Systems \n
                 Digital Systems
                 """)
    
with st.container():
    st.write("---")
    st.header("Contact Information")
    st.write("##")
    
    contact_form = """ 
    <form action="https://formsubmit.co/syedk.business@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    