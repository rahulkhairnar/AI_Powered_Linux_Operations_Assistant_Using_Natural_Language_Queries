# RootOps Architecture

## Server 01
IP: 192.168.85.129
Role: AI Controller

## Server 02
IP: 192.168.85.128
Role: Managed Linux Target

## Communication
Server 01 communicates with Server 02 using passwordless SSH and Paramiko.

## Monitoring
- Hostname
- IP address
- CPU/load
- Memory
- Disk
- Processes

## Application
Python-based RootOps assistant provides natural-language command selection and remote Linux monitoring.
