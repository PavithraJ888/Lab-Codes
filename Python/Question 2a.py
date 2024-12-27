def primeno(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

start = int(input("Enter starting number: "))
end = int(input("Enter end number : "))
primeno(start, end)
