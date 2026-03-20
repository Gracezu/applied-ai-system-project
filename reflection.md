# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
There are so many glitches when I try it the first time. 

- List at least two concrete bugs you noticed at the start  
1. The difficulty level is not working. Eventhough the easy level was chosen, it keeps showing the same as the difficult question.
2. The "New Game" button is not working. 
3. The "Show hint" doesn't help to guess the correct answer. It keeps showing "Go Higher" and "Go Lower" for a smaller and larger number (Eg., 7 and 8).
4. The difficulty level is wrong. It should be 1-100 for Easy, 1-50 for Normal and 1-20 for Hard.
5. The "Message to make a guess" doesn't show correctly.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result)

I used Copilot Agent mode to refactor and debug my code.
One correct AI suggestion was to move all game logic functions (like check_guess and parse_guess) into a separate logic_utils.py file. This made the code cleaner and easier to test. I verified this by running the app after refactoring and confirming that the game still worked correctly and that pytest tests passed successfully.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One incorrect or misleading AI suggestion was related to the check_guess function return value. Initially, the AI suggested returning only a string like "Too High", but my actual function returned a tuple (outcome, message). I verified this by running pytest and noticing test failures, then fixed the test cases to correctly unpack the tuple.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by both running the Streamlit app and checking if the behavior matched expectations, and by running pytest to confirm the logic worked correctly.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
One test I ran was checking if a guess of 60 against a secret of 50 returns "Too High". This confirmed that the logic in check_guess was working properly and no longer reversed.

- Did AI help you design or understand any tests? How?
AI helped me understand that I needed to test both the outcome and the message, and also helped me fix my test cases by unpacking the returned tuple correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because Streamlit reruns the entire script every time the user interacts with the app, which caused the random number to reset.


- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns mean that the whole script executes again on every interaction, but session state allows us to store variables so they persist across reruns. I would explain it like: “Streamlit refreshes the app every time you click something, but session state is like memory that keeps important values saved.”


- What change did you make that finally gave the game a stable secret number?
I fixed this by storing the secret number in st.session_state, so it only initializes once and doesn’t change every time the app reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? - This could be a testing habit, a prompting strategy, or a way you used Git. 
One habit I want to reuse is breaking problems into smaller parts and using testing to verify each fix instead of guessing.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would be more specific with my prompts when using AI, especially about function return types and expected behavior.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code is helpful but not always correct, so I need to carefully review, test, and understand the code instead of trusting it blindly.