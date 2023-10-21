import streamlit as st
from ultralytics import YOLO
from PIL import Image 
st.title('Dog Breed Classification App')

import base64


@st.cache_data
def get_img_as_base64(file):
  with open(file,"rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()

img2 = get_img_as_base64("dog1.jpg")
img = get_img_as_base64("texture.jpg")

page_bg_img = f"""
<style>
[data-testid = "stAppViewContainer"] {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
}}

[data-testid = "stSidebar"] {{
background-image: url("data:image/png;base64,{img2}");
background-size: cover;
background-position: center;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

@st.cache_resource
def my_model():
 model = YOLO('best.pt')
 return model
# st.file_uploader fetches the image or video from the computer onto the server
img = st.file_uploader("Upload your dog's image and find out its breed!")

checkCamera = st.checkbox("Upload the image using camera")
if checkCamera:
  img = st.camera_input("Take a picture")



if img is not None:
  im = Image.open(img)
  st.image(im)
  mod = my_model()
  # .predict() predicts the probability using a list of dat
  res = mod.predict(im)
  temp = res[0].probs.top5
  # conf gives the confidence value of the prediction
  conf = res[0].probs.top5conf
  conf = conf.tolist()
  col = st.columns(2)
  
  with col[0]:
    for i in temp:
      # names[index] returns the of the class
      st.write(res[0].names[i])
             
  
  with col[1]:
    for i in conf:
      i = round(i,2)
      i = i*100
      st.write(str(i),"%") 
  
    
rating = st.slider("Rate the guess: ", 0, 10, 1)
st.write("Rating: ", rating)


