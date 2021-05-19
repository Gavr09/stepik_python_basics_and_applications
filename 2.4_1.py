lines = []
with open('test_2.4_1/dataset_24465_4.txt') as inp:
    for line in inp:
        lines.append(line)

with open('test_2.4_1/output.txt', 'w') as out:
    for line in lines[::-1]:
        out.write(line)