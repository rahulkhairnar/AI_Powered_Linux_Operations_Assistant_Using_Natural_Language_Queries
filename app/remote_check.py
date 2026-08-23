import os
import paramiko

HOST = "192.168.85.128"
USERNAME = "rahul"

password = os.environ.get("REMOTE_PASS")
if not password:
    raise SystemExit("Set REMOTE_PASS env var first, e.g.: export REMOTE_PASS='your_password'")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(HOST, username=USERNAME, password=password, timeout=15)

    cmd = r"""
    echo "rootops-server-02"
    echo "---- UPTIME ----"
    uptime -p 2>/dev/null || uptime

    echo "---- MEMORY ----"
    free -h

    echo "---- DISK ----"
    df -hT | awk 'NR==1 || $1 ~ /^\/dev\// {print}'
    """

    stdin, stdout, stderr = ssh.exec_command(cmd)

    out = stdout.read().decode(errors="ignore")
    err = stderr.read().decode(errors="ignore").strip()

    print("\n=== Remote Server Monitoring ===\n")
    print(out)

    if err:
        print("\n=== STDERR ===\n")
        print(err)

finally:
    ssh.close()
