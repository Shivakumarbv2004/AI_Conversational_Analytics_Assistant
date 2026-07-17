# 📊 AI Conversational Analytics Assistant

An enterprise-grade, multi-agent AI system that allows users to ask natural language questions about a Supermarket Sales dataset and receive accurate, deterministic answers wrapped in highly professional business reports.

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Pandas](https://img.shields.io/badge/Analytics-Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Groq](https://img.shields.io/badge/LLM-Groq%20(Llama%203.1)-black?style=flat)

---

## ✨ Key Features
- **True AI Intent Classification:** A dedicated LLM `PlannerAgent` dynamically infers what the user wants to know, parsing complex natural language into precise analytical intents.
- **Deterministic Math, Zero Hallucinations:** Unlike standard LLMs that struggle with math, this architecture routes the intent to an `AnalyticsEngine` powered by **Pandas**. Aggregations (sums, averages, counts) are perfectly calculated against the underlying CSV.
- **Premium Glassmorphic UI:** A beautifully designed frontend built with Streamlit, utilizing custom CSS injections for a modern, sleek, and responsive user experience.
- **Automated Business Reporting:** The `ResponseAgent` takes the raw numbers and feeds them back to the LLM to generate professional, well-formatted reports including Executive Summaries, Key Findings, and Recommendations.

---

## 🏗️ Architecture (Multi-Agent System)

The backend is built around a centralized `Orchestrator` that delegates tasks to specialized agents:

1. **`PlannerAgent`**: Reads user input and asks the LLM to classify the intent into a specific tool (e.g., `sales_by_city`, `dashboard`).
2. **`RetrievalAgent`**: Takes the plan and executes the correct mathematical function inside the `AnalyticsEngine`.
3. **`AnalyticsEngine`**: Loads the CSV safely via a Singleton `DataLoader` and executes the requested Pandas dataframe manipulation.
4. **`ResponseAgent`**: Takes the mathematical output and asks the LLM to format it into a comprehensive business report.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- `uv` package manager (recommended for speed) or standard `pip`
- A free [Groq API Key](https://console.groq.com/keys)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shivakumarbv2004/AI_Conversational_Analytics_Assistant.git
   cd AI_Conversational_Analytics_Assistant
   ```

2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```
   *(Or `pip install -r requirements.txt`)*

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY="gsk_your_api_key_here"
   MODEL="llama-3.1-8b-instant"
   ```

### Running the Project

Start both the FastAPI backend and Streamlit frontend simultaneously with a single command:
```bash
python run.py
```
*Wait a few seconds, and your default browser will automatically open the AI Analytics Dashboard!*

---

## 💡 Example Queries to Try
Once the UI is open, try asking:
- *"Could you give me an overview of the dashboard?"*
- *"Which city generated the most sales?"*
- *"How are customers preferring to pay?"*
- *"Show me the top selling products."*
