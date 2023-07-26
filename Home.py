from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="James G. Lang", 
                   page_icon=":tada:", 
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   menu_items={'About':'# This is a header. cool!'})


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

## ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m4wmgweb.json")
img_head_shot = Image.open("images/headshot.png")

## ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, I am James :wave:")
    st.title("A Data Analyst studying at Georgia Tech's Online Master of Science in Analytics Program")
    st.write("I am passionate about finding ways to use python and VBA to be more efficient")
    st.write("[This is a link >](https://google.com)")

## ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
        """
        This is a paragraph about me: I like to create data science projects and hope to one day
        use data science to change the world for the better. On this website you will find
        - I like pie
        - There was one time that I made a website
        - Some cool data science projects.
        """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="analytics")

## ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_head_shot)
    with text_column:
        st.subheader("Real Estate Recommendation Engine")
        st.write(
            """
            Find Real Estate Arbitrage Opportunities!
            This app identifies low priced real estate opportunities or properties that have 
            been on the market for longer than the median days on market for the surrounding properties
            """
        )
        st.write("[Check it out here!](https://public.tableau.com/app/profile/cse6242team156/viz/CSE6242_DVA_TEAM_156_Project_Dashboard/FinalDashboard)")

## ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    # Documentation: https://formsubmit.co/ !!! Change Email !!!
    contact_form = """
    <form action="https://formsubmit.co/jameslang@gatech.edu" method="POST">
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