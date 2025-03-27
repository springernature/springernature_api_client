# SpringerNature API Client

[![PyPI Version](https://img.shields.io/pypi/v/springernature_api_client)](https://pypi.org/project/springernature-api-client/)
[![Python Version](https://img.shields.io/pypi/pyversions/springernature_api_client)](https://pypi.org/project/springernature-api-client/)
[![License](https://img.shields.io/pypi/l/springernature_api_client)](LICENSE)

A Python package to interact with the **SpringerNature API** for fetching metadata, open access articles, and text & data mining (TDM) content.

---

## 🚀 Installation

### Install Python

Ensure you have Python installed (version 3.7+ recommended).

Windows: Download from [python.org](https://www.python.org/downloads/) and install.

macOS: Install via Homebrew:

```bash
brew install python
```

Linux: Install using package manager (e.g., apt for Debian/Ubuntu):

```bash
sudo apt update && sudo apt install python3 python3-venv python3-pip
```

### Create a Virtual Environment (Recommended)

It's best to install the package inside a virtual environment to avoid conflicts.

```bash
# Create a virtual environment (venv)
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### Install the Package

```bash
pip install springernature_api_client
```

## 🔑 Setup

Before using the package, obtain an API key from SpringerNature Developer Portal.

Set the API key in your environment:

```bash
export SPRINGER_API_KEY="your_api_key_here"
```

Or pass it directly in Python:

```bash
api_key = "your_api_key_here"
```

## 📌 Basic Usage

Fetch Metadata and Export to Excel

```bash
import springernature_api_client.metadata as metadata
from springernature_api_client.utils import results_to_dataframe

# Initialize API Client
metadata_client = metadata.MetadataAPI(api_key="your_api_key")

# Fetch results (pagination enabled, stops at `s=200`)
response = metadata_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)

# Convert API response to DataFrame & export to Excel
df = results_to_dataframe(response, export_to_excel=True, filename="articles.xlsx")

print(df.head())  # Display first few rows
```

## 📚 API Modules

### 1️⃣ Meta API

```bash
import springernature_api_client.meta as meta
from springernature_api_client.utils import results_to_dataframe

meta_client = meta.MetaAPI(api_key="your_api_key")
response = meta_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)
df = results_to_dataframe(response, export_to_excel=True)
print(df.head())
```

### 2️⃣ Metadata API

```bash
import springernature_api_client.metadata as metadata
from springernature_api_client.utils import results_to_dataframe

metadata_client = metadata.MetadataAPI(api_key="your_api_key")
response = metadata_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)
df = results_to_dataframe(response, export_to_excel=True)
print(df.head())
```

### 3️⃣ Open Access API

```bash
import springernature_api_client.openaccess as openaccess
from springernature_api_client.utils import results_to_dataframe

openaccess_client = openaccess.OpenAccessAPI(api_key="your_api_key")
response = openaccess_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)
df = results_to_dataframe(response, export_to_excel=True)
print(df.head())
```

### 4️⃣ TDM (Text & Data Mining) API

```bash
import springernature_api_client.tdm as tdm
from springernature_api_client.utils import results_to_dataframe

tdm_client = tdm.TDMAPI(api_key="your_api_key")
response = tdm_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)
df = results_to_dataframe(response, export_to_excel=True)
print(df.head())
```

### 🔄 Pagination Handling (fetch_all=True)

If fetch_all=True, the API will automatically paginate through results.

```bash
response = metadata_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)
```

## 📤 Exporting to Excel

By default, results_to_dataframe() saves the results as an Excel file:

```bash
df = results_to_dataframe(response, export_to_excel=True, filename="output.xlsx")
```

## 🛠 Troubleshooting

### 1️⃣ Invalid API Key

Ensure you pass the correct API key.
Try setting the API key as an environment variable.

### 2️⃣ Rate Limit Exceeded (Error 429)

SpringerNature API limits requests per minute.
If you hit the limit, wait or request a higher quota.

### 3️⃣ Connection Timeout

If requests timeout, check your internet connection.
Try increasing the timeout value in the request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Contributing

We welcome contributions! Open an issue or submit a pull request. 🚀
