# Security Policy

## Supported Versions

We provide security updates for the following versions of the Springer Nature API Client:

| Version | Supported          |
| ------- | ------------------ |
| 0.0.2   | :white_check_mark: |
| < 0.0.2 | :x:                |

## Reporting a Vulnerability

We take the security of the Springer Nature API Client seriously. If you believe you've found a security vulnerability, please follow these steps:

1. **Do not disclose the vulnerability publicly**
2. Email us at supportapi@springernature.com with:
    - A description of the vulnerability
    - Steps to reproduce the issue
    - Potential impact of the vulnerability
    - Any suggested mitigation or fix (if available)

## Response Timeline

- We will acknowledge receipt of your report within 2 business days
- We aim to validate and respond to reports within 5 business days
- We will keep you informed as we work to address the vulnerability

## Disclosure Policy

- We follow responsible disclosure principles
- Once a fix is ready, we will coordinate with you on an appropriate disclosure timeline
- Security vulnerabilities will be noted in release notes once fixed

## Security Updates

- Security fixes are released as soon as possible after validation
- Updates will be published to PyPI following our standard release process
- Significant vulnerabilities will be detailed in release notes

## Best Practices for Users

- Keep your dependencies updated regularly
- Use pip or poetry to install from trusted sources
- Monitor the repository for security advisories
- Use environment variables for sensitive configuration (via python-dotenv)