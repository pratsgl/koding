import itertools
my_list = [1,2,3,4,5,6]

#combinations =  itertools.combinations(my_list,3)
combinations =  itertools.combinations(my_list,2)

for c in combinations:
    print(c)

# permutations = itertools.combinations(my_list,3)
# for p in permutations:
#     print(p)
