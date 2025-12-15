import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

web_search_agent = Agent(
  name="WebSearchAgent",
  role="A financial agent that uses web search to gather information about financial markets and companies.",
  model=Groq(id="llama-3.1-8b-instant"),
  tools=[DuckDuckGo(),],
  instructions=["Always provide sources for web search results."],
  show_tool_calls=True,
  markdown=True,
)

finacial_agent = Agent(
  name="FinancialAgent",
  role="A financial agent that provides investment advice based on market data and trends.",
  model=Groq(id="llama-3.1-8b-instant"),
  tools=[
    YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
  ],
  instructions=[
    "Use web search to gather the latest news and trends about financial markets and companies.",
    "Analyze market data using the YFinance tool to provide informed investment advice.",
    "Always cite your sources when providing information from web searches.",
    "Use tables to display data clearly."
  ],
  show_tool_calls=True,
  markdown=True,
)

app=Playground(agents=[finacial_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)