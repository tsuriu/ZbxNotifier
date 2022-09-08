from crypt import methods
from flask import Blueprint, render_template, request, send_file
from flask import current_app as app
from flask_qrcode import QRcode

#from flask_blueprint_tutorial.api import fetch_products

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)

qrcode = QRcode(app)

@home_bp.route("/qr", methods=["GET"])
def home():
    return render_template('index.html')

@home_bp.route("/qrcode", methods=["GET"])
def get_qrcode():
    qr_data = "2@Fm89duT1toMkUrxdp8Q0ceHIa3S37WgtXmpWp+35e9qnszRIPTa9K9yogdjyym9vNFba72rSN4r6Bg==,xNlsUA2QCq3MWYB3Sw/El4AM/Iza4CN1te/bpaVyLwo=,e6UMoWEEh2yZV4BgakSgc6bWndBkFr1yyaOQ50fjEQg=,ZH1jIFhoG0OewG5JV9xObK7mQGi512K1ribdnruqB7Q="
    return send_file(qrcode(qr_data, mode="raw", box_size=20), mimetype="image/png")

@home_bp.route("/status", methods=["GET"])
def get_status():
    pass