cd ./app
rasa train
rasa run --enable-api --cors "*" &
rasa run actions &