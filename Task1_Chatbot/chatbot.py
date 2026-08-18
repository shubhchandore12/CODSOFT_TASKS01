
import re
import random
from datetime import datetime
 
 
class RuleBasedChatbot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.user_name = None
 
        
        self.rules = [
            (r'\b(hi|hello|hey|greetings)\b',
             ["Hello there! How can I help you today?",
              "Hi! Nice to hear from you.",
              "Hey! What's on your mind?"]),
 
            (r'\bmy name is (\w+)', self._set_name),
 
            (r'\bwhat.?s your name\b|\bwho are you\b',
             [f"I'm {self.name}, your friendly rule-based chatbot!"]),
 
            (r'\bhow are you\b',
             ["I'm just a program, but I'm running smoothly! How about you?",
              "Doing great, thanks for asking!"]),
 
            (r'\b(what.?s the time|current time)\b', self._tell_time),
 
            (r'\b(what.?s the date|today.?s date)\b', self._tell_date),
 
            (r'\bhelp\b',
             ["I can chat about greetings, tell you the time/date, "
              "do simple math like 'add 2 and 3', or just have a "
              "casual conversation. Try me!"]),
 
            (r'\badd (\-?\d+) and (\-?\d+)', self._add_numbers),
            (r'\bsubtract (\-?\d+) and (\-?\d+)', self._subtract_numbers),
            (r'\bmultiply (\-?\d+) and (\-?\d+)', self._multiply_numbers),
 
            (r'\b(thank you|thanks)\b',
             ["You're welcome!", "No problem at all!", "Anytime!"]),
 
            (r'\b(bye|goodbye|exit|quit)\b',
             ["Goodbye! Have a great day!", "See you later!"]),
 
            (r'\bjoke\b',
             ["Why don't scientists trust atoms? Because they make up everything!",
              "I told a chemistry joke... there was no reaction."]),
        ]
 
        # Fallback responses when nothing matches
        self.fallback_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting... tell me more.",
            "Sorry, I don't have a response for that yet.",
            "Can you elaborate on that?",
        ]
 
    # ---------- Helper / dynamic response functions ----------
 
    def _set_name(self, match):
        self.user_name = match.group(1).capitalize()
        return f"Nice to meet you, {self.user_name}!"
 
    def _tell_time(self, match=None):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
 
    def _tell_date(self, match=None):
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
 
    def _add_numbers(self, match):
        a, b = int(match.group(1)), int(match.group(2))
        return f"{a} + {b} = {a + b}"
 
    def _subtract_numbers(self, match):
        a, b = int(match.group(1)), int(match.group(2))
        return f"{a} - {b} = {a - b}"
 
    def _multiply_numbers(self, match):
        a, b = int(match.group(1)), int(match.group(2))
        return f"{a} * {b} = {a * b}"
 
    # ---------- Core matching logic ----------
 
    def get_response(self, user_input):
        text = user_input.lower().strip()
 
        for pattern, response in self.rules:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if callable(response):
                    return response(match)
                return random.choice(response)
 
        return random.choice(self.fallback_responses)
 
    # ---------- Chat loop ----------
 
    def start_chat(self):
        print(f"{self.name}: Hi! I'm {self.name}. Type 'quit' to exit.\n")
        while True:
            user_input = input("You: ")
            if not user_input.strip():
                continue
 
            if re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()):
                print(f"{self.name}: {random.choice(['Goodbye! Have a great day!', 'See you later!'])}")
                break
 
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")
 
 
if __name__ == "__main__":
    bot = RuleBasedChatbot(name="RuleBot")
    bot.start_chat()
