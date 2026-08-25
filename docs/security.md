# Security Design

## Authentication

RootOps uses SSH key-based authentication for automated server communication.

## Passwordless Automation

BatchMode SSH is used for automated operations so that scripts do not require interactive password entry.

## Key Protection

Private SSH keys must remain outside the source repository and must never be committed to Git.

## Repository Protection

The project excludes:

- SSH private keys
- `.env` files
- Python virtual environments
- Python cache files
- application log files containing sensitive information

## Command Control

The current prototype uses controlled command mappings rather than arbitrary unrestricted command generation.

## Security Improvements

Future versions should add:

- non-root service accounts
- least-privilege sudo rules
- command allowlisting
- audit logging
- role-based access control
- secrets management
