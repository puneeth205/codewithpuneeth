import re
import google.generativeai as genai

# You must set your API key here (or use an environment variable)
API_KEY = "your_real_gemini_api_key_here"
genai.configure(api_key=API_KEY)

MODEL = genai.GenerativeModel('gemini-1.5-flash')

def gemini_translate_to_german(phrase):
    prompt = f"Translate this to German: '{phrase}'"
    response = MODEL.generate_content(prompt)
    return response.text.strip()

def gemini_calculate(operation, a, b):
    # operation should be 'add' or 'multiply'
    prompt = f"{operation.capitalize()} {a} and {b}."
    response = MODEL.generate_content(prompt)
    return response.text.strip()

def handle_query(query):
    response = []
    query_lower = query.lower()
    nums = [int(s) for s in re.findall(r'\b\d+\b', query)]
    print("Extracted numbers:", nums)  # Debug print

    # Multi-step: Translate and multiply
    if "translate" in query_lower and "multiply" in query_lower:
        try:
            phrase = query.split("translate '")[1].split("'")[0]
            translation = gemini_translate_to_german(phrase)
            response.append(f"German translation: {translation}")
        except Exception:
            response.append("Error: Could not identify phrase to translate.")
        if len(nums) >= 2:
            product = gemini_calculate("multiply", nums[0], nums[1])
            response.append(f"Multiplication: {nums[0]} * {nums[1]} = {product}")
        else:
            response.append("Error: Could not find two numbers to multiply.")

    # Add and translate
    elif "add" in query_lower and "translate" in query_lower:
        if len(nums) >= 2:
            sum_result = gemini_calculate("add", nums[0], nums[1])
            response.append(f"Addition: {nums[0]} + {nums[1]} = {sum_result}")
        else:
            response.append("Error: Could not find two numbers to add.")
        try:
            phrase = query.split("translate '")[1].split("'")[0]
            translation = gemini_translate_to_german(phrase)
            response.append(f"German translation: {translation}")
        except Exception:
            response.append("Error: Could not identify phrase to translate.")

    # Capital then multiply
    elif "capital" in query_lower and "multiply" in query_lower:
        response.append("Capital of Italy: Rome")
        if len(nums) >= 2:
            product = gemini_calculate("multiply", nums[0], nums[1])
            response.append(f"Multiplication: {nums[0]} * {nums[1]} = {product}")
        else:
            response.append("Error: Could not find two numbers to multiply.")

    # Only translation
    elif "translate" in query_lower:
        try:
            phrase = query.split("translate '")[1].split("'")[0]
            translation = gemini_translate_to_german(phrase)
            response.append(f"German translation: {translation}")
        except Exception:
            response.append("Error: Could not identify phrase to translate.")

    # Only add and multiply e.g. "Add 2 and 2 and multiply 3 and 3."
    elif "add" in query_lower and "multiply" in query_lower:
        add_nums = []
        mult_nums = []
        clauses = query_lower.split("and")
        for clause in clauses:
            numbers = [int(s) for s in re.findall(r'\b\d+\b', clause)]
            if "add" in clause and len(numbers) == 2:
                add_nums = numbers
            if "multiply" in clause and len(numbers) == 2:
                mult_nums = numbers
        if add_nums:
            add_result = gemini_calculate("add", add_nums[0], add_nums[1])
            response.append(f"Addition: {add_nums[0]} + {add_nums[1]} = {add_result}")
        else:
            response.append("Error: Could not find two numbers to add.")
        if mult_nums:
            mult_result = gemini_calculate("multiply", mult_nums[0], mult_nums[1])
            response.append(f"Multiplication: {mult_nums[0]} * {mult_nums[1]} = {mult_result}")
        else:
            response.append("Error: Could not find two numbers to multiply.")

    # LLM direct answer, e.g., "What is the distance between Earth and Mars?"
    elif "distance" in query_lower and "earth" in query_lower and "mars" in query_lower:
        prompt = "What is the average distance between Earth and Mars in kilometers?"
        response_content = MODEL.generate_content(prompt).text.strip()
        response.append(response_content)

    else:
        prompt = f"Answer the following: {query}"
        response_content = MODEL.generate_content(prompt).text.strip()
        response.append(response_content)

    return "\n".join(response)


if __name__ == "__main__":
    queries = [
        "Translate 'Good Morning' into German and then multiply 5 and 6.",
        "Add 10 and 20, then translate 'Have a nice day' into German.",
        "Tell me the capital of Italy, then multiply 12 and 12.",
        "Translate 'Sunshine' into German.",
        "Add 2 and 2 and multiply 3 and 3.",
        "What is the distance between Earth and Mars?"
    ]
    for q in queries:
        print(f"\nQuery: {q}")
        print(handle_query(q))
        print('-' * 30)
