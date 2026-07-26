import streamlit as st

st.set_page_config(
    page_title="Veritix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Veritix AI Assistant")

st.write("Welcome to Veritix AI")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose a tool",
    [
        "Dashboard",
        "Chat",
        "Summarizer",
        "Email Writer",
        "Reports"
    ]
)

st.header(page)

if page == "Dashboard":
    st.success("System Ready")

elif page == "Chat":
    st.info("Coming Soon")

elif page == "Summarizer":
    st.info("Coming Soon")

elif page == "Email Writer":
    st.info("Coming Soon")

elif page == "Reports":
    st.info("Coming Soon")