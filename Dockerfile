# https://gist.github.com/source-nerd/e4037755b2e76f8d8346c01548930e95
# https://stackoverflow.com/questions/56135497/can-i-install-python-3-7-in-ubuntu-18-04-without-having-python-3-6-in-the-system
FROM python:3.8-slim-buster

# RUN apt-get update

# install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libasound-dev \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0

RUN pip install pyaudio

# RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
# RUN curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
# RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
# RUN git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew \
# && mkdir ~/.linuxbrew/bin \
# && ln -s ../Homebrew/bin/brew ~/.linuxbrew/bin \
# && eval $(~/.linuxbrew/bin/brew shellenv) \
# && brew install portaudio
EXPOSE 8501
WORKDIR /app
COPY requirements.txt app/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r app/requirements.txt


COPY . /app

# ENTRYPOINT ["streamlit" "run"]

# CMD ["python -m" "streamlit" "run" "app/app.py" "--server.port=8501" "--server.address=0.0.0.0"]

CMD streamlit run app/app.py