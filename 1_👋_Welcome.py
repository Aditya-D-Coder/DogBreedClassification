 
import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
  with open(file,"rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()

img = get_img_as_base64("dogBg.jpg")
img2 = get_img_as_base64("fur1.jpg")

page_bg_img = f"""
<style>
[data-testid = "stAppViewContainer"] {{
background-image: url("data:image/png;base64,{img2}");
background-size: cover;
background-position: center;
}}

[data-testid = "stSidebar"] {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
}}
</style>
"""

with open("bgStyle.css") as source_bg:
  st.markdown(f"<style>{source_bg.read()}</style>",unsafe_allow_html=True)


st.markdown('<style> h1{color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style> h2{color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style> h3{color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style> h4{color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style> h5{color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style> h6{color:white;}</style>', unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Welcome! :wave:")
st.title("This app will classify your dog's breed based on its image :dog2:")
st.text("")
st.text("")
st.text("")
name = st.text_input("Hi, what is your name: ", max_chars = 15,placeholder = "Name")
st.write('Welcome, ',name)


st.text("")
st.text("")
st.text("")

st.divider()
tab1, tab2  = st.tabs(["About this app", "About me"])

with tab1:
  st.header("Learn about this app")
  st.text("")
  st.write("This app classifies dog breeds by using a YOLO machine learning image classification model. The user is provided with two options: uploading an image or clicking an image through their camera. This app operates using a medium sized YOLO model and the algorithm has been trained and tested using 9350 images which have been run through 20 epochs(iterations).")
with tab2:
  st.header("Learn about the creator of this app")
  st.text("")
  st.write("Hello, I am Aditya Punj - a computer science enthusiast. I am an Indian citizen residing in Jakarta and studying at BSJ(British School of Jakarta). I enjoy programming, and have learnt JavaScript along with the basics of HTML and CSS. Currently, I am learning machine learning using python and have built this project.")
