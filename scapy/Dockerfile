FROM python:3.10-slim

RUN apt-get update && apt-get install -y tcpdump iproute2 iputils-ping net-tools

RUN pip install --no-cache-dir scapy

CMD ["/bin/bash"]
