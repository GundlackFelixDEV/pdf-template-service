from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import os
import subprocess

TARGET_PATH='./.pdf'

def getPDF(out, url):
    args = [
        "google-chrome", 
        "--headless", 
        "--disable-gpu",
        "--no-sandbox",
        f'--print-to-pdf={out}',
        url]
    subprocess.run(args)

if __name__ == '__main__':
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)

    getPDF(out=f"{TARGET_PATH}/test.pdf", url="https://google.com")

    print(os.listdir(TARGET_PATH))