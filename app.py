from agents import Agent, PlannerAgent, Summarizer
from newsAPI import get_titles
import json

planner_prompt = """
    You are a journalist assistant. Your job is to structure a NewsAPI query to find the latest news about a topic.
    The research topic is: "{research_question}".

    The query should be structured as follows:
    {{
       "category": category,
       "q": query
    }}
"""

summarizer_prompt = """
    Please summarize the followung information for the user.
    The user was asking this question question is: {research_question}.
    And obtained the following results: {titles}
"""



def main():
    agent_plan = PlannerAgent(model="gpt-3.5-turbo-0125", temperature=0.7, prompt=planner_prompt)
    agent_summ = Summarizer(model="gpt-3.5-turbo-0125", temperature=0.7, prompt=summarizer_prompt)

    question = "I am pretty concerned about the latest news on AI. Can you help me find some articles?"

    response = agent_plan.invoke(research_question=question)
    response = json.loads(response)
    resp = get_titles(category=response['category'], query=response['q'])
    user_resp = agent_summ.invoke(research_question=question, titles=resp)

    print("User response: ", user_resp)

if __name__ == "__main__":
    main()