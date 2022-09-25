    first = 0
    last = arr.__len__()-1

    while(first<last):
        temp = arr[first] +arr[last]
        if(temp==sum):
            return True;
        elif (temp<sum):
            first+=1
        else:
            last-=1
    return False