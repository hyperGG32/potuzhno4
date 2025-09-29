"""
Task 9 — Music Festival Ticket Analyzer (No dicts, No functions) 🎤

Constraints: lists + loops + conditions + strings + numbers only (NO dicts, NO def). о яка вєсєлуха ну і правильно а то привикнем до лібів і пайтона в цілому а потім почнеться сішка і всі афігєють

Scenario:
  Entrance logs are noisy strings with three data points:
    - Ticket ID starting with 'T' + digits (e.g., T123)
    - Age (e.g., age=21, AGE:17)
    - Zone name containing 'zone' (zoneA, ZONE_B, ZONE_C)

Example logs:
  logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
  ]

Requirements:
  1) Extract for each line:
     - ticket id (string starting with 'T' + digits)
     - age (int)
     - zone label ('A', 'B', 'C') derived from zone token (case-insensitive)
     Ignore lines missing any of these three fields.

  2) Compute and print:
     - Valid tickets count
     - Minors (<18) count
     - Average age (1 decimal)
     - Zone counts as: A=?, B=?, C=?
     - Duplicates list (IDs that appear more than once)

Practice: string normalization, token scanning, counters, averages, duplicate detection

OUTPUT EXAMPLE
--------------
Valid tickets: 5
Minors: 2
Average age: 21.2
Zone counts: A=2, B=2, C=1
Duplicates: T045
"""

logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
]

print("(Starter) Logs loaded:", len(logs))

totalT = 0
ticketids = []
ages = []
zones = []
dublicateids = []
skip = False
for line in logs:
    line = line.split()
    skip = False
    for elem in line:
        if skip:
            continue
        if elem.split("T")[-1].isnumeric():
            if not "T" + elem.split("T")[-1] in ticketids:
                totalT += 1
                ticketids.append("T" + elem.split("T")[-1])
            else:
                dublicateids.append("T" + elem.split("T")[-1])
                skip = True
                continue
        if elem.lower().find("age") != -1:
            ages.append(int(elem.lower().split("age")[-1].strip(' =:')))
        if elem.lower().find("zone") != -1:
            zones.append(elem.lower().split("zone")[-1].strip(' _-'))

print("Valid tickets:", totalT)
print("Minors:", len([age for age in ages if age < 18]))
print("Average age:", round(sum(ages)/len(ages), 1))
print(f"Zone counts: A={zones.count('a')}, B={zones.count('b')}, C={zones.count('c')}")
print("Dublicates:", end=' ')
for dub in dublicateids:
    if dub != dublicateids[-1]:
        print(dub, end=', ')
    else:
        print(dub)
# вродь все робе але цикл страшний