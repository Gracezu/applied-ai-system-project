@pytest.mark.parametrize("difficulty, expected_range", [
    ("Easy", (1, 100)),
    ("Medium", (1, 50)),
    ("Hard", (1, 20)),
])
def test_difficulty_ranges(difficulty, expected_range):
    assert get_range_for_difficulty(difficulty) == expected_range


def test_invalid_difficulty():
    with pytest.raises(ValueError):
        get_range_for_difficulty("Impossible")