from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv

# -------------------------------------------------------------------
# Environment Setup
# -------------------------------------------------------------------
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# -------------------------------------------------------------------
# Agent 1: Web Search (TOOLS → OpenAI ONLY)
# -------------------------------------------------------------------
web_search_agent = Agent(
    name="WebSearchAgent",
    role=(
        "Collects the most recent and relevant financial news. "
        "Must ensure information is current and sourced."
    ),
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=[
        "Search only for the latest news (last few days if possible).",
        "Summarize findings concisely.",
        "Always include source citations.",
        "Do NOT provide investment advice."
    ],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# Agent 2: Market Data Analyst (TOOLS → OpenAI ONLY)
# -------------------------------------------------------------------
financial_data_agent = Agent(
    name="FinancialDataAgent",
    role="Analyzes structured financial data and analyst sentiment.",
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=[
        "Retrieve analyst recommendations and key financial metrics.",
        "Use tables for clarity.",
        "Remain factual; do not speculate or give advice.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# Agent 3: Investment Reasoning Agent (NO TOOLS → Groq)
# -------------------------------------------------------------------
investment_reasoning_agent = Agent(
    name="InvestmentReasoningAgent",
    role=(
        "Synthesizes news and financial data into coherent "
        "investment insights and risk-aware recommendations."
    ),
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=[
        "Combine analyst sentiment with recent news.",
        "Discuss risks, upside potential, and uncertainty.",
        "Provide high-level investment perspective (not financial advice).",
        "Be concise, structured, and professional."
    ],
    markdown=True,
)

# -------------------------------------------------------------------
# Orchestrator Agent (Coordinates all agents)
# -------------------------------------------------------------------
multi_ai_agent = Agent(
    name="MultiAgentFinancialAdvisor",
    team=[
        web_search_agent,
        financial_data_agent,
        investment_reasoning_agent,
    ],
    instructions=[
        "Delegate news gathering to WebSearchAgent.",
        "Delegate market data analysis to FinancialDataAgent.",
        "Delegate final synthesis to InvestmentReasoningAgent.",
        "Ensure a clear, logical flow from data → insight → conclusion."
    ],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# Run
# -------------------------------------------------------------------
multi_ai_agent.print_response(
    "Summarize analyst recommendations and share the latest news about Oracle. "
    "Based on this information, provide an investment outlook."
)
