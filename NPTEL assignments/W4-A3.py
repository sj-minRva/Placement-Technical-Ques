#Week 4 - assignment - 3

"""
In the year 2525, the Galactic Registry maintains records of citizens from various planets.
Each citizen is registered with:

A name, and

A birthdate, represented by a number from 1 to 365, indicating the day of the year they
were born.

The Interstellar Census Department is looking to identify "Birthday Twins" — citizens who
share the same day of birth.

Input:
The function will take the following two inputs:

A string of comma-separated names (e.g., "alice,bob,charlie"),

A string of comma-separated integers (each from 1 to 365), representing the birthdates
corresponding to the names above.

Task:
Identify all unique pairs of names where both individuals share the same birthday.

For each such pair, create a list in the form: [name1, name2], where name1 comes before
name2 alphabetically.

Store all such pairs in a list called common.

Notes:
Only the order within each pair matters — the overall order of pairs in common is not
important.

You can assume that at least one birthday twin pair will exist in any test case.
"""

names = input().strip().split(',')
dates = list(map(int, input().strip().split(',')))

birthday_map = {}
for name, date in zip(names, dates):
    birthday_map.setdefault(date, []).append(name)

common = []
for name_list in birthday_map.values():
    if len(name_list) > 1:
        name_list.sort()  # alphabetical order
        for i in range(len(name_list) - 1):
            for j in range(i + 1, len(name_list)):
                common.append([name_list[i], name_list[j]])

# Sort pairs globally
common.sort(key=lambda p: (p[0], p[1]))

# Print results
for a, b in common:
    print(f"{a},{b}")









