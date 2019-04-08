import random

def quickselect(items, item_index):

    def select(lst, l, r, index):

        # caso base
        if r == l:
            return lst[l]

        # escolhe pivot random
        pivot_index = random.randint(l, r)

        # move pivot para o começo da lista
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # particiona
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # move pivot para posição correta
        lst[i], lst[l] = lst[l], lst[i]

        # particiona recursivamente apenas um lado
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)


a = [5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]
for i in range(1, len(a)):
    print ('{0:2} found in position {1}.'.format(i, quickselect(a, i)))