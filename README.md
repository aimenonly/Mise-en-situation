# Automated Test Suite

This is the automated test suite repo. It uses **Pytest** to run tests and generates **JSON** and **Markdown** reports.


## Table of Contents


- [Automated Test Suite](#automated-test-suite)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running Tests](#running-tests)
    - [Reports](#reports)

## Project Structure

Here's an overview of the project structure:

/data ***Contains access details (hostname, username, password, etc.) and other reusable variables***

/reports ***JSON and Markdown files for test results***

/tests ***All test cases***

/utils ***Reusable functions***

/runner.sh ***Shell script to run the tests***

main.py ***Main to execute the test suite in Python***

requirements.txt ***Needed dependencies***

## Prerequisites

Before running the test suite, ensure that the following dependencies are installed:

1. **Python 3.x**
2. **Packages**:
   - Paramiko
   - SCP
   - Pytest

### Installation

You can set up the environment by installing the dependencies listed in the `requirements.txt` file:

```bash
   pip install -r requirements.txt
```

### Running Tests

**Running with Python**

To run the test suite, execute the following command:

```bash
   python main.py
```


This will run the test cases defined in the /tests directory and generate test result reports in both JSON and Markdown formats inside the /reports/ directory.


**as part of a CI/CD pipeline**

use the runner.sh shell script

```bash
   ./runner.sh
```

The script will run the tests and provide the results in the same manner as running main.py.

### Reports

After running the tests, results are generated in the /reports/ directory:

    test_report.json: A machine-readable JSON file.
    test_report.md: A human-readable Markdown.
