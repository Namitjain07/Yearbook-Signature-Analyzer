yearbook = {}
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if ':' in line:
            curr_name = line.split(':')[0]
            yearbook[curr_name] = {}
        else:
            other_name, status = line.split(',')
            yearbook[curr_name][other_name] = int(status)

max_count = 0
max_names = []
min_count = None
min_names = []
for name in yearbook:
    count = sum(yearbook[name].values())
    if min_count is None:
        min_count = count
    if count > max_count:
        max_count = count
        max_names = [name]
    elif count == max_count:
        max_names.append(name)
    if count < min_count:
        min_count = count
        min_names = [name]
    elif count == min_count:
        min_names.append(name)

with open('output.txt', 'w') as f:
    f.write('Most signatures:')
    for name in max_names:
        f.write(name + ', ')
    f.write('\nLeast signatures:')
    for name in min_names:
        f.write(name + ', ')
