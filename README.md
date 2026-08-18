# 🤖 Rule-Based Chatbot

## 📌 Task 1: Chatbot with Rule-Based Responses

This project is a simple **rule-based chatbot** developed in Python. It uses **regular expressions (regex), pattern matching, and if-else logic** to recognize the user's input and provide an appropriate response.

The chatbot can perform basic conversations, tell the current date and time, remember the user's name, perform simple mathematical operations, tell jokes, and respond to common greetings.

 
## 🎯 Objective

The main objective of this project is to understand how a basic chatbot works using:

* Pattern matching
* Regular expressions (Regex)
* If-else logic
* Functions
* Classes and objects
* Random responses
* Date and time functions
* User input handling



## 🛠️ Technologies Used

* Programming Language: Python
* Libraries:

  * `re` – Used for regular expression pattern matching
  * `random` – Used to select random responses
  * `datetime` – Used to display the current date and time



## ✨ Features

The chatbot supports the following commands and conversations:

### 👋 Greetings

The chatbot recognizes:


hi
hello
hey
greetings

Example:


You: hello
RuleBot: Hi! Nice to hear from you.

### 👤 Remember User Name

The user can introduce themselves:

```text
You: my name is Shubh
RuleBot: Nice to meet you, Shubh!
```

### 🤖 Chatbot Identity

The chatbot can answer questions such as:

```text
What's your name?
Who are you?
```

### 😊 How Are You

Example:

```text
You: how are you
RuleBot: Doing great, thanks for asking!
```

### 🕐 Current Time

The chatbot can provide the current time:

```text
You: what's the time
RuleBot: The current time is 18:30:25.
```

### 📅 Current Date

Example:

```text
You: today's date
RuleBot: Today's date is August 18, 2026.
```

### ➕ Addition

The chatbot can add two numbers:

```text
You: add 10 and 20
RuleBot: 10 + 20 = 30
```

### ➖ Subtraction

```text
You: subtract 20 and 5
RuleBot: 20 - 5 = 15
```

### ✖️ Multiplication

```text
You: multiply 5 and 4
RuleBot: 5 * 4 = 20
```

### 😂 Jokes

The chatbot can tell simple jokes when the user types:

```text
joke
```

### 🙏 Thank You

It recognizes:

```text
thank you
thanks
```

### 👋 Exit

The conversation can be ended by typing:

```text
quit
exit
bye
goodbye
```

---

## 🧠 How It Works

The chatbot follows a simple rule-based approach.

```text
User Input
     ↓
Convert Input to Lowercase
     ↓
Check Regex Patterns
     ↓
Pattern Matched?
   ↙        ↘
 Yes         No
 ↓            ↓
Response     Fallback
 ↓
Display Response
```

The chatbot stores its rules as **regular expression patterns** along with possible responses.

For example:

```python
(r'\b(hi|hello|hey|greetings)\b',
 ["Hello there! How can I help you today?",
  "Hi! Nice to hear from you."])
```

When the user enters a message, the chatbot checks whether the input matches any of these patterns.

---

## 📂 Project Structure

```text
Rule-Based-Chatbot/
│
├── chatbot.py
└── README.md
```

* `chatbot.py` – Main Python chatbot program
* `README.md` – Project documentation

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### 2. Save the Program

Save the provided code as:

```text
chatbot.py
```

### 3. Run the Program

Open the terminal in the project folder and run:

```bash
python chatbot.py
```

### 4. Start Chatting

You will see:

```text
RuleBot: Hi! I'm RuleBot. Type 'quit' to exit.

You:
```

Now enter your messages and interact with the chatbot.

---

## 💬 Sample Conversation

```text
RuleBot: Hi! I'm RuleBot. Type 'quit' to exit.

You: hello
RuleBot: Hello there! How can I help you today?

You: my name is Shubh
RuleBot: Nice to meet you, Shubh!

You: what is the time
RuleBot: The current time is 18:25:10.

You: add 15 and 25
RuleBot: 15 + 25 = 40

You: tell me a joke
RuleBot: Why don't scientists trust atoms? Because they make up everything!

You: bye
RuleBot: Goodbye! Have a great day!
```

---

## 🔑 Python Concepts Used

### 1. Regular Expressions

The `re` module is used to identify patterns in user input.

```python
re.search(pattern, text, re.IGNORECASE)
```

### 2. Classes and Objects

The chatbot is implemented using a Python class:

```python
class RuleBasedChatbot:
```

### 3. Functions

Different functions are used for different tasks such as:

* Setting the user's name
* Telling the time
* Telling the date
* Addition
* Subtraction
* Multiplication

### 4. Random Responses

The `random` module selects different responses randomly.

```python
random.choice(response)
```

### 5. Date and Time

The `datetime` module provides the current date and time.

```python
datetime.now()
```

---

## ⚠️ Limitations

This chatbot is **rule-based**, so it does not understand language like an AI/LLM chatbot.

Its limitations include:

* It can only recognize predefined patterns.
* It cannot understand complex questions.
* It cannot learn new information automatically.
* Responses are limited to the rules programmed by the developer.
* Unexpected questions may result in fallback responses.

---

## 🚀 Future Improvements

The chatbot can be improved by adding:

* More conversation patterns
* Weather information
* More mathematical operations
* Web/API integration
* Database support
* Voice input and output
* Natural Language Processing (NLP)
* Machine Learning
* AI/LLM-based responses

---

## 👨‍💻 Author

**Shubh Chandore**

Computer Science & Engineering Student

---

## 📜 License

This project is created for **educational purposes** as part of a chatbot programming task.

