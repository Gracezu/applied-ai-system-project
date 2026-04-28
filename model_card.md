1. Testing and Reliability
To ensure the AI's behavior is predictable, I implemented automated tests covering edge cases like empty strings, invalid difficulties, and boundary-point scoring. The system records ValueError incidents during input parsing to track user behavior patterns. I manually verified that the "New Game" button properly resets all session_state variables, preventing "zombie" game states.

2. Reflection
This project taught me that AI is a powerful but imperfect collaborator. While tools like Copilot are excellent for refactoring, they can easily introduce "silent bugs" like reversed logic or incorrect return types (e.g., returning a string when a tuple is expected). The real skill in modern development is not just writing code, but building the testing infrastructure to catch the AI when it slips.

## Limitations and Biases

The current system relies heavily on predefined logic in logic_utils.py, which means it lacks true "intelligence" to adapt to unforeseen user behaviors. A primary bias exists in the difficulty scaling; the "Hard" mode is significantly more restrictive (1-20 range, 5 attempts) than "Easy" (1-100 range, 6 attempts), which may not align with all players' perceptions of fair play or skill progression. Furthermore, the system assumes all users can read and interpret English text and standard numerical digits, excluding those with different linguistic needs or accessibility requirements.

## Collaboration

The AI recommended refactoring all core game logic (like check_guess and parse_guess) into a dedicated logic_utils.py file. This made the codebase modular, allowed for cleaner pytest implementation, and simplified the main app.py script.