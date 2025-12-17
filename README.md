# 📈 Multi-Agent Financial Intelligence System

A **production-grade multi-agent AI system** that combines **real-time financial news, structured market data, and advanced reasoning models** to provide comprehensive investment insights. Built using **Phi**, **OpenAI**, **Groq**, and finance tools like **YFinance** and **DuckDuckGo**.

---
## Project Overview

This system is composed of **three specialized agents**:

1. **WebSearchAgent** – Fetches the latest financial news using DuckDuckGo.
2. **FinancialDataAgent** – Retrieves structured market and analyst data from YFinance.
3. **InvestmentReasoningAgent** – Synthesizes news and market data to provide high-level investment insights using Groq LLMs.

The agents communicate in a coordinated fashion to provide a **clear, concise, and structured financial outlook**.

---

## Features

- ✅ Multi-agent coordination for financial analysis
- ✅ Live news retrieval with DuckDuckGo
- ✅ Real-time market and analyst data with YFinance
- ✅ Structured, table-based data presentation
- ✅ High-performance reasoning with Groq LLMs
- ✅ Interactive Playground UI for exploration and testing

---

## Getting Started

### Prerequisites

- Python 3.10+
- Anaconda or virtual environment
- Phi library (`pip install phi`)
- OpenAI Python SDK (`pip install openai`)
- Groq SDK (`pip install groq`)
- DuckDuckGo & YFinance tools (`pip install ddgs yfinance`)
- `.env` file containing:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

## Installation

git clone https://github.com/your-username/financial-agent.git
cd financial-agent/finance_agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Usage

1) python playground.py

2) Go to Phidata website -> playground -> connect with AI under localhost:7777


