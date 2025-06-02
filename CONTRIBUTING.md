# Contributing to Springer Nature API Client

Thank you for considering contributing to the Springer Nature API Client. This document outlines the process for contributing to this project.

## Code of Conduct

By participating in this project, you agree to uphold our Code of Conduct. Please report unacceptable behavior to supportapi@springernature.com.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Development Environment Setup

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/springernature_api_client.git
   cd springernature_api_client
   ```
2. Install dependencies with Poetry
   ```bash
   poetry install --with dev
    ```
3. Activate the virtual environment
    ```bash
   poetry shell
    ```
## Development Workflow

### Coding Standards
- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines
- Use meaningful variable and function names
- Include docstrings for all functions, classes, and modules
- Add type hints where appropriate

### Testing
- Write tests for all new features using pytest
- Run tests before submitting any changes
    ```bash 
    pytest
    ```
- Maintain or improve test coverage

### Pull Request Process
1. Fork the repository
2. Create a feature branch (```git checkout -b feature/amazing-feature```)
3. Commit your changes (```git commit -m 'Add some amazing feature'```)
4. Push to the branch (```git push origin feature/amazing-feature```)
5. Open a Pull Request

### Commit Messages
Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- feat: for new features
- fix: for bug fixes
- docs: for documentation changes
- test: for adding or modifying tests
- refactor: for code refactoring

### Reporting Bugs
Report bugs by opening an issue using the bug report template. 
Include:
- A clear description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots if applicable
- Environment details (OS, Python version, etc.)

### Feature Requests
Submit feature requests by opening an issue using the feature request template.

### Documentation
- Update documentation with any changes to APIs or behavior
- Use clear and concise language
- Include examples where appropriate

### Versioning
We follow [Semantic Versioning](https://semver.org/). Version numbers are in the format MAJOR.MINOR.PATCH.

### License
By contributing to this project, you agree that your contributions will be licensed under the project's MIT license.
