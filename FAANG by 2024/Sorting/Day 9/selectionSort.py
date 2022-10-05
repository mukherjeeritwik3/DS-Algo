def selectionSort(lst):
    smallest = lst[0]
    ixd = 0
    l =1
    for i in range(ixd,len(lst)):
        if i == len(lst)-1:
            break
        for j in range(l,len(lst)):
            if lst[j]<smallest:
                smallest = lst[j]
                idx = j
        l+=1        
        lst[i],lst[idx] = lst[idx],lst[i]
        smallest = lst[i+1]
        idx = i+1




basket = [32,52,321,21,2,3,1,2,1,9,10]
selectionSort(basket)
print(basket)
