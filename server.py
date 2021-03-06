from flask import request, render_template, send_from_directory, Flask
from flask_cors import CORS
import logging
import argparse
import os, sys
import PDFGenerator
from TEST_DATA import TESTINPUT
import json
        

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './.pdf/'

@app.route('/pdf/<template>', methods=['GET', 'POST'])
@app.route('/pdf')
def send_pdf(template=""):
    filename = f"{TESTINPUT['title']}.pdf"
    PDFGenerator.html2pdf(url=f'http://localhost:5001/{template}', param=TESTINPUT if template else {}, target=app.config['UPLOAD_FOLDER']+filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/sammelrechnung', methods=['POST', 'GET'])
def sammelrechnung():
    """Sammel Rechnung."""
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        profile = data.get('profile')
        nf_form = data.get('nf_form')
        invoice = data.get('invoice')
        receits = data.get('receits')
        title = data.get('title')
    else:
        profile = TESTINPUT['profile']
        nf_form = TESTINPUT['nf_form']
        invoice = TESTINPUT['invoice']
        receits = TESTINPUT['receits']
        title=TESTINPUT['title']

    return render_template('sammelrechnung.j2',title=title, Profile=profile, NF_FORM=nf_form, Invoice=invoice, Receits=receits)

@app.route('/')
def home():
    """Landing page."""
    return render_template(
        'home.j2',
        title="Hello World",
        description="This is a Jinja2 Created description",
        items=[
            {"title": "A", "description": "Description A", "status": "info"},
            {"title": "B", "description": "Description B", "status": "warning"}
        ],
        table={
            'columns': ["A", "B", "C", "D"],
            'rows': [
                ["A1", "A2", "A3", "A4"],
                ["B1", "B2", "B3", "B4"],
                ["C1", "C2", "C3", "C4"],
                ["D1", "D2", "D3", "D4"]
            ]
        }
    )

if __name__ == '__main__':
    try:
        LOG = "./.log/session-service.log"
        # Setup Argument Parser
        parser = argparse.ArgumentParser(description='Argument Parser')
        parser.add_argument('--l', '--log', dest='LOGFILE', type=str, default=LOG,
                            help=f'path for logfile (default: {LOG})')
        parser.add_argument("--production", action='store_const',
                            help="set to production mode", const=True, default=False)

        args = parser.parse_args()
        # Check if production is set
        PRODUCTION = args.production
        os.environ['PRODUCTION'] = str(PRODUCTION)

        if not os.path.exists(os.path.abspath(os.path.dirname(args.LOGFILE))):
            os.makedirs(os.path.abspath(os.path.dirname(args.LOGFILE)))

        # Setup Logging
        logging.basicConfig(filename=args.LOGFILE, level=logging.INFO if PRODUCTION else logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s')
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        logging.info(f"Starting Server with [{args}]")

        # Start Server
        app.run(host="0.0.0.0", debug=False, port=5001)

    except Exception as e:
        logging.error(e)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)