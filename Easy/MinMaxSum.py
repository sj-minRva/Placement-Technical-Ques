user_input = input("Enter 5 numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

if len(arr) != 5:
    print("Please enter exactly 5 integers.")
else:
    def miniMaxSum(arr):
        total = sum(arr)
        min_value = min(arr)
        max_value = max(arr)
        min_sum = total - max_value
        max_sum = total - min_value
        print(f"{min_sum} {max_sum}")
    
    miniMaxSum(arr)

print(2)