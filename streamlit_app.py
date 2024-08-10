import streamlit as st

st.title("MPS Monitoring System")
st.markdown(
    """
    <style>
    .custom-buttons {
        display: flex;
        flex-direction: column; /* Stack buttons vertically */
        # align-items: center; /* Center buttons horizontally */
    }

    .custom-buttons a {
        text-decoration: none; /* Remove underline from links */
        display: inline-block;
        width: 50vw !important; 
        height: 10vh !important;
        margin-bottom: 20px !important;
    }

    .custom-buttons button {
        width: 100%; 
        height: 100%;
        background-color: #3b778a !important; /* Dodger Blue */
        color: white !important; 
        font-size: 2rem !important;
        border: none !important; 
        border-radius: 10px !important; 
        cursor: pointer !important; 
        transition: background-color 0.3s ease, transform 0.3s ease !important; 
    }
    
    .custom-buttons button:hover {
        background-color: #1C86EE !important; /* Slightly darker Dodger Blue */
        transform: scale(1.05) !important;
    }
    </style>

    <div class="custom-buttons">
        <a href="https://www.google.com" target="_blank">
            <button id="button1">Go to Example 1</button>
        </a>
        <a href="https://www.google.com" target="_blank">
            <button id="button2">Go to Example 2</button>
        </a>
        <a href="https://www.google.com" target="_blank">
            <button id="button3">Go to Example 3</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
