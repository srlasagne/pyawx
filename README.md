# 🤖 PyAWX

Python client for managing AWX automation platform.

**📌 Table of Contents**

- [✨ Features](#-features)
- [📚 Documentation](#-documentation)
- [📦 Installation](#-installation)
- [📖 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [🧪 Testing](#-testing)
- [🛠️ Roadmap](#-roadmap)

## ✨ Features

- **Authentication support**: Built-in support for Basic Auth and OAuth2.
- **Data validation**: Pydantic models ensure that payloads conform to the AWX
  API's expected structure.
- **Extensibility**: Easily extendable to support new AWX resources or custom
  workflows.

## 📚 Documentation

Each module is documented in detail and can be explored using
[pdoc](https://pdoc.dev). Below is an overview of the key modules:

- `pyawx.auth`: Authentication classes for Basic Auth and OAuth2.
- `pyawx.http`: HTTP client abstraction for handling API requests.
- `pyawx.models`: Pydantic models for data validation and serialization.
- `pyawx.resources`: Resource classes for interacting with AWX resources.
- `pyawx.client`: Client interface for interacting with the AWX API.

## 📦 Installation

### 📥 Pip

Install the `pyawx` package using `pip`:

```bash
pip install pyawx
```

### 📥 UV

Install the `pyawx` package using `uv`:

```bash
uv add pyawx
```

## 📖 Usage

### 🔒 Authentication

To interact with the AWX API, you need to authenticate using either Basic
Authentication or OAuth2. Here's how to set up both methods:

#### 🔑 Basic Authentication

```python
from pyawxapi.client import Client

# Initialize the client with Basic Authentication
client = Client(
    "https://api.example.com",
    username="your_username",
    password="your_password",
)

# Fetch a job template by name
job_template = client.job_template.fetch("My Job Template")
```

#### 🔑 OAuth2 Authentication

```python
from pyawxapi.client import Client

# Initialize the client with OAuth2 Authentication
client = Client("https://api.example.com", token="your_oauth2_token")

# Fetch a workflow job template by name
workflow_job_template = client.workflow_job_template.fetch("My Workflow Job Template")
```

### 🔄 Working with Resources

The library provides resource-specific classes to interact with different AWX API
endpoints. Below are examples of how to work with job templates and workflow job
templates.

> [!NOTE]
> The library uses Pydantic models to ensure that the data conforms to the AWX API's
> expected structure. This helps in reducing runtime errors by validating the data
> before sending it to the API.

#### 📜 Job Templates

```python
from pyawxapi.models import JobTemplateModel

# Create a new job template
new_job_template = JobTemplateModel(
    name="My New Job",
    inventory="inventory_1",
    project="project_1",
    playbook="deploy.yml"
)

created_job_template = client.job_template.create(new_job_template)

# Update an existing job template
updated_job_template = JobTemplateModel(
    name="Updated Job Template",
    inventory="inventory_1",
    project="project_1",
    playbook="deploy.yml"
)

client.job_template.update("My Job Template", updated_job_template)

# Delete a job template
client.job_template.delete("My Job Template")
```

#### 📜 Workflow Job Templates

```python
from pyawxapi.models import WorkflowJobTemplateModel

# Create a new workflow job template
new_workflow = WorkflowJobTemplateModel(
    name="Release Deployment Workflow",
    inventory="prod_inventory",
    extra_vars='{"version": "1.2.3"}'
)
created_workflow = client.workflow_job_template.create(new_workflow)
print(created_workflow)

# Update an existing workflow job template
updated_workflow = WorkflowJobTemplateModel(
    name="Updated Workflow",
    inventory="prod_inventory",
    extra_vars='{"version": "1.2.4"}'
)
client.workflow_job_template.update("Release Deployment Workflow", updated_workflow)

# Delete a workflow job template
client.workflow_job_template.delete("Release Deployment Workflow")
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Open an issue to discuss your proposed changes.
2. Fork the repository.
3. Clone the fork.
4. Create a new branch (`git checkout -b feature/my-feat-branch`).
5. Make your changes.
6. Commit your changes (`git commit -m "feat: Add mew feature"`).
7. Push to the branch (`git push origin feature/my-feat-branch`).
8. Open a pull request.

## 🧪 Testing

Run unit tests using `pytest`:

```sh
uv run pytest tests
```

## 🛠️ Roadmap

- Add asynchronous calls support.
- Add support for more AWX resources.
