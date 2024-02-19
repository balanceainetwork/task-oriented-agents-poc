from crewai import Task
from textwrap import dedent

class TokenAnalysisTasks():
  def research(self, agent, token):
    return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the crypto token and
        its industry.
        Pay special attention to any significant events, market
        sentiments, and analysts' opinions. Also include upcoming 
        events like earnings and others.
  
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the token price.
        Also make sure to return the token name for the token.
  
        Make sure to use the most recent data as possible.
  
        Selected token by the customer: {token}
      """),
      agent=agent
    )
    
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""
        Conduct a thorough analysis of the crypto token performance, project developments and market performance. 
        This includes examining key financial metrics such as
        user base, marketcap
        Also, analyze the token's performance in comparison 
        to its industry peers and overall market trends.

        Your final report MUST expand on the summary provided
        but now including a clear assessment of the token
        performance, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario.

        Make sure to use the most recent data possible.
      """),
      agent=agent
    )

  def anouncement_analysis(self, agent):
    return Task(description=dedent(f"""
        Analyze the latest announcements for
        the token in question from sources like cryptonews.com and coindesk.com
        Focus on key sections like partnerships, major deliverables, significant events, 
        and any disclosed risks.
        Extract relevant data and insights that could influence
        the token's future performance.

        Your final answer must be an expanded report that now
        also highlights significant findings from these anouncements,
        including any red flags or positive indicators for
        your customer.
           
      """),
      agent=agent
    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive report. 
        
        You MUST Consider all aspects, including performance aspect of the token
        ,market sentiment, announcements, community engagement and qualitative data from
        internet sources.

        Make sure to include a section that shows significant announcements, and upcoming events like major milestones.

        Your final answer MUST be a comprehensive report for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
       
      """),
      agent=agent
    )


