import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_community.document_transformers import Html2TextTransformer

from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model='gpt-3.5-turbo',openai_api_key=os.environ['OPENAI_API_KEY']) # Loading GPT-3.5



class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    # Load HTML
    loader = AsyncHtmlLoader([website])
    docs = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    
    content = docs_transformed[0].page_content
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing research and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do research about a given topic.",
          llm=llm,
          verbose=False,
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)

if __name__ == "__main__":
  df = BrowserTools()
  summary = df.scrape_and_summarize_website("https://www.geeksforgeeks.org/agents-artificial-intelligence/")
  print(summary)