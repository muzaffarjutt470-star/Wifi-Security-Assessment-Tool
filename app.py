from flask import Flask, render_template
from analyzer.scanner import scan_wifi_networks
from analyzer.analyzer import analyze_networks


app = Flask(__name__)


@app.route("/")
def dashboard():
    networks = scan_wifi_networks()
    result = analyze_networks(networks)

    return render_template(
        "dashboard.html",
        statistics=result["statistics"],
        networks=result["networks"]
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
