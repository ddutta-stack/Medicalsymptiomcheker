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
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(ollamaurl, json=payload)
    if response.status_code == 200:
        return response.json().get('response', 'No condition found.')
    else:
        return f"Error: {response.status_code} - {response.text}"
    
    # Test the symptom checker
if __name__ == "__main__":
    test_symptoms= ("fever", "cough", "sore throat")
    print("Welcome to the Symptom Checker!")
    print(check_symptoms(test_symptoms))