def bubbleSort(lst):
    l = len(lst)
    for i in range(len(lst)):
        for j in range(l):
            if j == len(lst)-1:
                l-=1
                break
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
basket = [32,52,321,21]

bubbleSort(basket)
print(basket)