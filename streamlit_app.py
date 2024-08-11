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
        background-color: #2A3675 !important;
        color: white !important; 
        font-size: 1rem !important;
        border: none !important; 
        border-radius: 10px !important; 
        cursor: pointer !important; 
        transition: background-color 0.3s ease, transform 0.3s ease !important; 
    }
    
    .custom-buttons button:hover {
        background-color: #EE0909 !important; /* Slightly darker Dodger Blue */
        transform: scale(1.05) !important;
    }
    </style>

    <div class="custom-buttons">
        <a href="https://docs.google.com/document/d/1_kP1ZmlxJvEPXcC_KDG1TjvPAMtFX_aJ3jsZAM5HXJs/edit?usp=sharing" target="_blank">
            <button id="button1">BDU Status</button>
        </a>
        <a href="https://www.google.com" target="_blank">
            <button id="button2">Sub. EOI</button>
        </a>
        <a href="https://www.google.com" target="_blank">
            <button id="button3">Sub. Proposal</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
