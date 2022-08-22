def fiboRecursion(prev_num, next_num, iterations):
    next_add = prev_num + next_num
    print(f'{prev_num}', end=" ")
    iterations -= 1

    if iterations > 0:
        fiboRecursion(next_num, next_add, iterations)


fiboRecursion(0, 1, 10)
