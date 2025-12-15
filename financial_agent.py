from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTool
from phi.tools.duckduckgo import DuckDuckGo


web_search_agent = Agent(
  name="WebSearchAgent",
  role="A financial agent that uses web search to gather information about financial markets and companies.",
  model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
  tools=[DuckDuckGo(),],
  instructions=["Always provide sources for web search results."],
  show_tool_calls=True,
  markdown=True,
)

finacial_agent = Agent(
  name="FinancialAgent",
  role="A financial agent that provides investment advice based on market data and trends.",
  model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
  tools=[
    YFinanceTool(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
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

multi_ai_agent = Agent(
  team=[web_search_agent, finacial_agent],
  instructions=[
    "Collaborate to provide comprehensive financial advice.",
    "The WebSearchAgent is responsible for gathering the latest news and trends using web search.",
    "The FinancialAgent analyzes market data and provides investment advice based on the information gathered.",
    "Communicate clearly and cite sources when providing information."
  ],
  show_tool_calls=True,
  markdown=True,
)