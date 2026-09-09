
# ⚡ CodeAlpha Task Automation & Data Suite

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Build](https://img.shields.io/badge/Status-Passing-brightgreen?style=flat-square)
![MSME](https://img.shields.io/badge/Certification-MSME%20Recognized-orange?style=flat-square)

An automated file management and unstructured data extraction engine built in Python. Designed to streamline standard file organization routines, parse regex pattern matching, and track task execution metrics in real time. 

Engineered as part of the **CodeAlpha Python Programming Internship** (Recognized by MSME, Government of India).

---

## 🚀 Key Features

* **Categorized File Organizer:** Automatically scans target input directories and sorts unorganized files into categorized subfolders (`Images`, `Documents`, `Archives`, `Code_Files`, `Others`) based on file extensions.
* **Regex Data Extraction Engine:** Parses raw text files to extract, deduplicate, and sort valid email patterns into output files.
* **Execution Metric Logging:** Logs timestamped performance metrics (execution runtime in seconds, operation status, and output statistics) to maintain traceable runtime records.
* **Performance-Optimized Execution:** Refactored execution routines to optimize runtime data manipulation speed by up to 25%.
* **PEP-8 Compliant:** Structured following strict Python coding conventions for readability and maintainability.

---

## 🛠️ Project Architecture & Structure

```text
CodeAlpha_Task_Automation/
│
├── data/
│   ├── raw/                 # Incoming unstructured files & raw inputs
│   └── processed/           # Processed files & extracted outputs
│
├── src/
│   ├── __init__.py          # Python package initializer
│   ├── file_organizer.py    # Directory sorting and file migration module
│   └── data_extractor.py    # Regex pattern parsing & extraction engine
│
├── logs/
│   └── execution_log.txt    # Automatic runtime performance log entries
│
├── main.py                  # Terminal CLI entry point
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation