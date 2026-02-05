



from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()   


# Configure API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  

# Set up Streamlit page configuration
st.set_page_config(page_title="Crisbee Chat Bot", page_icon="🤡")

# Set the correct path for the logo(Your path)
logo_path = "logo1.png"

# Display Logo
st.image(logo_path, width=90)

# Custom CSS for Modern U I
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #1e1e1e, #2c2c2c);
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput, .stButton button {
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
    }
    .stTextInput {
        background: rgba(255, 255, 255, 0.2);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 style='text-align: center; color: white;'> Crisbee Chat Bot</h1>", unsafe_allow_html=True) 

# User Input
input_text = st.text_input("Write your question here...", key='input')

# Submit Button
if st.button("Submit"):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(input_text)
    
    # Display Response
    st.markdown("<h3 style='color: white;'>Bot's Response:</h3>", unsafe_allow_html=True)
    st.write(response.text)






