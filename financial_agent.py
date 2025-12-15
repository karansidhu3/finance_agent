from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTool
from phi.tools.duckduckgo import DuckDuckGo


web_search_agent = Agent(
  name="WebSearchAgent",
  role="A financial agent that uses web search to gather information about financial markets and companies.",
  model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
  tools=[
    DuckDuckGo(),
    YFinanceTool()
  ],
  instructions=["Always provide sources for web search results."],
  show_tool_calls=True,
  markdown=True,
)