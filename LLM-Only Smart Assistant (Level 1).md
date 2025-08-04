 LLM-Only Smart Assistant (Level 1)

Description
This is a Python CLI chatbot that uses prompt engineering to:
- Think step-by-step
- Format answers clearly
- Refuse direct math calculations and redirect to a calculator tool

 Features
- Uses Gemini  model
- Step-by-step logical responses
- Clear output formatting
- Handles factual, reasoning, and restricted math queries

 How to Run
1. Install dependencies:
    ```bash
    pip install google-generativeai

    ```

2. Set your Gemini API key in `chatbot.py`.

3. Run the program:
    ```bash
    python chatbot.py
    ```

 Sample Questions
- What are the colors in a rainbow?
- Tell me why the sky is blue?
- Which planet is the hottest?
- What is 15 + 23?

 Output Style
Each answer is broken into logical steps with a **Final Answer** at the end.
