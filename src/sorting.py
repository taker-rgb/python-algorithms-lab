bubble_sort
insertion_sort
merge_sort
quick_sort
merge_sort(xs)
quick_sort(xs)

def merge_sort(xs: list[int]) -> list[int]:
    if len(xs) <= 1:
        return list(xs)
    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
