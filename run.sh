#!/bin/bash
cd /home/ec2-user/rasa/git/chatbot_rasa
docker-compose build
docker-compose up -d