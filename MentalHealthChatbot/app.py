from flask import Flask, render_template, request, jsonify
from fuzzywuzzy import process
import re
import logging
import wikipedia
from training_data import qa_pairs  # Importing questions and answers
from synonyms import SYNONYMS  # Importing synonyms
from response_generator import dynamic_response  # Import the dynamic response
import datetime

app = Flask(__name__)

# Configure logging for more detailed output
logging.basicConfig(level=logging.DEBUG)

# Configurable fuzzy matching threshold
FUZZY_MATCH_THRESHOLD = 80

# Route for the chat page (Frontend)
@app.route('/')
def chat():
    return render_template('index.html')

def normalize_message(message):
    """ Normalize the user message by converting to lowercase and stripping spaces. """
    message = re.sub(r'[^\w\s]', '', message)  # Remove punctuation
    return message.strip().lower()

def expand_keywords(user_message):
    """ Expand user message to include synonyms for better matching. """
    words = user_message.split()
    expanded_message = []

    for word in words:
        # Check for synonyms and replace with the main keyword
        expanded_word = next((key for key, synonyms in SYNONYMS.items() if word in synonyms), word)
        expanded_message.append(expanded_word)

    return ' '.join(expanded_message)

def keyword_match(user_message):
    """ Check for direct keyword matches in the user message after expanding synonyms. """
    expanded_message = expand_keywords(user_message)
    
    # Use regex for better keyword matching
    for key in qa_pairs.keys():
        if re.search(r'\b' + re.escape(key.lower()) + r'\b', expanded_message):
            logging.info(f"Exact keyword match found for '{key}'")
            return qa_pairs[key]
    return None

def fuzzy_match(user_message):
    """ Perform fuzzy matching to find the closest question with higher accuracy. """
    expanded_message = expand_keywords(user_message)
    closest_match = process.extractOne(expanded_message, qa_pairs.keys(), score_cutoff=FUZZY_MATCH_THRESHOLD)
    
    if closest_match:
        logging.info(f"Fuzzy match found: {closest_match[0]} with score {closest_match[1]}")
        return qa_pairs[closest_match[0]]
    return None

def search_wikipedia(user_message):
    """ Search for the topic on Wikipedia and return the summary. """
    try:
        summary = wikipedia.summary(user_message, sentences=2)
        return summary
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
        logging.error(f"Wikipedia error: {e}")
        return None
    except Exception as e:
        logging.error(f"Error occurred while searching Wikipedia: {e}")
        return None

def get_time_based_greeting():
    """ Provide a greeting based on the current time. """
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def get_response(user_message):
    """ Get response based on various matching strategies. """
    user_message = normalize_message(user_message)

    # Step 1: Check for greeting keywords
    if any(greeting in user_message for greeting in ["hello", "hi", "hey", "greetings"]):
        time_greeting = get_time_based_greeting()
        return f"{time_greeting} I’m here to help, but it seems like I didn’t quite catch what you’re feeling. If you’d like, you can tell me more about your situation or ask me something else, and I’ll do my best to support you!"

    # Step 2: Check for exact keyword matches
    response = keyword_match(user_message)
    if response:
        logging.info(f"Response from keyword match: {response}")
        return response

    # Step 3: Check for fuzzy matches
    response = fuzzy_match(user_message)
    if response:
        logging.info(f"Response from fuzzy match: {response}")
        return response

    # Step 4: Try searching Wikipedia
    wikipedia_response = search_wikipedia(user_message)
    if wikipedia_response:
        logging.info(f"Response from Wikipedia: {wikipedia_response}")
        return wikipedia_response

    # Step 5: Generate a dynamic response if no matches found
    dynamic_resp = dynamic_response(user_message)
    logging.info(f"Response from dynamic generator: {dynamic_resp}")
    return dynamic_resp

# Route to handle chatbot responses
@app.route('/chat', methods=['POST'])
def chat_response():
    try:
        user_message = request.json['message']
        response = get_response(user_message)
        return jsonify(reply=response)
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify(reply="An error occurred while processing your request."), 500

if __name__ == '__main__':
    app.run(debug=True)
