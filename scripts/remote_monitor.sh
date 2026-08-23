#!/bin/bash

TARGET="root@192.168.85.128"

echo "================================="
echo " RootOps Remote Server Monitor"
echo " Target: rootops-server-02"
echo "================================="

echo
echo "=== HOSTNAME ==="
ssh -o BatchMode=yes "$TARGET" hostname

echo
echo "=== IP ADDRESS ==="
ssh -o BatchMode=yes "$TARGET" "ip -4 addr show ens33"

echo
echo "=== CPU / LOAD ==="
ssh -o BatchMode=yes "$TARGET" uptime

echo
echo "=== MEMORY ==="
ssh -o BatchMode=yes "$TARGET" free -h

echo
echo "=== DISK ==="
ssh -o BatchMode=yes "$TARGET" "df -h /"

echo
echo "=== RUNNING PROCESSES ==="
ssh -o BatchMode=yes "$TARGET" "ps aux --sort=-%mem | head"
