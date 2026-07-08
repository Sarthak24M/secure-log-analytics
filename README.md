# Secure Log Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/Apache%20Spark-4.1.2-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=flat&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=flat&logo=react&logoColor=black)
![MUI](https://img.shields.io/badge/Material%20UI-v9-007FFF?style=flat&logo=mui&logoColor=white)


A full-stack security log analytics platform that ingests Ubuntu authentication logs, processes them through an Apache Spark pipeline, and surfaces detections and analytics through a Flask REST API and a React dashboard.

> Built during a 45-day internship as a working proof-of-concept for scalable, structured log analysis.

---

## Overview

### Problem Statement

Ubuntu authentication logs (`/var/log/auth.log`) are a critical source of security signal — failed logins, privilege escalations, brute-force attempts, and root activity all leave traces there. But these logs are unstructured plaintext, and analysing them at scale requires more than shell scripts or grep.

### Motivation

This project explores how distributed data processing tools — specifically Apache Spark — can be applied to the security domain to turn raw syslog output into structured, queryable intelligence. The result is a pipeline that parses, classifies, and runs security detections on auth logs, with results exposed through a REST API and visualised in a live dashboard.

### Why Ubuntu Auth Logs

`auth.log` is a well-defined, real-world log format with high signal density: every SSH attempt, `sudo` invocation, PAM event, and session lifecycle event is recorded there. It is a natural fit for demonstrating log parsing, event classification, and security detection in a compact, reproducible way.

### Why Apache Spark

Spark's DataFrame API allows the same parsing and detection logic to scale from a single log file to a distributed dataset with no code changes. Using PySpark here, rather than pandas, demonstrates the architectural decision to build for scale from the start.

---

## Features

- [x] Structured parsing of raw Ubuntu `auth.log` using regex-based Spark transformations
- [x] Field extraction: username, target user, command, UID, TTY, CWD, session ID, IP address
- [x] Event classification into 9 categories: `AUTH_FAILURE`, `AUTH_SUCCESS`, `PASSWORD_CHANGE`, `PRIVILEGED_COMMAND`, `SESSION_OPEN`, `SESSION_CLOSE`, `CRON_JOB`, `SYSTEM_SHUTDOWN`, `SYSTEM_STARTUP`
- [x] Severity classification: `HIGH`, `MEDIUM`, `LOW` per event type
- [x] Security detections: brute-force, root activity, excessive privileged commands, high-severity alerts
- [x] Analytics: event distribution, authentication summary, top users, top processes
- [x] DataFrame caching to avoid rebuilding the pipeline on repeated API calls
- [x] Flask REST API with CORS support
- [x] React dashboard with Material UI dark theme
- [x] Live data — dashboard fetches from all three API endpoints
- [x] Clickable summary cards that drill down into the underlying log records
- [x] Loading and error states in the dashboard
- [x] Benchmark utility for timing pipeline stages
- [x] Modular pipeline architecture (reader → parser → extractor → classifier → analytics/detections)

---

## System Architecture

```mermaid
graph TD
    A[Ubuntu auth.log] --> B[Reader\npipeline/reader.py]
    B --> C[Parser\npipeline/parser.py]
    C --> D[Feature Extractor\npipeline/extractor.py + extractors.py]
    D --> E[Classifier\npipeline/classifier.py]
    E --> F[Pipeline Cache\npipeline/cache.py]
    F --> G[Analytics\npipeline/analytics.py]
    F --> H[Detections\npipeline/detections.py]
    G --> I[Flask REST API\napi/app.py]
    H --> I
    I --> J[/api/summary]
    I --> K[/api/analytics]
    I --> L[/api/detections]
    J --> M[React Dashboard\nfrontend/src]
    K --> M
    L --> M
```

---

## Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Log Processing | Apache Spark (PySpark) | 4.1.2 |
| Backend | Flask | 3.1.3 |
| Backend | Flask-CORS | — |
| Frontend | React | 19 |
| Frontend | Material UI | v9 |
| Frontend | Vite | 8 |
| Runtime | Python | 3.11+ |
| Data | pandas | 3.0.3 |
| Data | NumPy | 2.5.0 |

---

## Project Structure

```
secure-log-analytics/
│
├── api/                        # Flask REST API
│   ├── __init__.py
│   ├── app.py                  # Route definitions
│   └── services.py             # Business logic; calls pipeline functions
│
├── data/
│   └── raw/
│       └── auth.log            # Ubuntu authentication log (sample)
│
├── frontend/                   # React + Vite application
│   ├── public/
│   │   └── favicon.svg
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   └── SummaryCard.jsx
│   │   ├── pages/
│   │   │   └── Dashboard.jsx   # Main view with summary, analytics, detections
│   │   ├── services/
│   │   │   └── api.js          # Fetch wrappers for all three endpoints
│   │   ├── theme.js            # MUI dark theme configuration
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── pipeline/                   # PySpark processing pipeline
│   ├── __init__.py
│   ├── spark_session.py        # SparkSession factory
│   ├── reader.py               # Reads raw log file into a DataFrame
│   ├── parser.py               # Regex parsing into structured columns
│   ├── patterns.py             # All regex patterns (centralised)
│   ├── extractors.py           # Field extraction functions
│   ├── extractor.py            # Applies extractors; adds auth_status
│   ├── classifier.py           # Event type and severity classification
│   ├── analytics.py            # Aggregation queries
│   ├── detections.py           # Security detection logic
│   ├── engine.py               # Assembles the full pipeline
│   └── cache.py                # Singleton pipeline cache for the API
│
├── tools/
│   └── benchmark.py            # Pipeline timing utility
│
├── main.py                     # CLI entry point (runs pipeline, prints results)
└── requirements.txt
```

---

## Prerequisites

- Python 3.11+
- Java 8 or 11 (required by Apache Spark — `JAVA_HOME` must be set)
- Node.js 18+
- npm

Verify Java is available:

```bash
java -version
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sarthak24M/secure-log-analytics.git
cd secure-log-analytics
```

### 2. Set up the Python environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Install frontend dependencies

```bash
cd frontend
npm install
```

---

## Running the Project

### Start the Flask API

From the root of the repository:

```bash
# Option 1 — Flask CLI
python -m flask --app api/app.py run

# Option 2 — direct
python api/app.py
```

The API will be available at `http://127.0.0.1:5000`.

> **Note:** The first request triggers the Spark pipeline build, which takes a few seconds. Subsequent requests use the cached DataFrame.

### Start the React dashboard

In a separate terminal:

```bash
cd frontend
npm run dev
```

The dashboard will be available at `http://localhost:5173`.

### Run the pipeline directly (CLI)

To run the full pipeline and print results to the terminal without starting the API:

```bash
python main.py
```

---

## API Documentation

| Method | Route | Description | Response |
|---|---|---|---|
| `GET` | `/` | Health check | `{ "message": "Secure Log Analytics API is running." }` |
| `GET` | `/api/summary` | Dashboard summary counts | `{ total_events, authentication_failures, high_severity_alerts, password_changes, privileged_commands }` |
| `GET` | `/api/analytics` | Aggregated analytics | `{ event_distribution, authentication_summary, top_users, top_processes }` |
| `GET` | `/api/detections` | Security detections | `{ high_severity_alerts, authentication_failures, password_changes, brute_force, root_activity, excessive_privileged_commands }` |

<details>
<summary>Example: <code>GET /api/summary</code></summary>

```json
{
  "total_events": 289,
  "authentication_failures": 12,
  "high_severity_alerts": 12,
  "password_changes": 1,
  "privileged_commands": 8
}
```
</details>

<details>
<summary>Example: <code>GET /api/detections</code> (partial)</summary>

```json
{
  "brute_force": [
    { "target_user": "sarthak-swayam", "failed_attempts": 5 }
  ],
  "root_activity": [
    {
      "timestamp": "2026-06-16T09:15:35",
      "username": "root",
      "target_user": "root",
      "process": "passwd",
      "event_type": "PASSWORD_CHANGE",
      "command": "",
      "severity": "MEDIUM"
    }
  ]
}
```
</details>

---

## Security Detections

| Detection | Logic | Severity |
|---|---|---|
| Authentication Failures | All events with `event_type == AUTH_FAILURE` | HIGH |
| Brute Force | Users with ≥ 3 failed authentication attempts | HIGH |
| Root Activity | Events where `username`, `target_user`, or `uid` is root (CRON excluded) | MEDIUM–HIGH |
| Excessive Privileged Commands | Users with ≥ 3 `PRIVILEGED_COMMAND` events | MEDIUM |
| Password Change Alerts | All `PASSWORD_CHANGE` events | MEDIUM |
| High Severity Alerts | All events with `severity == HIGH` | HIGH |

---

## Event Classification

| Event Type | Pattern Matched |
|---|---|
| `AUTH_FAILURE` | `Failed password`, `authentication failure`, `Invalid user`, `Failed publickey` |
| `AUTH_SUCCESS` | `Accepted password`, `Accepted publickey` |
| `PASSWORD_CHANGE` | `password.*changed`, `changed by` |
| `PRIVILEGED_COMMAND` | `executing command` |
| `SESSION_OPEN` | `session opened` |
| `SESSION_CLOSE` | `session closed` |
| `CRON_JOB` | Process name starts with `cron` |
| `SYSTEM_SHUTDOWN` | `powering down`, `power off`, `shutdown` |
| `SYSTEM_STARTUP` | `startup`, `system boot`, `boot completed` |

---

## Performance & Benchmarking

### Pipeline Optimisation

The pipeline uses **DataFrame caching** (`pipeline/cache.py`) to avoid rebuilding the Spark execution plan on every API call. A singleton pattern holds the `SparkSession` and `classified_logs` DataFrame in memory for the lifetime of the Flask process.

```python
# pipeline/cache.py
def get_pipeline():
    global _spark, _classified_logs
    if _spark is None or _classified_logs is None:
        _spark, _classified_logs = build_pipeline()
    return _spark, _classified_logs
```

The first API request pays the full build cost; all subsequent requests query the already-cached DataFrame.

### Running the Benchmark

```bash
python tools/benchmark.py
```

Sample output format:

```
========== PIPELINE BENCHMARK ==========

Pipeline Build Time : X.XXXX seconds
Summary Time        : X.XXXX seconds
Analytics Time      : X.XXXX seconds

========================================
```

---

## Screenshots

> _Screenshots to be added once the application is running in production configuration._

| View | Description |
|---|---|
| `docs/screenshots/dashboard.png` | Main dashboard with summary cards |
| `docs/screenshots/analytics.png` | Event distribution and top users tables |
| `docs/screenshots/detections.png` | Brute force and root activity detections |
| `docs/screenshots/benchmark.png` | Benchmark output in terminal |

---

## Future Enhancements

- **Docker Compose** — containerise Flask and the frontend; remove the manual setup requirement
- **Kafka integration** — stream live `auth.log` entries instead of batch-processing a static file
- **Elasticsearch / OpenSearch** — replace in-memory Spark results with an indexed store for faster queries and log retention
- **Cloud deployment** — deploy the pipeline on AWS EMR or Databricks for true distributed processing
- **Authentication** — add JWT-based auth to the Flask API so the dashboard is not publicly accessible
- **RBAC** — role-based access control for analyst vs. admin views
- **Additional log sources** — extend the parser to support `/var/log/syslog`, nginx access logs, and Windows Event Logs
- **Alerting** — webhook or email notifications when brute-force or root activity thresholds are exceeded

---


---

## Author

**Sarthak Swayam**  
B.Tech Computer Science (Gaming Technology)  
VIT Bhopal University

[![GitHub](https://img.shields.io/badge/GitHub-Sarthak24M-181717?style=flat&logo=github)](https://github.com/Sarthak24M)
