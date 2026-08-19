import json
from datetime import datetime


def generate_report(result, output_file="reports/wifi_security_report.json"):
    report = {
        "report_metadata": {
            "generated_at": datetime.now().isoformat(),
            "report_type": "Wi-Fi Security Assessment",
            "tool": "Wi-Fi Security Assessment Tool",
        },
        "statistics": result["statistics"],
        "networks": result["networks"],
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_file
