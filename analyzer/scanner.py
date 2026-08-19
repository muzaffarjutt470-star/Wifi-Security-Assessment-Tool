import json
import platform
import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            check=False
        )

        if result.returncode != 0:
            return ""

        return result.stdout.strip()

    except (subprocess.SubprocessError, OSError):
        return ""


def get_wifi_interface():
    if platform.system().lower() != "linux":
        return None

    output = run_command(["iw", "dev"])

    for line in output.splitlines():
        line = line.strip()

        if line.startswith("Interface "):
            return line.split(" ", 1)[1]

    return None


def split_nmcli_line(line):
    fields = []
    current = []
    escaped = False

    for char in line:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == ":":
            fields.append("".join(current))
            current = []
        else:
            current.append(char)

    if escaped:
        current.append("\\")

    fields.append("".join(current))

    return fields


def clean_value(value):
    return value.strip()


def scan_wifi_networks():
    interface = get_wifi_interface()

    if not interface:
        return []

    output = run_command([
        "nmcli",
        "-t",
        "-f",
        "SSID,BSSID,CHAN,SIGNAL,SECURITY",
        "device",
        "wifi",
        "list",
        "ifname",
        interface
    ])

    networks = []

    for line in output.splitlines():
        if not line.strip():
            continue

        parts = split_nmcli_line(line)

        if len(parts) < 5:
            continue

        ssid = clean_value(parts[0])
        bssid = clean_value(parts[1])
        channel = clean_value(parts[2])
        signal = clean_value(parts[3])
        security = ":".join(parts[4:]).strip()

        try:
            channel_value = int(channel)
        except ValueError:
            channel_value = 0

        try:
            signal_value = int(signal.replace("%", ""))
        except ValueError:
            signal_value = 0

        networks.append({
            "ssid": ssid or "<Hidden>",
            "bssid": bssid,
            "channel": channel_value,
            "signal": signal_value,
            "security": security or "OPEN"
        })

    return networks


def save_scan_results(networks, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(networks, file, indent=4)


if __name__ == "__main__":
    networks = scan_wifi_networks()

    print(f"Networks detected: {len(networks)}")
    print()

    for network in networks:
        print(
            f"SSID: {network['ssid']} | "
            f"BSSID: {network['bssid']} | "
            f"Security: {network['security']} | "
            f"Signal: {network['signal']}% | "
            f"Channel: {network['channel']}"
        )
