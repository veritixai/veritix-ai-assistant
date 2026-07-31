from gtts import gTTS
import os


def text_to_speech(text, filename="audio/output.mp3"):

    os.makedirs("audio", exist_ok=True)

    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    tts.save(filename)

    return filename