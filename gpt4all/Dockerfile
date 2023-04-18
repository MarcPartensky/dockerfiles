FROM python:alpine

RUN apk update
# RUN apk add aria2
# RUN curl -L -w "%{url_effective}\n" -o url.txt -s "https://tinyurl.com/gpt4all-lora-quantized"
# RUN cat url.txt

# RUN curl -L -w "%{url_effective}\n" -o /dev/null -s "https://tinyurl.com/gpt4all-lora-quantized"
RUN wget https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin
# RUN transmission-cli $(cat url.txt)
# RUN aria2c https://tinyurl.com/gpt4all-lora-quantized -m 5
 # RUN transmission-cli "magnet:?xt=urn:btih:1F11A9691EE06C18F0040E359361DCA0479BCB5A&dn=gpt4all-lora-quantized.bin&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce"
# RUN stig download https://tinyurl.com/gpt4all-lora-quantized
RUN pip install nomic
COPY main.py main.py

ENTRYPOINT ["python", "main.py"]
