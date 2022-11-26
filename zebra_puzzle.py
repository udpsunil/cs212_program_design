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
11. The man who smokes Chesterfields lives in the house next to the man with the fox
12. Kools are smoked in a house next to the house where horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments
15. The Norwegian lives next to the blue house

Who drinks water? Who owns the Zebra

Analysis: Houses are present
Properties -> Nationality, Colors, Pets, Drinks, Smokes
Assignments -> Locations, next to, immediate right, first middle etc.
"""
# First version - Brute Force
import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

for (red, green, ivory, yellow, blue) in orderings:
    for (englishman, spaniard, ukrainian, japanese, norwegian) in orderings:
        for (dog, snails, fox, horse, zebra) in orderings:
            for (coffee, tea, milk, oj, water) in orderings:
                for (oldgold, kools, chesterfields, luckystrike, parliaments) in orderings:
                    if englishman == red:
                        pass