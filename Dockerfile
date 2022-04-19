FROM selenium/standalone-chrome:latest

#Install python3
RUN sudo apt-get update
RUN sudo apt-get install -y  python3
RUN sudo apt-get install -y python3-pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir --disable-pip-version-check -r requirements.txt
CMD ["python"]
