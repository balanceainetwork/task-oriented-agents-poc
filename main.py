from crewai import Crew
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()

from token_analysis_agents import TokenAnalysisAgents
from token_analysis_tasks import TokenAnalysisTasks





class FinancialCrew:
  def __init__(self, token):
    self.token = token

  def run(self):
    agents = TokenAnalysisAgents()
    tasks = TokenAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.token)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
    anouncement_task = tasks.anouncement_analysis(financial_analyst_agent)
    recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        anouncement_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Crypto Tokens Analysis Crew")
  print('-------------------------------')
  token = input(
    dedent("""
      What is the token you want to analyze?
    """))
  
  financial_crew = FinancialCrew(token)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
