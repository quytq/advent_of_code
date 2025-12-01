import re
words = []
with open ('input.txt') as f:
    words = [l.strip() for l in f]

def get_next(start, direction, step):
    next_pos = 0
    step = step % 100
    if direction == 'L':
        next_pos = start - step
        if next_pos < 0:
            next_pos = 100 + next_pos
    if direction == 'R':
        next_pos = start + step
        if next_pos >= 100:
            next_pos = next_pos%100
    return next_pos
    


r = re.compile("([a-zA-Z]+)([0-9]+)")
start = 50
direction = ''
step = 0
password = 0
for w in words:
    print(w)
    m = r.match(w)
    direction = m.group(1)
    step = int(m.group(2))
    start = get_next(start, direction, step)
    print(start)
    if start == 0:
        password = password+1


print(password)
