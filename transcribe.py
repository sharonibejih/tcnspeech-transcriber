import torch
from transformers import AutoModelForCTC, Wav2Vec2Processor
import speech_recognition as sr
import io
from pydub import AudioSegment


processor = Wav2Vec2Processor.from_pretrained("sharonibejih/wav2vec2-large-xlsr-ng-en-sermon")
model = AutoModelForCTC.from_pretrained("sharonibejih/wav2vec2-large-xlsr-ng-en-sermon")

r = sr.Recognizer()

def transcribe():
    with sr.Microphone(sample_rate=16000) as source:
        print("You can start speaking now...")
        while True:
            audio = r.listen(source)  # pyaudio object
            # print("You said something now")
            data = io.BytesIO(audio.get_wav_data())
            # convert data to numpy array
            clip = AudioSegment.from_file(data)
            # convert clip tensor
            x = torch.FloatTensor(clip.get_array_of_samples())
            inputs = processor(x, sampling_rate=16000, 
            return_tensors="pt", padding=True).input_values

            logits = model(inputs).logits

            tokens = torch.argmax(logits, dim=-1)
            text = processor.batch_decode(tokens)
            return text
            # print("You said", str(text))
        