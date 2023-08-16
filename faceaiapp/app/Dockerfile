FROM ubuntu:18.04

# Refresh cache and install packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends git wget

# Install Python 3.8 instead of the default 3.6
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python3.8
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

## Install pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py



RUN apt-get update -y 
RUN apt-get install -y mysql-client
RUN apt-get install -y iputils-ping
RUN apt-get install -y vim 

COPY ./app /app
RUN cat /app/requirements.txt
 


RUN python3 -m pip install  -r /app/requirements.txt


RUN pip install Flask==2.3.2
RUN pip install Werkzeug==2.3.6
RUN pip install requests==2.31.0

WORKDIR /app
RUN chmod 777 *.py
ENTRYPOINT ["python3"] 
CMD ["/app/main.py"]
