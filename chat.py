import re
import random
import sys

class RuleBasedChatbot:
    def __init__(self, rules, default_response="Sorry, I don't understand that."):
        """
        Initialize the chatbot with:
          - rules: a list of (pattern, responses) tuples
          - default_response: fallback when no rule matches
        """
        self.rules = [(re.compile(pattern, re.IGNORECASE), responses)
                      for pattern, responses in rules]
        self.default_response = default_response

    def get_response(self, user_input: str) -> str:
        """Return a response based on matching rules."""
        user_input = user_input.strip()
        for pattern, responses in self.rules:
            if pattern.match(user_input):
                return random.choice(responses)
        return self.default_response

    def chat_loop(self, prompt="You: ", exit_commands=None):
        """Run a chat loop until one of exit_commands is entered."""
        if exit_commands is None:
            exit_commands = ("bye", "exit", "quit")
        print("Chatbot: Hello! (type one of {} to quit)".format(exit_commands))
        while True:
            try:
                user_input = input(prompt)
            except (EOFError, KeyboardInterrupt):
                print("\nChatbot: Goodbye!")
                break

            if user_input.strip().lower() in exit_commands:
                print("Chatbot: Goodbye!")
                break

            response = self.get_response(user_input)
            print("Chatbot:", response)


if __name__ == "__main__":
    # Define rules: pattern -> list of possible responses
    rules = [
        (r"^(hello|hi|hey)$", ["Hi there!", "Hello! How can I help you?"]),
        (r"^how are you\??$", ["I'm fine, thanks! How about you?", "Doing well — thanks for asking!"]),
        (r"^(thanks|thank you)$", ["You're welcome!", "No problem at all!"]),
        (r"^(bye|goodbye)$", ["Goodbye! Have a nice day!", "See you later!"]),
        # catch-all fallback (pattern matches anything)
        (r".*", ["Hmm — can you rephrase that?", "I’m sorry, I didn’t catch that."])
    ]

    bot = RuleBasedChatbot(rules)
    bot.chat_loop()
