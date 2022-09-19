import streamlit as st
import os
import time
import speech_recognition as sr
from transcribe import transcribe

os.system("brew install portaudio")
os.system("pip install pyaudio")

r = sr.Recognizer()

st.markdown("Loading transcription model... Please wait")
st.title("Sermon Transcription")

st.text("Click on the button below to turn on device mic")

start = st.button("Start speaking")

while start==True:
    text = transcribe()
    st.write(text)
    # with sr.Microphone(sample_rate=16000) as source:
    #     st.write("You can start speaking now...")
    #     while True:
    #         audio = r.listen(source)  # pyaudio object
    #         st.write("You said something now")


# with st.form("user_form", clear_on_submit=True):
#     if __name__ == '__main__':
#         main()
        
    


## hide "Made with Streamlit" trademark
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>

#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.write('')
# st.write('')
# st.write('')

# st.markdown('TCN Community')