import pulp

# Define data
courses = ['A', 'B', 'C', 'D', 'E']
time_slots = [1, 2, 3]
overlap = {
    ('A', 'B'): 10,
    ('A', 'C'): 5,
    ('B', 'D'): 8,
    ('C', 'E'): 7,
    ('D', 'E'): 3
}

# Initialize the problem
prob = pulp.LpProblem("Course_Scheduling", pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", ((c, t) for c in courses for t in time_slots), cat='Binary')

# Define auxiliary variables to capture overlap in the same time slot
z = pulp.LpVariable.dicts("z", overlap.keys(), lowBound=0, cat='Continuous')

# Objective function: minimize overlaps in the same time slot
prob += pulp.lpSum(overlap[(c1, c2)] * z[(c1, c2)] for (c1, c2) in overlap)

# Constraints: Each course is scheduled exactly once
for c in courses:
    prob += pulp.lpSum(x[c, t] for t in time_slots) == 1

# Constraints: Capture overlap in the same time slot
for (c1, c2) in overlap:
    for t in time_slots:
        prob += z[(c1, c2)] >= x[c1, t] + x[c2, t] - 1

# Solve the problem
prob.solve()

# Output the results
print(f"Status: {pulp.LpStatus[prob.status]}")
for c in courses:
    for t in time_slots:
        if pulp.value(x[c, t]) == 1:
            print(f"Course {c} is scheduled in time slot {t}")
