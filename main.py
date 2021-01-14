import time

import requests
import streamlit as st
from PIL import Image
import os

STYLES = {
    "unet": "U-net-efficientnet",
    "featurepyramidnetwork": "FPN-efficientnet",
    "linknet": "LinkedNet",
}

HOST = "http://154.61.75.187:5000/"

st.set_option("deprecation.showfileUploaderEncoding", False)

st.set_page_config(
        page_title="Segmentor",  # default page title
        layout="wide",
        initial_sidebar_state="expanded"  # "expanded", "collapsed"
    )

st.title("Image Segmentation Tool")
try:
    response = requests.get(HOST)
    status_check = 200
except requests.exceptions.ConnectionError:
    status_check = 0
    print("backend offline")

if status_check == 200:
    print('Backend Server was online')
    st.text('This tool is used to compare 3 segmentation models mentioned below')
    st.text('The backend Server is hosted on a private server with low capacity. Please be patient.')
    # Page when server is online
    image = st.file_uploader("Choose an image")
    st.text('This tool has been custom trained to segment cars/vehicles from images.')
    style = st.selectbox("Choose the model", [i for i in STYLES.keys()])
    st.markdown("More Info : [link](https://github.com/Ashish-Surve/Comparsion_Segmentation_models)")

    add_sidebar1 = st.sidebar.text("You can contribute to project by")
    add_sidebar2 = st.sidebar.image("https://cdn-images-1.medium.com/max/1200/1*Dw4-tOJ_9myFUywLd3qzjA.png",width = 30)
    add_sidebar3 = st.sidebar.text("PayPal \n paypal.me/Asurve")
    add_sidebar4 = st.sidebar.markdown('[Connect](https://www.linkedin.com/in/ashish-surve/)')
    if st.button("Find Car!"):
        if image is not None and style is not None:
            files = {"file": image.getvalue()}
            res = requests.post(HOST+f"{style}", files=files)
            file = open("sample_image.png", "wb")
            file.write(res.content)
            file.close()
            # DEBUG
            # image_p = r"../backend/"+ img_path.get("name")
            # Docker
            # image_p = img_path.get("name")
            image = Image.open("sample_image.png")

            st.image(image)
            os.remove("sample_image.png")
            displayed_styles = [style]
            displayed = 1
            total = len(STYLES)
else :
    print('Backend Server is offline')
    st.text('The backend Server is offline. The Server is paid and needs support to stay online.')
    st.text('Ping me for support.')
    st.text('[Connect](https://www.linkedin.com/in/ashish-surve/)')


