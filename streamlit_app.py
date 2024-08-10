import streamlit as st

st.title("🎈 My new app")
st.markdown(
    """
    <style>
    .custom-buttons button {
        width: 50vw !important; 
        height: 10vh !important;
        background-color: #ADD8E6 !important; 
        color: white !important; 
        font-size: 1rem !important;
        border: none !important; 
        border-radius: 10px !important; 
        cursor: pointer !important; 
        transition: background-color 0.3s ease, transform 0.3s ease !important; 
    }
    
    .custom-buttons button:hover {
        background-color: #87CEFA !important; 
        transform: scale(1.05) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-buttons">
        <button id="button1">Button 1</button>
        <button id="button2">Button 2</button>
        <button id="button3">Button 3</button>
    </div>
    """,
    unsafe_allow_html=True
)


