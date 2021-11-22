FROM ubuntu:18.04
ENTRYPOINT []
COPY . /app/
RUN apt-get clean && apt-get update -qq && apt-get install -y python3.6 python3-pip && rm -rf /var/lib/apt/lists/* && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache -r /app/requirements.txt
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh