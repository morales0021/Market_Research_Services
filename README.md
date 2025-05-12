# 📊 Market Research Service

**Market Research Service** is a lightweight microservice designed to generate structured market report subsections using the OpenAI API. It returns formatted JSON outputs describing specific segments of a market report, making it ideal for integration into automated research workflows or SaaS platforms. It also provides the specific json outputs for generating a set of charts. Everything is generated dynamically using prompt engineering and prompt chains.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- OpenAI API key

> ⚠️ **Note:** This is a draft version. The API key must be manually inserted into `mrservices/main.py`.

---

### 🛠️ Installation & Running the Service

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the microservice:
   ```bash
   uvicorn main:app --host <your_ip_here> --port <your_port> --reload
   ```

---

## 🧠 Functionality

This microservice leverages OpenAI to generate well-structured content for specific sections of a market report. The results are returned in a consistent, schema-validated JSON format.

---

## 📁 Project Structure

```
.
├── mrservices/
│   └── completions/             # Api functions to call OpenAI api
│   └── formats/                 # Pydantic classes defining output format
│   └── pipelines/               # Contains the pipeline for the chains of prompts 
│   └── prompts/                 # The prompts used to generate the subsections and the charts
│   └── react/                   # Some auxiliary functions to format the json output to another compatible chart library used in react.
│   └── main.py                 # Core service logic (contains OpenAI key)
├── tests/
│   └── jupyter_notebooks/      # Usage examples and test cases
```

---

## 🧪 Examples

To explore how the microservice works and what kind of data it returns, check out the example notebooks inside:

```
tests/jupyter_notebooks/
```

These examples show different types of report section generations and how to call the service programmatically.

---

## 📦 Output Format

The service uses Pydantic models located in `mrservices/formats` to ensure the OpenAI output adheres to a defined schema. This ensures reliable and clean integration into downstream applications.

---

## 🧩 TODO

- Move API key to secure environment configuration
- Add authentication for production use
- Expand predefined section types
- Add error handling and validation improvements

---

## 📬 Contact

For questions, suggestions, or collaborations, feel free to open an issue or contact the maintainer.
