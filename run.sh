#!/bin/bash
cd /home/ec2-user/rasa/git/TFG_chatbot_rasa
docker-compose down
docker-compose build
docker-compose up -d