x = [-1, -4, -0.06, 5, 7, 13]

def neg_sel(arr):
    neg_x = []
    for n in arr:
        if n < 0:
            neg_x.append(n)
    return neg_x

print(neg_sel(x))

neg_lst = [n for n in x if n < 0]
print(neg_lst)

######

odd_numbers = (i for i in range(1, 101) if i % 2 != 0)
print(odd_numbers)

# Python
n = input('Enter a number: ')
arr = list(map(int, n.split()))

print(" ".join(list(map(str, arr))))
