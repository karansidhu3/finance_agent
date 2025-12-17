from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv
import os

# ---------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ---------------------------------------------------------------------
# Agent 1: Web Search Agent (TOOLS → OpenAI ONLY)
# ---------------------------------------------------------------------
web_search_agent = Agent(
    name="WebSearchAgent",
    role="Fetches the most recent financial and company-specific news.",
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=[
        "Search for the most recent news only.",
        "Summarize results clearly.",
        "Always include source citations.",
        "Do NOT provide opinions or investment advice."
    ],
    show_tool_calls=True,
    markdown=True,
)

# ---------------------------------------------------------------------
# Agent 2: Financial Data Agent (TOOLS → OpenAI ONLY)
# ---------------------------------------------------------------------
financial_data_agent = Agent(
    name="FinancialDataAgent",
    role="Retrieves and summarizes structured market and analyst data.",
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
        "Present analyst recommendations and fundamentals.",
        "Use tables where appropriate.",
        "Remain factual and objective.",
        "Do NOT provide investment advice."
    ],
    show_tool_calls=True,
    markdown=True,
)

# ---------------------------------------------------------------------
# Agent 3: Investment Reasoning Agent (NO TOOLS → Groq)
# ---------------------------------------------------------------------
investment_reasoning_agent = Agent(
    name="InvestmentReasoningAgent",
    role="Synthesizes news and financial data into investment insights.",
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=[
        "Combine analyst sentiment with recent news.",
        "Highlight risks, opportunities, and uncertainty.",
        "Provide a high-level investment outlook (not financial advice).",
        "Be concise, structured, and professional."
    ],
    markdown=True,
)

# ---------------------------------------------------------------------
# Playground App
# ---------------------------------------------------------------------
app = Playground(
    agents=[
        web_search_agent,
        financial_data_agent,
        investment_reasoning_agent,
    ]
).get_app()


# ---------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
