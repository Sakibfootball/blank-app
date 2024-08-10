import streamlit as st

st.title("🎈 My new app")
st.markdown(
    """<style>
        .element-container:nth-of-type(3) button {
            height: 10em;
            width: 40em
        }
        </style>""",
    unsafe_allow_html=True,
)

st.button("STOP")

st.button("PLAY")

st.button("PAUSE")
