import streamlit as st
import cv2
from colorizer import colorize_image

st.title("AI Powered Image Colorizer")

uploaded_file = st.file_uploader(
    "Upload a Black & White Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image("temp.jpg", caption="Original Image")

    if st.button("Colorize"):

        output = colorize_image("temp.jpg")

        cv2.imwrite("colorized_output.jpg", output)

        st.image(
            "colorized_output.jpg",
            caption="Colorized Image"
        )

        with open("colorized_output.jpg", "rb") as file:

            st.download_button(
                "Download Colorized Image",
                file,
                file_name="colorized_output.jpg"
            )