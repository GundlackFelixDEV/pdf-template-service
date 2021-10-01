from TEST_DATA import TESTINPUT
from PDFGenerator import html2pdf
import subprocess
import time
if __name__ == '__main__':

    p = subprocess.Popen(['python3', 'server.py'])

    time.sleep(1)

    url='http://localhost:5001/sammelrechnung'
    param=TESTINPUT 
    target = './.pdf/PDFGenerator_Sammelrechnung.pdf'
    html2pdf(url=url, param=param, target=target)

    p.terminate()