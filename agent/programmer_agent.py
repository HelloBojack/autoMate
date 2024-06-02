from actions.action_util import ActionUtil
from agent.prompt import programmer_prompt
from utils.llm_util import LLM_Util


class ProgrammerAgent:
    def __init__(self):
        action_descriptions = ""
        for action_class in ActionUtil.get_actions():
            action = action_class()
            action_descriptions += action.package_actions_description() + "\n"
        self.messages = [{"content": programmer_prompt.substitute(python_code=action_descriptions), "role": "system"}]

    def run(self, question):
        self.messages.append({"content": question, "role": "user"})
        res = LLM_Util().invoke(self.messages)
        self.messages.append({"content": res["content"], "role": "assistant"})
        return res["content"]

        




