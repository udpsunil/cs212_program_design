# Lesson 1 : Section 15

def poker(hands):
    """Return the best hand: poker([hand,...]) => hand"""
    return max(hands, key=hand_rank)


def card_ranks(hand) -> list:
    """returns an ORDERED tuple of the ranks
    in a hand (where the order goes from
    highest to lowest rank)"""
    rank_mapping = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
    ranks = [r for r, s in hand]
    for r in ranks:
        if r in rank_mapping:
            index = ranks.index(r)
            ranks[index] = rank_mapping[r]
    ranks = [int(r) for r in ranks]
    ranks.sort(reverse=True)
    return ranks


def straight(ranks) -> int:
    """returns True if the hand is a straight"""
    return ranks == list(range(ranks[0], ranks[0] - 5, -1))


def flush(hand) -> bool:
    """returns True if the hand is a flush"""
    return len({s for r, s in hand}) == 1


def kind(no_of_items, ranks) -> any:
    """returns the first rank that the hand has
    exactly n of. For A hand with 4 sevens
    this function would return 7"""
    return next((r for r in ranks if ranks.count(r) == no_of_items), None)


def two_pair(ranks):
    """if there is a two pair, this function
    returns their corresponding ranks as a
    tuple. For example, a hand with 2 twos
    and 2 fours would cause this function
    to return (4, 2)"""
    pair = [kind(2, r) for r in set(ranks)]
    return sorted(pair)


def hand_rank(hand):
    """Return a value indicating the rank of a hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return 8, max(ranks)
    elif kind(4, ranks):  # 4 of a kind
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):  # flush
        return 5, card_ranks(hand)
    elif straight(ranks):  # straight
        return 4, card_ranks(hand)
    elif kind(3, ranks):  # 3 of a kind
        return 3, kind(3, ranks), card_ranks(hand)
    elif two_pair(ranks):  # 2 pair
        return 2, kind(2, ranks)
    elif kind(2, ranks):  # kind
        return 1, kind(2, ranks), card_ranks(hand)
    else:  # high card
        return 0, card_ranks(hand)


def test() -> None:
    """Test cases for the functions in Poker program"""
    sf = "6C 7C 8C 9C TC".split()  # ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fh, fk]) == fk
    assert poker([fh, fh]) == fh

    # Border cases
    assert poker([sf]) == sf
    assert poker([sf for _ in range(100)]) == sf

    # hand_rank tests
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    # card_ranks tests
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    print("tests pass")


if __name__ == "__main__":
    test()
