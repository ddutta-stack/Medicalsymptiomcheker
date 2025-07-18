#Symptom checker UI based implementation using Gradio.
# This code provides a user interface for the symptom checker using Gradio.
# It allows users to input their symptoms and receive a possible condition based on those symptoms.
import gradio as gr
import requests
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
# create the gradio interface
interface = gr.Interface(
    fn=check_symptoms,
    inputs=gr.Textbox(lines=2,placeholder="Enter about your symptoms",label="Enter your symptoms (comma separated)"),
    outputs=gr.Textbox(lines=2,label="Possible Condition"),
    title="Symptom Checker",
    description="Enter your symptoms to get a possible condition as suggested by AI.")  
# launch the interface to support user interaction using the UI
if __name__ == "__main__":
    interface.launch()