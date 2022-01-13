def reverse(n):
    s = 0
    while n > 0:
        r = n % 10
        s = s * 10 + r
        n = int(n / 10)

    return s

num = int(input("Enter a number\n"))
ans = reverse(num)
print("Reversed Number = ",ans)