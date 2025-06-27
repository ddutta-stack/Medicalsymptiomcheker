# Symtom checker for a simple medical application. This is a basic implementation using console input.
import requests
# Start
ollamaurl = "http://localhost:11434/api/generate"

def check_symptoms(symptoms):
    """
    Check the provided symptoms and return a possible condition.
    
    Args:
        symptoms (list): A list of symptoms provided by the user.
        
    Returns:
        str: A possible condition based on the symptoms.
    """
    prompt = f'Given the symptoms: what could be a possible condition?'
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }