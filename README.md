# mining-watchdog

> watchdog · restart · share

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Mining watchdog shell — bench + submit, no live pool.

## Features

- Default algorithm randomx
- Role: watchdog
- Stratum job queue with stub notify/submit
- CPU backend with SHA-256 work loop
- Watchdog-style controller and share counter

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd mining-watchdog
python -m pip install -e .
python -m minewd --help
```

## CLI Usage

```bash
minewd bench --rounds 32
# Hash a stub job locally

minewd status
# Print controller snapshot

minewd submit --nonce 1
# Record a stub share
```

## Project Structure

```
minewd/
  stratum/     client + job queue
  algo/        hasher
  device/      CPU backend
  core/        controller
  cli.py
tests/
```

## Configuration

See `minewd/config.py`.

| Setting | Default | Description |
|---------|---------|-------------|
| `algo` | `randomx` | Hash algorithm id |
| `threads` | `2` | Worker count |
| `pool` | `stratum+tcp://localhost:3333` | Stub pool URL |

## Tests

```bash
python -m pytest -q
```

## Background

Watchdog scripts use this filename on farm boxes.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![mining](https://img.shields.io/badge/mining-111827?style=flat-square) ![watchdog](https://img.shields.io/badge/watchdog-111827?style=flat-square) ![mining-watchdog](https://img.shields.io/badge/mining%20watchdog-111827?style=flat-square) ![miner](https://img.shields.io/badge/miner-111827?style=flat-square) ![cryptominer](https://img.shields.io/badge/cryptominer-111827?style=flat-square) ![stratum](https://img.shields.io/badge/stratum-111827?style=flat-square) ![hashrate](https://img.shields.io/badge/hashrate-111827?style=flat-square) ![mining-pool](https://img.shields.io/badge/mining%20pool-111827?style=flat-square)

`mining` `watchdog` `mining-watchdog` `miner` `cryptominer` `stratum` `hashrate` `mining-pool` `open-source` `python`

Search: mining-watchdog · watchdog · restart · share · Mining watchdog shell — bench + submit, no live pool.

---

<sub>Mining watchdog shell — bench + submit, no live pool.</sub>
