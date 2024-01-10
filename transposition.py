import math


def matrix_generator(key, pt, encrypt):
    no_of_rows = math.ceil(len(pt)/len(key))
    matrix = [["" for i in range(len(key))] for j in range(no_of_rows)]
    if(encrypt):
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
    else:
        row, col = 0,0
        for i in pt:
            matrix[row][col] = i
            if row == len(matrix)-1 and col < len(matrix[0]):
                col +=1
                row = 0
            else:
                row += 1
    
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end = " ")
        print()


def encrypt(matrix, key):
    key_list = sorted(list(key))  
    # print(list(key))
    
    ind = [key_list.index(letter) for letter in key]  
    # print(ind)
    
    ans = ""
    for i in range(len(ind)):
        j = ind.index(i)
        row = 0
        while(row < len(matrix)):
            ans += matrix[row][j]
            row += 1
        
    return ans


def decrypt(encrypted_message, key):
    matrix = matrix_generator(key, encrypted_message, False)
    print("Initial Matrix of Encrypted text:")
    print_matrix(matrix)

    key_list = sorted(list(key)) 
    print(key_list)

    ind = [key_list.index(letter) for letter in key]  
    print(ind)

    matrix2 = [["_" for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    print("Final Matrix of Encrypted text:")
    col = 0
    for i in range(len(ind)): 
        j = ind.index(i)    
        x = 0               
        row = 0
        while(x < len(matrix)):
            matrix2[x][j] = matrix[row][col] 
            x += 1
            row += 1
        col += 1

    print_matrix(matrix2)
    
    ans = ""
    for row in range(len(matrix2)):
        for col in range(len(matrix[row])):
            ans += matrix2[row][col]
    
    ans = ans.replace("_", " ")
    return ans


key = "MEOWS"
plaintext = "Hello Im Isha"
print("Plaintext is:", plaintext)

matrix = matrix_generator(key, plaintext, True)
print_matrix(matrix)

encrypted_message = encrypt(matrix, key)
print("Encrypted Message is:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted Message is:", decrypted_message)
