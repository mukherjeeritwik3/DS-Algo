def insertionSort(lst):
    callbackIdx = -1
    for i in range(len(lst)):
        t =i
        while(callbackIdx!=-1):
            if lst[t]<lst[callbackIdx]:
                lst[t], lst[callbackIdx] = lst[callbackIdx], lst[t]
                t-=1
            callbackIdx-=1
        callbackIdx=i


basket = [32,52,321,21,2,3,1,2,1,9,10]
insertionSort(basket)
print(basket)
