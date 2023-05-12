def lambda_prac():
    list3 = {1, 2, 3, 4, 5}
    # def odd_value(n):
    #     if n % 2 != 0:
    #         return n
    print(list(filter(lambda n: n % 2 != 0, list3)))


lambda_prac()