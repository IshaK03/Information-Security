import math


def matrix_generator(key, pt):
    no_of_rows = math.ceil(len(pt)/len(key))
    matrix = [["" for i in range(len(key))] for j in range(no_of_rows)]
    pt = pt.replace(" ", "_")

    no_of_elements = sum(len(row) for row in matrix)
    if len(pt)<no_of_elements:
        pt = pt + ("_")*(no_of_elements-len(pt))

    row,col = 0,0
    for i in pt:
        matrix[row][col] = i
        if col == len(matrix[0])-1 and row < len(matrix):
            row +=1 
            col = 0
        else:
            col += 1
    
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end = " ")
        print()


def encrypt(matrix, key):
    key_list = sorted(list(key))  #[A, C, H, K]
    # print(list(key))
    ans = ""
    
    ind = [key_list.index(letter) for letter in key]  # [2, 0, 1, 3]
    # print(ind)
    
    for i in range(len(ind)):
        j = ind.index(i)
        row = 0
        while(row < len(matrix)):
            ans += matrix[row][j]
            row += 1
        
    return ans


def decrypt(encrypted_message, key):
    matrix = matrix_generator(key, encrypted_message)
    matrix = transpose(matrix)
    key_list = sorted(list(key)) 
    # print(key_list)
    ind = [key_list.index(letter) for letter in key]  # [2, 0, 1, 3]
    ans = ""
    # print(ind)
    row = 0

    while(row<len(matrix)):
        for i in ind:
            ans += matrix[row][i]
        row += 1
        
    return ans


def transpose(matrix):
    transpose = [["" for _ in range(len(matrix))] for i in range(len(matrix[0]))]
    row, col = 0,0
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            transpose[row][col] = matrix[col][row]
            if col == len(transpose[0])-1 and row < len(transpose):
                col = 0
                row += 1
            else:
                col += 1
    print("Transpose Matrix of encrypted message:")
    print_matrix(transpose)

    return transpose


key = "HACK"
plaintext = "Geeks for Geeks"
print("Plaintext is:", plaintext)

matrix = matrix_generator(key, plaintext)
print_matrix(matrix)

encrypted_message = encrypt(matrix, key)
print("Encrypted Message is:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted Message is:", decrypted_message)