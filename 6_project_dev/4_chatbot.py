"""
types of chatbot:
rule based
ai powered
hybrid
specialized

working:
User → Interface → NLP Engine → Dialogue Manager → Backend/Logic → Response Generator → User


Python libraries like spayCy, NLTK, ChatterBot, Rasa, and LangChain, highlighting their suitability for various chatbot applications.

ChatterBot is a library designed for building chatbots that can engage in conversations.

Rasa is a more robust framework that provides greater flexibility and control over your chatbot's behavior. It's a sophisticated AI engine that can power highly interactive and intelligent conversations. It uses Natural Language Understanding (NLU) and Dialogue Management (DM) to create more dynamic and engaging conversations.

spacy pipeline:
- tokenization
- part of speech tagging
- named entity recognition
"""

import spacy

# command to download model: python3 -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


def get_intent(doc):
    """Analyze the doc to find the user's primary intent."""
    # Use lemmatization to catch variations of words
    lemmas = [token.lemma_.lower() for token in doc]

    if any(greet in lemmas for greet in ["hello", "hi", "greetings", "hey"]):
        return "greeting"

    # Check for specific patterns: "How are you"
    if "how" in lemmas and "be" in lemmas and "you" in lemmas:
        return "status_check"

    # Identify if they are asking about a specific person/place (Named Entity Recognition)
    if doc.ents:
        return "entity_query"

    return "unknown"


def respond_to_user(user_input):
    doc = nlp(user_input)
    intent = get_intent(doc)

    # Handle Greetings
    if intent == "greeting":
        return "Hello! I noticed you're feeling chatty today."

    # Handle "How are you"
    elif intent == "status_check":
        return "My CPU is cool and my code is clean. How are you?"

    # Handle Entities (The "Smart" part)
    elif intent == "entity_query":
        entity = doc.ents[0]
        return f"I see you mentioned {entity.text} ({entity.label_}). What about it?"

    # Fallback: Parse the sentence structure
    else:
        # Find the root verb of the sentence
        root_verb = [token.lemma_ for token in doc if token.head == token][0]
        return f"I'm not sure I understand, but it sounds like you're talking about '{root_verb}'."


# Main Loop
print("Chatbot initialized. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = respond_to_user(user_input)
    print(f"Chatbot: {response}")
