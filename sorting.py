def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        least = i
        for j in range(i+1,n):
            if arr[least]>arr[j]:
                least=j
        arr[least],arr[i]=arr[i],arr[least]

        # write your code :)

    return arr


def partition(arr, left, right):
    pivot = arr[left]  # make the first element as pivot
    i=left+1
    j=right
    while True:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>pivot:
            j-=1
        if j<=i:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[left],arr[j]=arr[j],arr[left]



    # write your code :)

    return  j # write your code :)


def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)  # sorts the left side of pivot
        quick_sort(arr, p + 1, right)  # sort the right side of pivot.

    return arr


def merge_sort(arr):
    n = len(arr)

    if n > 1:
        # find the mid point
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # sort the left and right part
        merge_sort(left)
        merge_sort(right)

        k=0
        j=0

        l=left[0]
        r=right[0]
        for i in range(n):
            if k<len(left):
                l=left[k]
            elif k>=len(left):
                l=right[len(right)-1]+1

            if j<len(right):
                r=right[j]
            elif j>=len(right):
                r=left[len(right)-1]+1

            if l<r:
                #if k<len(left):
                arr[i]=l
                k+=1

            elif l >= r:
                #if j < len(right):
                arr[i] = r
                j += 1


        # merge
        # write your code :)

    return arr

a=[4,3,7,5,1,4,5,10,9]
#print(merge_sort(a))
print(quick_sort(a,0,len(a)-1))
#print(selection_sort(a))
