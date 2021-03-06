#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque


def get_fibonacci_number(index):
	if index == 0:
		return 0
	elif index == 1 :
		return 1
	else:
		return get_fibonacci_number(index-1)+ get_fibonacci_number(index-2)

def get_fibonacci_sequence(lenght, result = [0,1]):
	if lenght == 0:
		return None
	elif lenght == 1:
		return result[0:1]
	elif lenght == 2:
		return result[0:2]
	elif len(result) < lenght:
		return get_fibonacci_sequence(lenght,result + [result[-1] + result[-2]])
	else:
		return (result)


def get_sorted_dict_by_decimals(dict_arg):
	return dict(sorted(dict_arg.items(), key = lambda t: t[1] % 1.0 ))

def fibonacci_numbers(length):
	initial_val = [0,1]
	yield initial_val[0]
	if length >= 2:
		yield initial_val[1]
	last_elems = deque(initial_val)
	if length > 2:
		for i in range(2,length):
			fibo_num = last_elems[-1] + last_elems[-2]
			last_elems.append(fibo_num)
			last_elems.popleft()
			yield fibo_num

def build_recursive_sequence_generator(TODO,crepe):
	pass

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	print("------ GENERATORS ------")
	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
