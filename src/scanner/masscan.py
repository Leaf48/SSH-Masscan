import subprocess
import json


class Masscan:
    @staticmethod
    def scan(ipv4: str, ports: str, maxrate: str):
        command = [
            "masscan",
            "-oJ",
            "-",
            ipv4,
            "-p",
            ports,
            "--max-rate",
            maxrate,
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        try:
            scan_result = json.loads(result.stdout)
            print(scan_result)

            return scan_result
        except Exception as e:
            return []
