def has_run_of_three(s):
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == b == c:
            return True

solutions = []
for ampm in ['AM', 'PM']:
    for hour in range(1, 12+1):
        for minute in range(0, 60):
            time_string = f'{hour:02}:{minute:02} {ampm}'
            if has_run_of_three(time_string.replace(':', '')):
                solutions.append(time_string)

for sol in solutions:
    print(sol)

print()
print(len(solutions))
