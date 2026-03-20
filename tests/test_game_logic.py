import pytest

# Only import when running with pytest
if __name__ != "__main__":
    from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests for parse_guess fixes
def test_parse_guess_empty():
    ok, guess, err = parse_guess("")
    assert not ok
    assert guess is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert not ok
    assert guess is None
    assert err == "Enter a guess."

def test_parse_guess_valid_int():
    ok, guess, err = parse_guess("42")
    assert ok
    assert guess == 42
    assert err is None

def test_parse_guess_float_string():
    # Previously allowed, now fails
    ok, guess, err = parse_guess("5.0")
    assert not ok
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_invalid():
    ok, guess, err = parse_guess("abc")
    assert not ok
    assert guess is None
    assert err == "That is not a number."


# Tests for update_score fixes
def test_update_score_win():
    new_score = update_score(50, "Win", 3)
    # max(100 - (3-1)*10, 10) = max(100-20,10)=80
    assert new_score == 50 + 80

def test_update_score_win_min():
    new_score = update_score(0, "Win", 15)
    # max(100 - (15-1)*10, 10) = max(100-140,10)=10
    assert new_score == 10

def test_update_score_too_high():
    # Previously rewarded, now no change
    new_score = update_score(50, "Too High", 2)
    assert new_score == 50

def test_update_score_too_low():
    # Previously penalized, now no change
    new_score = update_score(50, "Too Low", 1)
    assert new_score == 50


if __name__ == "__main__":
    # Run tests manually when executed directly
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

    tests = [
        test_winning_guess,
        test_guess_too_high,
        test_guess_too_low,
        test_parse_guess_empty,
        test_parse_guess_none,
        test_parse_guess_valid_int,
        test_parse_guess_float_string,
        test_parse_guess_invalid,
        test_update_score_win,
        test_update_score_win_min,
        test_update_score_too_high,
        test_update_score_too_low,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1

    # Test parametrized ones
    difficulties = [("Easy", (1, 100)), ("Medium", (1, 50)), ("Hard", (1, 20))]
    for diff, expected in difficulties:
        try:
            result = get_range_for_difficulty(diff)
            assert result == expected
            print(f"✓ test_difficulty_ranges_{diff}")
            passed += 1
        except Exception as e:
            print(f"✗ test_difficulty_ranges_{diff}: {e}")
            failed += 1

    # Test invalid difficulty
    try:
        get_range_for_difficulty("Impossible")
        print("✗ test_invalid_difficulty: Should have raised ValueError")
        failed += 1
    except ValueError:
        print("✓ test_invalid_difficulty")
        passed += 1
    except Exception as e:
        print(f"✗ test_invalid_difficulty: {e}")
        failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")
