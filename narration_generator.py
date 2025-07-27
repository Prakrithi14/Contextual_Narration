import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyCv-0Uz5PpIXfSQJsXJLzx7kWiFwLyI_d0")

def generate_narration(occasion, topic,length):
    prompt = f"Write a beautiful, context-aware narration for the occasion '{occasion}' of topic '{topic}' with {length}."

    # Create the model instance
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Generate content
    response = model.generate_content(prompt)

    return response.text
