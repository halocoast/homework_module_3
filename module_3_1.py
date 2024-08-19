calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    a1 = []
    a1.append(len(string))
    a1.append(string.upper())
    a1.append(string.lower())
    return tuple(a1)
def is_contains(string, list_to_search):
    count_calls()
    flag = False
    string = string.upper()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string in list_to_search:
        flag = True
    return flag
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)