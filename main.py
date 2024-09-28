data = [

    [100, 200, 300],
    [400, 500, 600],
    [150, 140, 160]

    ]

list = []

for row in data:
    for item in row:
        if item > 190:
                list.append(item)

print(list)

