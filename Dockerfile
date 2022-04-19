FROM selenium/standalone-chrome:latest

#Install python
RUN sudo apt-get update
RUN sudo apt-get install -y  python
RUN sudo apt-get install -y python3-pip

COPY requirements.txt .
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

RUN sudo -H pip install -U pipenv
CMD ["python"]
