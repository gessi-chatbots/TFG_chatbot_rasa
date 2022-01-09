#!/bin/bash
cd /home/ec2-user/rasa/git/TFG_chatbot_rasa
docker-compose build
docker-compose up -d
docker exec -it tfg_chatbot_rasa-postgres-1 psql -U project_admin -d rasa -f scripts/queries.sql