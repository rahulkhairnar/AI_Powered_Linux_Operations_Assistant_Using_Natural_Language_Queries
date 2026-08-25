# Security Design

- SSH key-based authentication is used for automated communication.
- BatchMode SSH prevents interactive password prompts during automation.
- Private SSH keys must never be committed to Git.
- `.env`, virtual environments, cache files and sensitive logs are excluded.
- The current prototype uses controlled command mappings rather than unrestricted command generation.
- Future work includes least-privilege accounts, command allowlisting, audit logging, RBAC and secrets management.
