from crewai import Agent

import os

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

from langchain.chat_models import ChatOpenAI


llm = ChatOpenAI(model='gpt-3.5-turbo',openai_api_key=os.environ['OPENAI_API_KEY']) # Loading GPT-3.5

class TokenAnalysisAgents():
  

  def financial_analyst(self):
    return Agent(
      role='The Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in crypto market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
 
       
      ]
    )

  def research_analyst(self):
    return Agent(
      role='Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, projects announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
     
  
      
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal="""Impress your customers with full analysis of token
      and cyrpto project""",
      backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic thoughts. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
    

      ]
    )