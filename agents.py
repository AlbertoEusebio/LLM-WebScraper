from openAI import get_llm

class Agent:
    def __init__(self, model, temperature, prompt):
        self.prompt = prompt
        self.llm = get_llm(model=model, temperature=temperature)
        self.state = {}

    def get_llm(self):
        return self.llm

    def update_state(self, key, value):
        self.state[key] = value

    def invoke(self, *args, **kwargs):
        raise NotImplementedError


class PlannerAgent(Agent):
    def invoke(self, research_question):

        prompt = self.prompt.format(research_question=research_question)

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"research question: {research_question}"}
        ]

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        self.update_state("planner_response", response)

        print("Planner response: ", response) # print to console the response

        return response


class Summarizer(Agent):
    def invoke(self, research_question, titles):

        prompt = self.prompt.format(titles=titles, research_question=research_question)

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Titles: {titles}, research question: {research_question}"}
        ]

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        self.update_state("summary_response", response)

        print("Summarizer response: ", response) # print to console the response

        return response