from collections import Counter

from analyzer.risk import assess_networks


def calculate_statistics(networks):
    total_networks = len(networks)

    security_types = Counter(
        network.get("security", "OPEN")
        for network in networks
    )

    risk_levels = Counter(
        network.get("risk", "UNKNOWN")
        for network in networks
    )

    channels = Counter(
        network.get("channel", 0)
        for network in networks
        if network.get("channel", 0) > 0
    )

    strong_networks = sum(
        1
        for network in networks
        if network.get("signal", 0) >= 70
    )

    weak_signal_networks = sum(
        1
        for network in networks
        if network.get("signal", 0) < 40
    )

    return {
        "total_networks": total_networks,
        "security_types": dict(security_types),
        "risk_levels": dict(risk_levels),
        "channels": dict(channels),
        "strong_networks": strong_networks,
        "weak_signal_networks": weak_signal_networks,
    }


def analyze_networks(networks):
    analyzed_networks = assess_networks(networks)
    statistics = calculate_statistics(analyzed_networks)

    return {
        "networks": analyzed_networks,
        "statistics": statistics
    }


if __name__ == "__main__":
    sample_networks = [
        {
            "ssid": "Office-WiFi",
            "bssid": "AA:BB:CC:DD:EE:01",
            "channel": 1,
            "signal": 85,
            "security": "WPA2"
        },
        {
            "ssid": "Guest-WiFi",
            "bssid": "AA:BB:CC:DD:EE:02",
            "channel": 6,
            "signal": 65,
            "security": "OPEN"
        },
        {
            "ssid": "Modern-WiFi",
            "bssid": "AA:BB:CC:DD:EE:03",
            "channel": 11,
            "signal": 75,
            "security": "WPA3"
        }
    ]

    result = analyze_networks(sample_networks)

    print("=== WI-FI SECURITY ASSESSMENT ===")
    print()

    stats = result["statistics"]

    print(f"Total Networks: {stats['total_networks']}")
    print(f"Strong Signal Networks: {stats['strong_networks']}")
    print(f"Weak Signal Networks: {stats['weak_signal_networks']}")
    print()

    print("Risk Levels:")
    for risk, count in stats["risk_levels"].items():
        print(f"  {risk}: {count}")

    print()

    print("Networks:")

    for network in result["networks"]:
        print(
            f"{network['ssid']} | "
            f"{network['security']} | "
            f"{network['risk']} | "
            f"Score: {network['risk_score']}"
        )
