a = 'text text text'

b = 1

for c in a:
    if c == ' ':
        b = b + 1
    else:
        continue

print(b)
