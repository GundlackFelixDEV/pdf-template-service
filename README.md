
# Requirements
* Python 3.8
* Google Chrome
* Chromedriver

# Setup
## A - VSCode + Remote Container

1. Follow the [Install](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) instructions to Setup *VSCode* with *Remote Container*
2. Open projectfolder in container
3. Execute server.py

## B - Manual - Linux
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
apt-get -y update

# Magic happens
apt-get install -y google-chrome-stable

# Installing Unzip
apt-get install -yqq unzip

# Download the Chrome Driver
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
DISPLAY=:99

pip install -r ./requirements.txt

```
