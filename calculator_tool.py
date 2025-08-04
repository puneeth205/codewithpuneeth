def calculate(expression):
    try:
        result = eval(expression)
        return f"🧮 Result: {result}"
    except Exception:
        return "❌ Could not understand the math expression."