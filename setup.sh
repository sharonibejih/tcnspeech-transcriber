#!/bin/sh
# install portaudio, a requirement for pyaudio, which is a requirement for SpeechRecognition
brew install portaudio # for linux use this: sudo apt-get install portaudio19-dev python-pyaudio
pip install -r requirements.txt