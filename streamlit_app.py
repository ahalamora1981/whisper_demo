import streamlit as st
import whisper
import os


model = whisper.load_model("medium")

# Create a title and subtitle for the app
st.title("Audio Input Example")
st.markdown("Upload an audio file and click the submit button to display the output.")

# Create a file uploader for audio files
uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

# Create a submit button
if st.button("Submit"):
    # Check if an audio file was uploaded
    if uploaded_file is not None:
        # Save the uploaded file to a local folder
        folder_path = "audio_files"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the output message
        st.write("Audio file saved to local folder " + file_path)

        transcription = model.transcribe(file_path, initial_prompt="")
        st.write(transcription["text"])

    else:
        st.write("Please upload an audio file.")
