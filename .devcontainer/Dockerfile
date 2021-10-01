# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.194.3/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM python:3.8

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN dpkg -i google-chrome-stable_current_amd64.deb --fix-missing; apt-get -fy install

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver 

# Set display port as an environment variable
ENV DISPLAY=:99
ENV CHROME_USER_DATA_DIR /usr/out/chrome

ARG REQUIREMENTS=requirements.txt
COPY ${REQUIREMENTS} /tmp/
RUN pip install -r /tmp/${REQUIREMENTS}

EXPOSE 5001