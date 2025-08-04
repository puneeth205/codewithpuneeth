import google.generativeai as genai
import re
from calculator_tool import calculate

# Replace with your actual API key
genai.configure(api_key="your_real_gemini_api_key_here")

def is_math_question(prompt):
    math_keywords = ['add', 'plus', 'sum', 'subtract', 'minus', 'multiply', 'times', 'divide']
    has_keywords = any(word in prompt.lower() for word in math_keywords)
    has_symbols = bool(re.search(r'\d+\s*[\+\-\*/]\s*\d+', prompt))
    return has_keywords or has_symbols

def is_mixed_query(prompt):
    return ' and ' in prompt.lower() and is_math_question(prompt)

def extract_expression(prompt):
    # Replace math words with symbols
    prompt = prompt.lower()
    prompt = prompt.replace("plus", "+")
    prompt = prompt.replace("add", "+")
    prompt = prompt.replace("minus", "-")
    prompt = prompt.replace("subtract", "-")
    prompt = prompt.replace("times", "*")
    prompt = prompt.replace("multiply", "*")
    prompt = prompt.replace("divided by", "/")
    prompt = prompt.replace("divide", "/")

    # Extract the math expression
    expr = re.findall(r'[\d\.\+\-\*/]+', prompt)
    return ''.join(expr).strip()

def generate_llm_response(user_input):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            f"Answer step-by-step:\nUser: {user_input}\nAssistant:"
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini Error: {e}"

def main():
    print("🤖 Gemini Assistant + Calculator — Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        if is_mixed_query(user_input):
            print("\nAssistant: Sorry, I can only handle one type of task at a time.")
            continue

        if is_math_question(user_input):
            expr = extract_expression(user_input)
            result = calculate(expr)
            print(f"\nAssistant: {result}")
        else:
            response = generate_llm_response(user_input)
            print(f"\nAssistant:\n{response}")

if __name__ == "__main__":
    main()
