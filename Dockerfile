FROM rasa/rasa-sdk:2.8.2
COPY ./actions ./actions
USER root
RUN pip install --no-cache-dir -r ./actions/requirements2.txt
USER 1001