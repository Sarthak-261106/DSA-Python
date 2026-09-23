nums = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def juggling(nums,d):
    n=len(nums)
    d=int(input())
    gcdval=gcd(n,d%n)

    for i in range(gcdval):
        temp=nums[i]
        j=i
        while True:
            k=(j+d)%n
            if k==i:
                break

            nums[j]=nums[k]
            j=k
        nums[j]=temp    

    return nums
    






