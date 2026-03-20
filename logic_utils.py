def get_range_for_difficulty(difficulty: str):
# FIX: Standardized difficulty ranges (Easy: 1-100, Medium: 1-50, Hard: 1-20)
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 100),
        "Medium": (1, 50),
        "Hard": (1, 20),
    }
    if difficulty not in ranges:
        raise ValueError(f"Invalid difficulty: {difficulty}")
    return ranges[difficulty]


def parse_guess(raw: str):
# FIX: Simplified parse logic to prevent crashes on invalid input
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."
    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."
    return True, value, None

# FIX: Refactored logic functions out of app.py using Copilot Agent mode
def check_guess(guess, secret):
# FIX: Corrected high/low logic (was reversed and misleading in original code)
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "Too high! Try again."
    else:
        return "Too Low", "Too low! Try again."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(100 - (attempt_number - 1) * 10, 10)
        return current_score + points
    return current_score
