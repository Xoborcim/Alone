# Alone
A game that I made in Grade 11 ICS,

You wake up in a dark forest with no recollection of who you are or how you got there. Explore around and hope to discover who are what put you there.

## Running

Requires Python 3.9+ and no third-party packages.

```bash
cd alone
python alone.py
```

## Building an executable

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd alone
pyinstaller alone.spec         # output goes to alone/dist/
```
