
# eMudhra CA Private Key Compromise — Security Analysis

An educational cybersecurity investigation into the October 2026 eMudhra Certificate Authority incident.

## Overview

This project examines how a key-generation failure resulted in eight weak intermediate CA private keys using P-384 elliptic-curve cryptography.

It explores the incident, the underlying cryptographic concepts, its potential security implications, and the importance of secure key generation.

## Project Structure

```text
emudhra-ca-analysis/
├── demo/
│   └── weak_key_recovery.py
├── research/
│   └── incident-analysis.md
├── screenshots/
└── README.md
```

## Practical Demonstration

The Python demonstration simulates recovery of deliberately weak P-384 private scalars by searching a small candidate range.

It uses synthetic cryptographic keys and does not access or attack real CA infrastructure.

### Requirements

- Python 3
- cryptography

### Installation

```bash
python -m pip install cryptography
```

### Execution

```bash
python demo/weak_key_recovery.py
```

## Key Concepts Explored

- Public-key cryptography
- Elliptic Curve Cryptography (ECC)
- P-384
- Certificate Authorities
- Intermediate CA certificates
- Private-key security
- Cryptographic randomness
- Certificate revocation

## Key Finding

The incident did not demonstrate a break in P-384 cryptography. It demonstrated how weak private-key generation can undermine otherwise strong cryptographic systems.

## Disclaimer

This project is intended strictly for educational and cybersecurity awareness purposes. All practical demonstrations use synthetic keys.

## References

- [eMudhra Official Statement](https://emudhra.com/en/press-release/emudhra-statement-distrust-global-tls-intermediate-root-ca)
- [CERT-In Advisory](https://www.cert-in.org.in/s2cMainServlet?CACODE=CICA-2026-3649&pageid=PUBADV01)
- [Google Security Response](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)
- [Kudelski Security Research](https://kudelskisecurity.com/research/emudhra-intermediate-ca-private-key-compromise)

---

**Prepared for OpenCode Cybersecurity**
