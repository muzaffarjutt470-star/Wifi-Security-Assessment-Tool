# Wi-Fi Security Assessment Tool

A Python-based Wi-Fi security assessment tool designed for authorized wireless security analysis. The tool discovers nearby wireless networks, analyzes their security configuration, evaluates signal strength, calculates risk scores, generates security reports, and presents results through a professional Flask dashboard.

## Features

- Wireless network discovery
- SSID identification
- BSSID identification
- Wi-Fi channel detection
- Signal strength analysis
- Wireless security detection
- WPA2 detection
- WPA3 detection
- Legacy WPA1 detection
- Open network detection
- Automated risk scoring
- LOW, MEDIUM, and HIGH risk classification
- Network statistics
- JSON security report generation
- Flask web dashboard
- Professional network assessment table
- Responsive dashboard interface

## Project Structure

wifi-security-assessment-tool/

├── analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── report.py
│   ├── risk.py
│   └── scanner.py
│
├── reports/
│   └── .gitkeep
│
├── static/
│   └── css/
│
├── templates/
│   └── dashboard.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

## Technologies Used

- Python 3
- Flask
- NetworkManager
- nmcli
- Linux Wireless Networking
- Jinja2
- HTML5
- CSS3
- JSON

## How It Works

The tool follows a simple security assessment workflow:

1. Discover nearby wireless networks.
2. Collect SSID, BSSID, channel, signal strength, and security information.
3. Analyze the detected security configuration.
4. Calculate a risk score.
5. Assign a risk level.
6. Generate assessment statistics.
7. Create a JSON security report.
8. Display the results through the Flask dashboard.

## Risk Assessment

The assessment engine evaluates networks according to their detected wireless security configuration.

| Security Type | Risk Level | Score | Assessment |
|---|---|---:|---|
| Open | HIGH | 90 | Wireless network without encryption |
| WPA1 + WPA2 | MEDIUM | 55 | Legacy WPA1 compatibility enabled |
| WPA2 | LOW | 25 | WPA2 encryption detected |
| WPA3 | LOW | 15 | Modern wireless security detected |

## Scanner

The scanner collects information such as:

- SSID
- BSSID
- Security type
- Signal strength
- Channel

Example assessment data:

SSID: WirelessNet
BSSID: 18:C5:8A:2A:65:48
Security: WPA1 WPA2
Signal: 89%
Channel: 1

## Risk Engine

The risk engine evaluates each detected network and produces:

- Risk level
- Risk score
- Security reason

Example:

WirelessNet | WPA1 WPA2 | MEDIUM | Score: 55

CHADHAR | WPA2 | LOW | Score: 25

## JSON Security Reports

The tool can generate structured JSON reports containing:

- Report metadata
- Total networks
- Security types
- Risk levels
- Channel statistics
- Signal statistics
- Network assessment results
- Risk reasons

Example report structure:

{
    "report_metadata": {},
    "statistics": {},
    "networks": []
}

Generated reports containing live scan information should normally remain outside version control.

## Flask Dashboard

The project includes a Flask-based security dashboard.

The dashboard displays:

- Total Networks
- Strong Signal Networks
- Weak Signal Networks
- LOW Risk Networks
- MEDIUM Risk Networks
- HIGH Risk Networks
- Risk Assessment
- Detected Networks
- SSID
- BSSID
- Security
- Signal
- Channel
- Risk
- Risk Score
- Risk Reason

## Installation

Clone the repository:

git clone https://github.com/mushtaqmuzaffar875-a11y/Wi-Fi-Security-Assessment-Tool.git

Enter the project directory:

cd Wi-Fi-Security-Assessment-Tool

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Running the Scanner

Run the wireless scanner:

python -m analyzer.scanner

Run the security assessment:

python -m analyzer.analyzer

Generate a security report:

python -m analyzer.report

## Running the Dashboard

Start the Flask application:

python app.py

Open the dashboard in your browser:

http://127.0.0.1:5000

## Requirements

The project requires:

- Linux operating system
- Python 3
- NetworkManager
- nmcli
- Compatible wireless interface
- Flask
- Permission to perform wireless network discovery

## Security and Responsible Use

This project is intended for:

- Cybersecurity education
- Defensive security research
- Authorized wireless security assessment
- Laboratory environments
- Networks owned by the user
- Networks for which explicit permission has been granted

Only assess wireless networks when you have authorization to do so.

## What This Tool Does Not Do

This project is focused on security assessment and does not perform:

- Wi-Fi password cracking
- Authentication bypass
- Deauthentication attacks
- Handshake cracking
- Unauthorized network access
- Exploitation of wireless access points
- Credential theft
- Network disruption

## Limitations

The assessment is based on wireless information that is discoverable by the system.

A LOW risk classification does not guarantee that a wireless network is completely secure.

The tool provides a configuration-focused assessment rather than a complete penetration test.

## Example Results

A typical assessment may produce results such as:

Total Networks: 8

LOW Risk: 5

MEDIUM Risk: 3

HIGH Risk: 0

Example:

CHADHAR | WPA2 | LOW | Score: 25

WirelessNet | WPA1 WPA2 | MEDIUM | Score: 55

Redmi Note 13 | WPA2 | LOW | Score: 25

## Author

MUZAFFAR MUSHTAQ

CS Student • Cybersecurity Enthusiast

## License

This project is developed for educational, defensive security research, and authorized security assessment purposes.
