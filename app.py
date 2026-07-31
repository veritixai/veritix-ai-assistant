import streamlit as st

from services.pdf_service import read_pdf, get_pdf_statistics
from services.ai_service import summarize_text
from database.database import create_tables

st.set_page_config(
    page_title="Veritix AI Studio",
    page_icon="🤖",
    layout="wide"
)

create_tables()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Veritix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==============================
# Header
# ==============================
st.title("🚀 Veritix AI Studio")
st.caption("Create AI Videos • Chat • PDF • Automation")

# ==============================
# Sidebar
# ==============================
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose a tool",
   [
    "Dashboard",
    "AI Video Generator",
    "Chat",
    "Summarizer",
    "Email Writer",
    "Reports"
]
)

# ==============================
# Main Page
# ==============================
st.header(page)

# ==========================================================

# ==========================================================
# Dashboard
# ==========================================================
if page == "Dashboard":

    st.success("System Ready")

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        text = ""
        total_pages = 0

        for pdf in uploaded_files:

            try:
                pdf_text = read_pdf(pdf)

                text += pdf_text + "\n\n"

                pdf_stats = get_pdf_statistics(pdf, pdf_text)

                total_pages += pdf_stats["pages"]

            except Exception:
                st.warning(f"⚠️ Could not read: {pdf.name}")
                continue

        stats = {
            "pages": total_pages,
            "words": len(text.split()),
            "characters": len(text),
            "reading_time": round(len(text.split()) / 200)
        }

        st.success("✅ PDF(s) Loaded Successfully")

        st.subheader("📊 PDF Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Pages", stats["pages"])
            st.metric("Words", stats["words"])

        with col2:
            st.metric("Characters", stats["characters"])
            st.metric("Reading Time", f"{stats['reading_time']} min")

        st.subheader("📄 Preview")
        st.write(text[:10000])

        st.divider()

        if st.button("✨ Summarize with AI"):

            with st.spinner("AI is analyzing your PDF(s)..."):
                summary = summarize_text(text)

            st.subheader("📄 AI Summary")
            st.write(summary)

        st.divider()

        st.subheader("💬 Chat with PDF")

        question = st.text_input(
            "Ask a question about these documents"
        )

        if st.button("Ask AI") and question:

            from services.chat_service import ask_pdf

            with st.spinner("🤖 Veritix AI is thinking..."):

                answer = ask_pdf(
                    question,
                    text,
                    st.session_state.chat_history
                )

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

        if st.session_state.chat_history:

            st.subheader("💬 Conversation")

            for chat in st.session_state.chat_history:

                with st.chat_message("user"):
                    st.write(chat["question"])

                with st.chat_message("assistant"):
                    st.write(chat["answer"])



# ==========================================================
# AI Video Generator
# ==========================================================
elif page == "AI Video Generator":

    st.header("🎬 AI Video Generator")

    topic = st.text_input(
        "Video Topic",
        placeholder="e.g. 5 Facts About Space"
    )

    duration = st.selectbox(
        "Video Duration",
        ["30 Seconds", "60 Seconds"]
    )

    style = st.selectbox(
        "Style",
    [
        "Educational",
        "Kids",
        "Story",
        "Scary Stories",
        "Motivational",
        "Business",
        "History",
        "Science",
        "Technology",
        "Health",
        "Finance",
        "Psychology",
        "Travel",
        "Luxury",
        "News",
        "AI",
        "Quotes",
        "Facts",
        "Religion",
        "Language Learning"
    ]
)
    
if st.button("🚀 Generate Video"):

    from services.video_service import generate_video_script
    from services.tts_service import text_to_speech
    from services.scene_service import split_script_into_scenes

    with st.spinner("🤖 Creating script..."):

        script = generate_video_script(
            topic,
            style,
            duration
        )

    st.success("Script Generated!")

    st.subheader("📝 Video Script")
    st.write(script)

    scenes = split_script_into_scenes(script)

    st.subheader("🎬 Scenes")

    for i, scene in enumerate(scenes, start=1):
        st.write(f"Scene {i}")
        st.info(scene)

    with st.spinner("🎤 Generating voice..."):

        audio_file = text_to_speech(script)

    st.success("Voice Generated!")
    st.audio(audio_file)




    st.write(f"Saved to: {audio_file}")

# ==========================================================
# Chat
# ==========================================================
elif page == "Chat":

    st.info("Coming Soon")

# ==========================================================
# Summarizer
# ==========================================================
elif page == "Summarizer":

    st.info("Coming Soon")

# ==========================================================
# Email Writer
# ==========================================================
elif page == "Email Writer":

    st.info("Coming Soon")

# ==========================================================
# Reports
# ==========================================================
elif page == "Reports":

    st.info("Coming Soon")



# ==========================================================
# Settings
# ==========================================================
elif page == "Settings":

    st.header("⚙️ Veritix AI Studio Settings")

    st.subheader("🎤 Voice Engine")

    voice_engine = st.selectbox(
        "Choose Voice",
        [
            "gTTS",
            "Kokoro (Coming Soon)",
            "Piper (Coming Soon)"
        ]
    )

    st.subheader("🖼️ Image Engine")

    image_engine = st.selectbox(
        "Choose Image Source",
        [
            "Pexels",
            "Pixabay",
            "Unsplash",
            "AI Images (Coming Soon)"
        ]
    )

    st.subheader("🎬 Video")

    resolution = st.selectbox(
        "Resolution",
        [
            "1080x1920",
            "720x1280"
        ]
    )

    st.success("Settings saved for this session.")