import streamlit as st
import os
import time
import speech_recognition as sr
from transcribe import transcribe

os.system("sudo apt-get install portaudio19-dev python-pyaudio")
os.system("pip install pyaudio")

r = sr.Recognizer()

st.title("Sermon Transcription")

st.text("Click on the button below to turn on device mic")

start = st.button("Start speaking")

while start==True:
    text = transcribe()
    st.write(text)