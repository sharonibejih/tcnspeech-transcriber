import torch
from transformers import AutoModelForCTC, Wav2Vec2Processor
import speech_recognition as sr
import pyttsx3
import io
from pydub import AudioSegment
import streamlit as st

## load model and processor from the huggingface hub repository.
processor = Wav2Vec2Processor.from_pretrained("sharonibejih/wav2vec2-large-xlsr-ng-en-sermon")
model = AutoModelForCTC.from_pretrained("sharonibejih/wav2vec2-large-xlsr-ng-en-sermon")

# r = sr.Recognizer()

def transcribe():
    """
    Takes in speech from a microphone and processes it to return the spoken words.

    NOTE:
    This is an endless loop that only stops when the application is stopped.
    """
    st.write(sr.Microphone.list_microphone_names())
    # sr.Microphone(device_index=0)
    # print(
    #     f"MICs Found on this computer: \n {sr.Microphone.list_microphone_names()}")
    # Creating a recognition object
    # r = sr.Recognizer()
    # r.energy_threshold = 4000
    # r.dynamic_energy_threshold = False

    # with sr.Microphone(sample_rate=16000) as source:
    #     print("You can start speaking now...")
    #     while True:
    #         r.adjust_for_ambient_noise(source, 1)
    #         audio = r.listen(source)  # pyaudio object
    #         # print("You said something now")
    #         data = io.BytesIO(audio.get_wav_data())
    #         # convert data to numpy array
    #         clip = AudioSegment.from_file(data)
    #         # convert clip to tensor
    #         x = torch.FloatTensor(clip.get_array_of_samples())

    #         inputs = processor(x, sampling_rate=16000, 
    #         return_tensors="pt", padding=True).input_values

    #         logits = model(inputs).logits

    #         tokens = torch.argmax(logits, dim=-1)
    #         text = processor.batch_decode(tokens)
    #         # print("You said", str(text))
    #         return text
            
        
