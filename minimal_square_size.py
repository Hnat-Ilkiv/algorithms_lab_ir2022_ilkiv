def minimal_square_size(N, W, H):
    max_w_square = N * W
    max_h_square = N * H
    min_squere_size = 0
    count = 0

    if max_h_square >= max_w_square:
        # print("if")
        for i in range(1, N + 1):
            count += 1
            temp_H = H * i
            temp_W = (N // i if N % i == 0 else N // i + 1) * W
            squere_size = temp_H ** 2 if temp_H >= temp_W else temp_W ** 2
            # print(f"H: {temp_H}\nW: {temp_W}\nsquere_size: {squere_size}\n")
            if min_squere_size > squere_size or min_squere_size == 0:
                min_squere_size = squere_size
        result = int(min_squere_size ** 0.5)

    else:
        # print("else")
        for i in range(1, N + 1):
            count += 1
            temp_W = W * i
            temp_H = (N // i if N % i == 0 else N // i + 1) * H
            squere_size = temp_H ** 2 if temp_H >= temp_W else temp_W ** 2
            # print(f"H: {temp_H}\nW: {temp_W}\nsquere_size: {squere_size}\n")
            if min_squere_size > squere_size or min_squere_size == 0:
                min_squere_size = squere_size
        result = int(min_squere_size ** 0.5)

    print(f"count: {count}")

    return  int(result)

if __name__ == "__main__":
    # N, W, H = 10, 3, 2 # 3

    # result = minimal_square_size(N, W, H)
    # print(f"result: {result}\n")

    # N, W, H = 4, 1, 1 # 2

    # result = minimal_square_size(N, W, H)
    # print(f"result: {result}\n")

    N, W, H = 9000, 1000000000, 999999999 # 1999999998

    result = minimal_square_size(N, W, H)
    print(f"result: {result}\n")

    # N, W, H = 1, 5, 4 # 5

    # result = minimal_square_size(N, W, H)
    # print(f"result: {result}\n")
