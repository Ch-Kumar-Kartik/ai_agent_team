from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()

model = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

web_agent = Agent(
    name="Web Agent",
    model=model,
    tools=[GoogleSearchTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=model,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=model,
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

response = agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA")
print(response)