# 🔍 OSINT Tools Comparison & Analytics Framework

An empirical threat intelligence data model and analytical system built to research, weigh, evaluate, and demonstrate the capabilities of popular Open-Source Intelligence (OSINT) tools. Designed for SOC analysts, Blue Teams, and threat researchers looking to optimize their reconnaissance workflows and understand attacker footprinting techniques.

---

## 💻 Overview

In modern cybersecurity operations, Open-Source Intelligence (OSINT) serves as a foundational pillar for attack surface management, red team simulations, and proactive threat hunting. However, the sheer volume of open-source tooling makes choosing the right platform for specific investigative goals a bottleneck.

This project delivers a **data-driven analytical dashboard** that normalizes, scores, and visualizes the operational capabilities of industry-standard OSINT engines (such as Maltego, Shodan, SpiderFoot, and Amass). By utilizing an algorithmic weighting core, users can dynamically filter and isolate tools based on deployment complexity, targets, and tactical use cases.

---

## ✨ Features

* **Algorithmic Weighting Core:** Dynamically calculates composite capability scores ($1.0 - 10.0$) using weighted vectors across 7 distinct operational metrics.
* **Dynamic Visualization Engine:** Implements interactive bar charts and multi-variable scatter plots mapping tool accuracy against performance speed profiles.
* **Granular Filtering & Parameter Tuning:** Allows users to narrow down candidate tools by specific security use cases and deployment setup complexity.
* **Deep-Dive Tactical Profiles:** Comprehensive indexing of features, data feeds, strengths, and limitations for 8+ top-tier platforms.
* **Compliance-Ready Exporters:** One-click generation of enterprise-grade reporting files in both structured CSV and formatted Excel (XLSX) formats.

---

## 🏗️ Architecture

The framework relies on a decoupled **Model-View-Controller (MVC)** inspired architecture, separating the telemetry data from calculation algorithms and rendering layouts.

```
       [ Client Browser ] <--- WebSocket ---> [ UI Dashboard (dashboard.py) ]
                                                     │
                                           Reads Engine Matrices
                                                     ▼
    [ Metric Computations (utils.py) ] <---> [ Analytics Core (engine.py) ]
                                                     │
                                           Ingests Asset Profiles
                                                     ▼
                                        [ JSON Database (Dataset) ]

```

---

## 🛠️ Technology Stack

* **Programming Language:** Python 3.10 / 3.11
* **User Interface Framework:** Streamlit (v1.32.0)
* **Data Processing & Analytics:** Pandas (v2.2.1), NumPy (v1.26.4)
* **Visualization Layer:** Matplotlib (v3.8.3), Seaborn (v0.13.2)
* **Excel Processing Matrix:** OpenPyXL (v3.1.2)

---

## ⚙️ Installation

### Prerequisites

* Python 3.10 or higher installed globally on your workstation.
* Standard `pip` package manager and `venv` isolation modules configured.

### Clone Repository

```bash
git clone https://github.com/muhammad-umair09/osint-tools-comparison.git
cd osint-tools-comparison

```

### Install Dependencies

Set up a clean virtual environment sandbox and update package specifications:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

```

### Run Project

Initialize the local analytical server web interface instance:

```bash
streamlit run app/dashboard.py

```

---

## 📖 Usage

Follow these step-by-step instructions to extract tactical metrics using the interface:

1. **Access the Framework:** Open your local browser to `http://localhost:8501`.
2. **Filter by Use Case:** Use the sidebar dropdown menu to isolate tools addressing specific demands, such as *Attack Surface Management* or *Phishing Assessment Prep*.
3. **Tune Setup Complexity:** Check or uncheck complexity parameters (`Low`, `Medium`, `High`) depending on your operational deployment constraints.
4. **Inspect Granular Profiles:** Scroll to the "Deep-Dive Granular Intelligence Profiles" section, choose a tool, and examine its raw APIs, advantages, and drawbacks.
5. **Export Reports:** Scroll to the bottom and click **Export Enterprise Grade Report to Excel** to pull formatting sheets into your local report folder.

---

## 📂 Project Structure

```text
osint-tools-comparison/
│
├── app/
│   ├── __init__.py          # Package initialization configuration
│   ├── config.py            # Global dashboard titles, constants, and metric weights
│   ├── dashboard.py         # Primary Streamlit rendering and layout matrix
│   ├── engine.py            # Computational logic and telemetry normalization core
│   └── utils.py             # Downstream export engines for CSV and Excel files
│
├── data/
│   └── osint_tools_dataset.json  # Raw telemetry metadata profile records
│
├── docs/
│   └── RESEARCH.md          # Comprehensive open-source engineering study paper
│
├── .gitignore               # System, IDE, and venv tracking exclusion lists
├── README.md                # Enterprise-grade documentation matrix
└── requirements.txt         # Package dependency specification matrix

```

---

## 🔧 Configuration

All application weighting paradigms are controlled centrally through `app/config.py`. To recalibrate the grading algorithms, open the file and adjust the `WEIGHTS` dictionary values. Ensure the total value sums up to exactly $1.0$:

```python
# app/config.py
WEIGHTS = {
    "features": 0.15,
    "ease_of_use": 0.10,
    "accuracy": 0.15,
    "performance": 0.15,
    "automation": 0.15,
    "reporting": 0.10,
    "data_sources": 0.20  # Given highest priority vector
}

```

---

## 🛡️ Security Considerations

* **Passive Reconnaissance Safety:** Running this application interface performs no active remote scanning against targeted entities; it is entirely client-side safe.
* **API Key Management:** No actual API keys are required or stored to utilize this system. All telemetry values represent normalized performance benchmarks based on empirical research.

---

## 🧪 Testing

To validate data processing and verify schema correctness, run standard testing executions:

```bash
python -m unittest discover -s app -p "*engine*.py"

```

---



## ⚡ Performance Optimization

* **Vectorized Computations:** All score calculation logic maps through vector matrices inside Pandas dataframes rather than standard sequential Python loops, allowing real-time calculations.
* **Memory Optimization:** Aggressive list flattening ensures that dashboard refreshes load under 150ms.



## 🤝 Contributing

Contributions to improve our metric datasets or add support for new platform tools are highly encouraged. Please review the instructions below:

1. Fork the project repository.
2. Create your feature development branch (`git checkout -b feature/AmazingFeature`).
3. Commit your localized architectural modifications (`git commit -m 'Add new feature'`).
4. Push to the remote branch target upstream (`git push origin feature/AmazingFeature`).
5. Open a professional Pull Request detailing your changes.

---

## 📐 Code Style Guidelines

* **PEP 8 Compliance:** All script structures must adhere strictly to standard PEP 8 syntax standards.
* **Docstring Requirements:** Every function module must contain an explicit docstring stating parameters, return types, and algorithmic limits.

---

## 🔄 Git Workflow

* **Main Branch Stability:** The `main` branch remains protected at all times. Direct pushes are barred.
* **Branch Naming Standard:** Use prefixes such as `feature/`, `bugfix/`, or `docs/` followed by descriptive hyphenated nouns.

 