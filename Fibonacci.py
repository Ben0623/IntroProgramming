



def main():
    n = int(input("Enter the number"))
    cur, prev = 1, 1
    for i in range(n-2):
        cur , prev = cur+prev, cur
    print("the Fib number is:", cur)
main()