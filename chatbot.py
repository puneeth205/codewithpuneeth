import google.generativeai as genai
import re

# Set your Gemini API key here (starts with AIza...)
genai.configure(api_key="your_real_gemini_api_key_here")  # Replace with your actual key

def is_math_question(prompt):
    return bool(re.search(r'\b(add|plus|sum|subtract|minus|multiply|divide|\d+\s*[\+\-\*/]\s*\d+)\b', prompt.lower()))

def generate_prompt(user_input):
    if is_math_question(user_input):
        return "I cannot solve math directly. Please use a calculator tool for accurate results."
    
    return (
        "You are a smart assistant. Always answer step-by-step in simple language.\n"
        f"User Question: {user_input}\n"
        "Answer:"
    )

def ask_gemini(user_input):
    prompt = generate_prompt(user_input)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

def main():
    print("🤖 Gemini Assistant — Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = ask_gemini(user_input)
        print(f"\nAssistant:\n{response}")

if __name__ == "__main__":
    main()
