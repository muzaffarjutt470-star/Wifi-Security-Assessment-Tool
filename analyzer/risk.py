def assess_security(security):
    security = security.upper().strip()

    if security == "OPEN" or security == "":
        return {
            "risk": "HIGH",
            "score": 90,
            "reason": "Open Wi-Fi network without encryption"
        }

    if "WEP" in security:
        return {
            "risk": "HIGH",
            "score": 85,
            "reason": "WEP encryption is considered weak"
        }

    if "WPA1" in security and "WPA2" in security:
        return {
            "risk": "MEDIUM",
            "score": 55,
            "reason": "Legacy WPA1 compatibility is enabled"
        }

    if security == "WPA":
        return {
            "risk": "HIGH",
            "score": 75,
            "reason": "Legacy WPA security detected"
        }

    if "WPA3" in security:
        return {
            "risk": "LOW",
            "score": 15,
            "reason": "WPA3 provides modern wireless security"
        }

    if "WPA2" in security:
        return {
            "risk": "LOW",
            "score": 25,
            "reason": "WPA2 encryption detected"
        }

    return {
        "risk": "MEDIUM",
        "score": 50,
        "reason": "Unknown or unsupported security configuration"
    }


def assess_network(network):
    result = assess_security(network.get("security", ""))

    return {
        **network,
        "risk": result["risk"],
        "risk_score": result["score"],
        "risk_reason": result["reason"]
    }


def assess_networks(networks):
    return [assess_network(network) for network in networks]


if __name__ == "__main__":
    sample_networks = [
        {
            "ssid": "Test-Open",
            "security": "OPEN"
        },
        {
            "ssid": "Test-WPA2",
            "security": "WPA2"
        },
        {
            "ssid": "Test-WPA3",
            "security": "WPA3"
        },
        {
            "ssid": "Test-Legacy",
            "security": "WPA1 WPA2"
        }
    ]

    results = assess_networks(sample_networks)

    for network in results:
        print(
            f"{network['ssid']} | "
            f"{network['risk']} | "
            f"Score: {network['risk_score']} | "
            f"{network['risk_reason']}"
        )
