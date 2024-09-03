def calculate_structure_sum(data_, count = 0):
    if isinstance(data_, str):
        count += len(data_)
    elif isinstance(data_, int):
        count += data_
    elif isinstance(data_, dict):
        for i in data_:
            count = calculate_structure_sum(i, count)
        for i in data_.values():
            count = calculate_structure_sum(i, count)
    else:
        for i in data_:
            count = calculate_structure_sum(i, count)
    return count

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)