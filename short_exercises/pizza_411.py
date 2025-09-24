my_pizzas = ['meateater', 'pepporoni', 'bbq chicken']
friend_pizzas = my_pizzas[:]
my_pizzas.append('veggie delight')
friend_pizzas.append('chicken supreme')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")