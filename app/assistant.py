import subprocess

COMMANDS = {
    "show disk usage": "df -h",
    "show memory usage": "free -h",
    "show cpu load": "uptime",
    "show ip address": "ip -4 addr show ens33",
    "show hostname": "hostnamectl",
    "show running processes": "ps aux --sort=-%mem | head"
}

print("=== NewBornKernelRootOps ===")
print("Type a natural language query")
print("Type 'exit' to quit\n")

while True:
    query = input("AI> ").strip().lower()

    if query == "exit":
        break

    command = COMMANDS.get(query)

    if command:
        print(f"\nExecuting: {command}\n")
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(result.stdout)
    else:
        print("Sorry, I do not understand that query yet.\n")
