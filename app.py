import streamlit as st
from PIL import Image

def main():
    st.title("Hello Golu")
    
    # Add your Streamlit app code here
    st.write("Good morning Daddy's Girl")
    image = st.camera_input("Take a picture")

    img = Image.open(image)

    grey_scale = img.convert("L")

    st.image(grey_scale)



    
    
if __name__ == "__main__":
    main()
