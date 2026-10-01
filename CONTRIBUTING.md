# Contributing to CivicScan

Thanks for helping improve CivicScan.

## Quick start

1. Fork the repository.
2. Create a focused branch for your change.
3. Copy `.env.example` to `.env` and add your own local credentials if needed.
4. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
5. Run the test suite:
   ```bash
   pytest -q
   ```
6. Open a pull request with a clear description and testing notes.

## Good first contributions

Issues labeled **good first issue** are intended to be approachable entry points. Documentation, tests, UI improvements and reproducible benchmarks are also welcome.

## Pull request expectations

- Keep changes focused.
- Never commit API keys, private data or generated uploads.
- Add or update tests for behavior you change.
- Explain any new environment variables.
- Include screenshots for meaningful UI changes.

## Development principles

CivicScan is a prototype civic-computer-vision system. Prefer small, testable modules and explicit error handling over hidden magic.
