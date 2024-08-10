import streamlit as st

st.title("🎈 My new app")
st.markdown(
    """<style>
         button {
          width: 50vw; 
          height: 10vh; 
          background-color: #ADD8E6;
          color: white; 
          font-size: 6rem;
          border: none; 
          border-radius: 10px; 
          display: flex; 
          justify-content: center;
          align-items: center; 
          cursor: pointer;
        }
        </style>""",
    unsafe_allow_html=True,
)

st.button("STOP")
st.button("PLAY")
st.button("PAUSE")
