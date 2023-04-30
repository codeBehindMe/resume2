import openai


class Chat:
    def __init__(self) -> None:
        self.session_id = "foo"
        self.messages = []
        self.model = "gpt-3.5-turbo"
        self.initial_context = "You're a friendly chatbot"
        self.append_to_history("system", self.initial_context)

    def append_to_history(self, role: str, message: str):
        self.messages.append({"role": role, "content": message})

    def ask_something(self, input_message: str) -> str:
        self.append_to_history("user", input_message)

        resp = openai.ChatCompletion.create(model=self.model, messages=self.messages)

        response_message = resp.choices[0].message
        self.append_to_history(response_message["role"], response_message["content"])
        print(self.messages)

        return resp.choices[0].message
