def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

def quickSortHelper(data,first,last):
    if first<last:
        splitpoint = partition(data,first,last)
        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)

def partition(data,first,last):
    pivotvalue = data[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark

data = [54,26,93,17,77,31,44,55,20]
quickSort(data)
print(data)

def quickSortDescending(data):
    quickSortHelperDescending(data,0,len(data)-1)
    
def quickSortHelperDescending(data,first,last):
    if first<last:
        splitpoint = partitionDescending(data,first,last)
        quickSortHelperDescending(data,first,splitpoint-1)
        quickSortHelperDescending(data,splitpoint+1,last)

def partitionDescending(data,first,last):
    pivotvalue = data[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:  # Changed to >= for descending order
            leftmark = leftmark + 1
        while data[rightmark] <= pivotvalue and rightmark >= leftmark:  # Changed to <= for descending order
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark
data = [54,26,93,17,77,31,44,55,20]
quickSortDescending(data)
print(data)

