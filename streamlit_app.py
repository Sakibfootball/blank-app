import streamlit as st

st.title("🎈 My new app")
st.markdown(
    """<style>
        .element-container:nth-of-type(3) button {
            width: 50vw; /* 50% of the viewport width */
              height: 50vh; /* 50% of the viewport height */
          background-color: #4CAF50; /* Green background */
      color: white; /* White text color */
      font-size: 2rem; /* Font size */
      border: none; /* Remove border */
      border-radius: 10px; /* Rounded corners */
      display: flex; /* Flexbox to center content */
      justify-content: center; /* Center horizontally */
      align-items: center; /* Center vertically */
      cursor: pointer; /* Pointer cursor on hover */
      transition: background-color 0.3s ease, transform 0.3s ease;
        }
        </style>""",
    unsafe_allow_html=True,
)

st.button("STOP")

st.button("PLAY")

st.button("PAUSE")
