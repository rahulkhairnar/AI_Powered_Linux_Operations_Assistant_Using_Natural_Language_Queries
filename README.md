# NewBornKernelRootOps

## Status
- Ubuntu 24.04.4 LTS
- Server 01: 192.168.85.129
- Server 02: 192.168.85.128
- Passwordless SSH: Working
- Paramiko: Working
- Remote monitoring: Working
- Natural-language CLI: Working
- Automated tests: Working

## Architecture
Server 01 acts as the RootOps controller and Server 02 acts as the managed Linux target.

## Supported Operations
- hostname
- IP address
- CPU/load
- memory
- disk
- running processes

## Documentation

- `docs/architecture.md` - System architecture
- `docs/final_architecture.md` - Final architecture description
- `docs/security.md` - Security design
- `docs/test_results.md` - Test matrix and verification results
- `docs/troubleshooting.md` - Troubleshooting guide
- `docs/demo_transcript.md` - Reproducible demonstration
- `docs/limitations.md` - Current limitations
- `docs/final_evidence.txt` - Final execution evidence
