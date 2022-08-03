import itertools


def find_subsets(s, n):
    return list(itertools.combinations(s, n))


s = {1, 2, 3}
n = 2

print(find_subsets(s, n))
