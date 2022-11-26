"""
Documentation:
See http://en.wikipedia.org/wiki/Zebra_Puzzle
1. There are 5 houses
2. The Englishman lives in the red house
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.
9. Milk is drunk in the middle house
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to man with fox
12. Kools are smoked in a house next to the house where horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments
15. The Norwegian lives next to the blue house

Who drinks water? Who owns the Zebra

Analysis: Houses are present
Properties -> Nationality, Colors, Pets, Drinks, Smokes
Assignments -> Locations, next to, immediate right, first middle etc.
"""
# First version - Brute Force using generator expressions
import itertools


def zebra_puzzle():
    """Return a tuple (WATER, ZEBRA) indicating their house numbers."""

    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next(
        (WATER, ZEBRA)
        for (red, green, ivory, yellow, blue) in orderings
        for (englishman, spaniard, ukrainian, japanese, norwegian) in orderings
        for (dog, snails, fox, horse, ZEBRA) in orderings
        for (coffee, tea, milk, oj, WATER) in orderings
        for (oldgold, kools, chesterfields, luckystrike, parliaments) in orderings
        if englishman is red
        if spaniard is dog
        if coffee is green
        if ukrainian is tea
        if is_right_of(green, ivory)
        if oldgold is snails
        if kools is yellow
        if milk == middle
        if norwegian == first
        if is_next_to(chesterfields, fox)
        if is_next_to(kools, horse)
        if luckystrike is oj
        if japanese is parliaments
        if is_next_to(norwegian, blue)
    )


def is_right_of(h1, h2):
    """House h1 is immediately right of h2 if h1 - h2 == 1."""
    return h1 - h2 == 1


def is_next_to(h1, h2):
    """Two houses are next to each other if they differ by 1."""
    return abs(h1 - h2) == 1


print(zebra_puzzle())
