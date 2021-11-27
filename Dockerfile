FROM rasa/rasa:2.8.12
COPY . .
USER root
RUN pip install --no-cache-dir -r requirements.txt
USER 1001