import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64

def html2pdf(url, target, param):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    # If there are parameter - Use a POST Request
    if param:
        # Render the HTML Template
        js = f'''var xhr = new XMLHttpRequest();
            xhr.open('POST', '{url}', false);
            xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

            xhr.send('data={json.dumps(param)}');
            return xhr.response;'''
        result = driver.execute_script(js)
        # Save Temporary result to Filesystem
        html_target = os.path.abspath(__file__) +  "~tmp.html"
        with open(html_target, 'w') as fd:
            fd.write(result)
        
        # Open local HtmlPage
        driver.get('file://'+ str(os.path.abspath(html_target)))

        # Clean Temporary result
        os.remove(html_target)

    # Default benavior - use a get request
    else:
        driver.get(url)

    file_name = write_pdf(driver, target)
    
    driver.quit()

    return file_name

def write_pdf(driver, target):
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

    with open(target, 'wb') as fd:
        fd.write(pdf)