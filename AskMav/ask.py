import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Hello|Hi",
        ["Hello. My name is Juan Tristan and I am an IT Strategist. You can ask me questions about my skills and I will respond."]
    ],
    [
        r"What are chatbots used for?",
        ["Chatbots are used for a wide range of purposes, including customer service, marketing, sales, and support. They can also be used for personal assistants, virtual therapists, and other applications."]
    ],
    [
        r"How do chatbots work?",
        ["Chatbots use natural language processing and machine learning algorithms to analyze user input and generate responses."]
    ],
    [
        r"Can chatbots understand multiple languages?",
        ["Yes, some chatbots are designed to understand and respond in multiple languages."]
    ],
    [
        r"How can I create a chatbot?",
        ["You can create a chatbot using programming languages like Python, and NLP libraries like NLTK and spaCy. There are also chatbot development platforms that provide drag-and-drop interfaces and pre-built templates."]
    ],
    [
        r"Thank you|Thanks",
        ["You're welcome!"]
    ],
    [
        r"Bye|Goodbye",
        ["Goodbye, have a nice day!"]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
