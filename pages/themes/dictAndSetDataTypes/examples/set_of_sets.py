set_of_numbers = {1,2,3}
print(set_of_numbers) #{1, 2, 3}

set_of_strings = {"a", "b"}
print(set_of_strings) #{'b', 'a'}

set_of_imutables = {"a", 1, "b", 2, 3}
print(set_of_imutables) #{'a', 'b', 2, 3, 1}

set_of_mutables = { [1,2,3], ["a", "b"] }
print(set_of_imutables) #TypeError: unhashable type: 'list'