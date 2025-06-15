class MergeSort:
    @staticmethod
    def merge(l: list, r: list) -> list:
        i = j = 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            elif r[j] <= l[i]:
                res.append(r[j])
                j += 1
        # Pick up the remaining/end elements
        while i < len(l):
            res.append(l[i])
            i += 1
        while j < len(r):
            res.append(r[j])
            j += 1
        return res

    @staticmethod
    def merge_sort(arr: list) -> list:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        l = MergeSort.merge_sort(arr[:mid])
        r = MergeSort.merge_sort(arr[mid:])
        sorted_arr = MergeSort.merge(l, r)
        return sorted_arr


def print_list(arr):
    for m in range(len(arr)):
        print(arr[m], end=" ")
    print()


# Driver 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 3]
    print("Given array is")
    print_list(arr)
    sorted_arr = MergeSort.merge_sort(arr)
    print("\nSorted array is ")
    print_list(sorted_arr)