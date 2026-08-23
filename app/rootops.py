#!/usr/bin/env python3

import paramiko

SERVERS = {
    "server 01": {
        "host": "192.168.85.129",
        "name": "rootops-server-01"
    },
    "server 02": {
        "host": "192.168.85.128",
        "name": "rootops-server-02"
    }
}

KEY_FILE = "/root/.ssh/id_ed25519"
USERNAME = "root"


def run_remote(host, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            hostname=host,
            username=USERNAME,
            key_filename=KEY_FILE,
            timeout=10
        )

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        return output, error

    finally:
        ssh.close()


def server_status(server):
    host = SERVERS[server]["host"]
    name = SERVERS[server]["name"]

    command = """
echo "HOSTNAME=$(hostname)"
echo "IP=$(hostname -I | awk '{print $1}')"
echo "UPTIME=$(uptime -p)"
echo "LOAD=$(awk '{print $1,$2,$3}' /proc/loadavg)"
echo "MEMORY:"
free -h
echo "DISK:"
df -h /
echo "PROCESSES:"
ps aux --sort=-%mem | head -6
"""

    output, error = run_remote(host, command)

    print()
    print("=" * 60)
    print(" ROOTOPS SERVER REPORT")
    print("=" * 60)
    print(f"Server : {name}")
    print(f"Address: {host}")
    print("=" * 60)
    print(output)

    if error:
        print("\nERROR:")
        print(error)


def main():

    print("=" * 60)
    print("        NewBornKernel RootOps AI")
    print("=" * 60)
    print("Available commands:")
    print("  check server 01")
    print("  check server 02")
    print("  exit")
    print()

    while True:

        query = input("AI> ").strip().lower()

        if query == "exit":
            print("RootOps stopped.")
            break

        if query == "check server 01":
            server_status("server 01")

        elif query == "check server 02":
            server_status("server 02")

        else:
            print("I do not understand that command yet.")


if __name__ == "__main__":
    main()
