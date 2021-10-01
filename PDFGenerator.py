import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64

TARGET_PATH=str(os.path.realpath('.')) + '/.pdf/'


  

def html2pdf(url, out=None):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("Title: %s" % driver.title)

    file_name = write_pdf(driver)
    
    driver.quit()

    return file_name

def write_pdf(driver, out="", filename=""):
    params = {  
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
	    'preferCSSPageSize': True,
    }
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': "Page.printToPDF", 'params': params})
    response = driver.command_executor._request('POST', url, body )
    if response.get('status'):
        raise Exception(response.get('value'))

    result = response.get('value')

    pdf = base64.b64decode(result['data'])

    file_name = filename if filename else driver.title + ".pdf"
    with open((TARGET_PATH if not out else out) + file_name, 'wb') as fd:
        fd.write(pdf)

    return file_name

if __name__ == '__main__':
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)

    html2pdf(out=f"{TARGET_PATH}/test.pdf", url="https://google.com")

    print(os.listdir(TARGET_PATH))
    print(os.listdir('/usr/out/chrome'))