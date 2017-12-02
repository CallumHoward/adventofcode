import re

total_count = 0
escaped_count = 0
new_count = 0

with open('08.txt') as f:
    for line in f.readlines():
        total_count += len(line.rstrip())
        escaped_count += len(re.findall(r'\\\\|\\x[0-9a-f]{2}|\\"|[a-z]', line))

        new_count += 6
        new_count += sum(4 for match in re.findall(r'\\\\', line))
        line = re.sub(r'\\\\', '', line)
        new_count += sum(5 for match in re.findall(r'\\x[0-9a-f]{2}', line))
        line = re.sub(r'\\x[0-9a-f]{2}', '', line)
        new_count += sum(4 for match in re.findall(r'\\"', line))
        line = re.sub(r'\\"', '', line)
        new_count += sum(1 for match in re.findall(r'[a-z]', line))
        line = re.sub(r'[a-z]', '', line)


print total_count - escaped_count
print new_count - total_count
