docker-build:
	docker build -t streamlit-wav2vec2 .
docker-run:
	docker run -p 8501:8501 streamlit-wav2vec2