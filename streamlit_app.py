import streamlit as st

st.title("🎈 My new app")
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


