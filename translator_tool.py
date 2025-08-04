# translator_tool.py

def translate_to_german(phrase):
    # Simple dictionary for demo. Extend as needed.
    dictionary = {
        "Good Morning": "Guten Morgen",
        "Have a nice day": "Einen schönen Tag noch",
        "Sunshine": "Sonnenschein"
    }
    return dictionary.get(phrase, f"[No German translation for '{phrase}']")
    