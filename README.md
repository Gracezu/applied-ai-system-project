# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.


## 🕵️‍♂️ Your Mission
1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

1. Original Project Context
The original "Glitchy Guesser" was a Streamlit-based number guessing game designed to teach debugging skills. Its primary goal was to provide a broken environment where users could find and fix common logic errors, such as state management bugs (where the secret number resets) and reversed mathematical comparisons.

2. Title and Summary
Project: Agentic Game Investigator
This project transforms a simple, bug-prone guessing game into a resilient app using an Agentic Workflow. It matters because it demonstrates how to integrate "self-healing" logic and automated validation layers within a Python application, ensuring that AI-generated code remains reliable and production-ready.

3. Architecture Overview
The system is built on a Supervisor-Validator model.

User Interface (Streamlit): Captures user inputs and displays game states.

Agent Controller: Acts as the middleman, passing inputs to the utility functions and checking for anomalies.

Logic Engine (logic_utils.py): Contains the core mathematical and parsing operations.

Automated Tester (test_game_logic.py): A suite of unit tests that the system uses to verify logic integrity.

4. Setup Instructions 🛠️
To run the project locally, follow these steps
Clone the Repository: Ensure app.py, logic_utils.py, and test_game_logic.py are in the same folder.

Install Dependencies-
`pip install -r requirements.txt`
`pip install streamlit pytest`

Before starting the app, verify the logic
`pytest test_game_logic.py`

Launch the App:
`python -m streamlit run app.py`


5. Sample Interactions
User Input	AI Internal Processing	Resulting Output
Guess: "abc"	parse_guess catches ValueError.	Error: "That is not a number."
Guess: 50 (Secret: 50)	check_guess returns "Win".	🎉 Success: "You won! The secret was 50."
Guess: 60 (Secret: 20)	check_guess evaluates 60 > 20.	Hint: "Too high! Try again."

6. Design Decisions
I moved all game logic into logic_utils.py. This requires more files, but it allows for independent testing without running the Streamlit server. I used st.session_state to store the secret number. This prevents the "Commitment Issues" bug where the number reset on every click. The system now rejects floats (e.g., "5.0") in parse_guess to ensure integer-only comparisons, preventing subtle math errors.



