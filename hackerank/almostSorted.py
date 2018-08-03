# https://www.hackerrank.com/challenges/almost-sorted/problem


def almostSorted(arr):
    start = -1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            start = i
            break
    if start == -1:
        print("no")
        return

    for j in range(len(arr)-1, start - 1, -1):
        if arr[j] < arr[j-1]:
            end = j
            break
    arr[start], arr[end] = arr[end], arr[start]
    i = 0
    res = True
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            res = False
            break
        i += 1
    if res:
        print("%s\n%s %d %d" % ("yes", "swap", start+1, end+1))
        return
    arr[start+1:end] = arr[start+1:end][::-1]
    i = 0
    res = True
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            res = False
            break
        i += 1
    if res:
        print("%s\n%s %d %d" % ("yes", "reverse", start+1, end+1))
        return
    print("no")
    return


if __name__ == "__main__":
    arr = [1, 5, 4, 3, 2, 6]
    #arr = [3, 1, 2]
    arr = [4, 2]
    almostSorted(arr)
