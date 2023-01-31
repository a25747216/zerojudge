lines = []
while True:
    try:
        lines.insert(0, input())
    except EOFError:
        break

max_len = max( map(len, lines))
out_lines = ["" for i in range(max_len)]

for line in lines:
    for c, char in enumerate(line):
        out_lines[c] += char
    if line != lines[len(lines) - 1]:
        for c in range(len(line), max_len):
            out_lines[c] += " "
    else:
        for c in range(len(line), max_len):
            out_lines[c] += ""

print("\n".join(map(str, out_lines)))