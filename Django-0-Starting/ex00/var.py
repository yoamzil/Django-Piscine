def	my_var():
	my_int = 42
	my_str = "42"
	my_text = "quarante-deux"
	my_float = 42.0
	my_bool = True
	my_list = [42]
	my_dict = {42: 42}
	my_tuple = (42,)
	my_set = set()

	print(my_int, "has a type", type(my_int))
	print(my_str, "has a type", type(my_str))
	print(my_text, "has a type", type(my_text))
	print(my_float, "has a type", type(my_float))
	print(my_bool, "has a type", type(my_bool))
	print(my_list, "has a type", type(my_list))
	print(my_dict, "has a type", type(my_dict))
	print(my_tuple, "has a type", type(my_tuple))
	print(my_set, "has a type", type(my_set))

if	__name__ == '__main__':
	my_var()