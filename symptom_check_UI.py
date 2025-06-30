#Symptom checker UI based implementation using Gradio.
# This code provides a user interface for the symptom checker using Gradio.
# It allows users to input their symptoms and receive a possible condition based on those symptoms.
import gradio as gr
import random
ollamaurl = "http://localhost:11434/api/generate"

