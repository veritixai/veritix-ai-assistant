import streamlit as st


def show():

    st.title("📚 Series Manager")

    with st.form("series_form"):

        name = st.text_input("Series Name")

        topic = st.text_input("Topic")

        style = st.selectbox(
            "Style",
            [
                "Educational",
                "Kids",
                "Story",
                "Business",
                "History",
                "AI",
                "Facts"
            ]
        )

        duration = st.selectbox(
            "Duration",
            [
                "30 Seconds",
                "60 Seconds"
            ]
        )

        videos = st.number_input(
            "Videos Per Day",
            min_value=1,
            max_value=20,
            value=3
        )

        status = st.selectbox(
            "Status",
            [
                "Active",
                "Paused"
            ]
        )

        submitted = st.form_submit_button("Create Series")

        if submitted:

            st.success("Series created successfully! (Database integration next)")