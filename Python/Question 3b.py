def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    max_num = arr[0]
    min_num = arr[0]
   for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num
def find_second_largest(arr):
    if len(arr) < 2:
        return None  
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None
def main():
    arr = list(map(int, input("Enter the numbers separated by space: ").split()))
    max_num, min_num = find_max_min(arr)
    if max_num is None or min_num is None:
        print("Array is empty, cannot find max or min.")
    else:
        print(f"Maximum number: {max_num}")
        print(f"Minimum number: {min_num}") 
    second_largest = find_second_largest(arr)
    if second_largest is None:
        print("No second largest number in the array.")
    else:
        print(f"Second largest number: {second_largest}")
if __name__ == "__main__":
    main()
