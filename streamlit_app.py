import streamlit as st

st.title("🎈 My new app")
st.markdown(
    """
    <style>
    button {
        width: 50vw !important; 
        height: 10vh !important;
        background-color: #ADD8E6 !important; 
        color: white !important; 
        font-size: 2rem !important;
        border: none !important; 
        border-radius: 10px !important; 
        cursor: pointer !important; 
        transition: background-color 0.3s ease, transform 0.3s ease !important; 
    }
    
    button:hover {
        background-color: #87CEFA !important; 
        transform: scale(1.05) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.button("STOP")
st.button("PLAY")
st.button("PAUSE")
