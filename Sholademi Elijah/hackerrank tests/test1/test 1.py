def plus_minus(arr):
    n = int(input())
    if __name__ == '__main__':
        positive = 0
        negative = 0
        zero = 0

        arr = list(map(int, arr.rstrip().split()))

        for i in range(n):
            if arr[i] > 0:
                positive += 1
            elif arr[i] < 0:
                negative += 1
            elif arr[i] == 0:
                zero += 1

        positive_fraction = round(positive / len(arr), 5)
        negative_fraction = round(negative / len(arr), 5)
        zero_fraction = round(zero / len(arr), 5)

        print("The positive fraction: {0} \nThe negative fraction: {1} \nThe zero fraction: {2}".format(positive_fraction, negative_fraction, zero_fraction))


plus_minus(input("enter array items: "))
