---
inclusion: always
---

# Python Usage for This Demo App

**CRITICAL**: Python 3 with the project `.venv` (auto-activated in terminals).

## Python Version Support

- **Python**: 3.8+ (tested with 3.8–3.12)

## Environment

- **Virtual environment**: `.venv/` in the repo root (already activated for you)
- **App dependencies**: `requirements.txt` (Kivy, Mistune, pytest, hypothesis)
- **Garden widget**: install editable copy from `external/markdownlabel` to match the demo

## Commands (PATH already points at `.venv/bin`)

- Install deps: `pip install -r requirements.txt`
- Install garden widget: `pip install -e external/markdownlabel`
- Run app: `python3 main.py`
- Run all tests: `pytest tests/`
- Run single test: `pytest tests/test_content.py`

## Notes

- This repo is a runnable demo, not a packaged distribution; no build/publish steps.
- Window sizing helpers live at `window_size_probe.py` / `window_size_viewer.py` if you need to tweak them.
