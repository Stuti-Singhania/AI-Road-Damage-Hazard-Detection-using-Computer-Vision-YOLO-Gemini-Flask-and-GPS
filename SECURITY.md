# Security Policy

## Reporting a vulnerability

Please do not publish API keys, credentials or exploitable security details in a public issue.

For a sensitive vulnerability, contact the repository owner privately through GitHub. Include the affected component, reproduction steps, potential impact and any suggested mitigation.

## Secrets

Never commit:

- Google/Gemini API keys
- Roboflow API keys
- passwords or tokens
- private user data
- captured images containing sensitive information

Use local environment variables or a secret manager instead.
