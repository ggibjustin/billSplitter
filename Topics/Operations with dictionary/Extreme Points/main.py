# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
key2 = min(test_dict, key = lambda k: test_dict[k])
print('min:', key2)
key3 = max(test_dict, key = lambda k: test_dict[k])
print('max:', key3)
