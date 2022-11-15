def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    return None  # we will be changing this later.


def test() -> None:
    "Test cases for the functions in Poker program"
    sf = "6C 7C 8C 9C TC".split()  # ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fh, fk]) == fk
    assert poker([fh, fh]) == fh

    # Border cases
    assert poker([sf]) == sf
    assert poker([sf for i in range(100)]) == sf

    print("tests pass")


if __name__ == "__main__":
    test()
