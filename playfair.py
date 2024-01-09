def key_matrix(key):
    alphabet ="ABCDEFGHIKLMNOPQRSTUVWXYZ" # exclude j
    matrix = [["" for i in range(5)] for j in range(5)]
    key = key.upper()
    key = key.replace(" ", "")

    for i in key:
        if i in alphabet:
            alphabet = alphabet.replace(i, "")

    row, col = 0,0
    for i in key + alphabet:
        if not any(i in sublist for sublist in matrix):
            matrix[row][col] = i
            if col == 4 and row < 4:
                col = 0
                row += 1
            elif col<4:
                col += 1

    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()

    return matrix


def pairs(pt):
    pt = pt.upper()
    pt = pt.replace(" ", "")
    pairs = []
    i = 0
    while(i<len(pt)):
        if i == len(pt) - 1:
            pairs.append(pt[i] + "Z")
            break
        elif pt[i] != pt[i+1]:
            pairs.append(pt[i] + pt[i+1])
            i += 2
        elif pt[i] == pt[i+1]:
            pairs.append(pt[i] + "X")
            i += 1
    print("Pairs are:",end=" ")
    for i in pairs:
        print(i, end=" ")
    print()
    return pairs
    
def Codeword(matrix, pairs, encrypt):
    row1,col1,row2,col2 = 0,0,0,0
    ans = ""
    
    for pair in pairs:
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == pair[0]:
                    row1 = row
                    col1 = col
                elif matrix[row][col] == pair[1]:
                    row2 = row
                    col2 = col
        if(encrypt):
            if col1 == col2:
                ans += matrix[(row1+1)%5][col1]
                ans += matrix[(row2+1)%5][col2] 
            elif row1 == row2:
                ans += matrix[row1][(col1+1)%5] 
                ans += matrix[row2][(col2+1)%5] 
            else:
                ans += matrix[row1][col2]
                ans += matrix[row2][col1]
        else:
            if col1 == col2:
                ans += matrix[row1-1][col1]
                ans += matrix[row2-1][col2] 
            elif row1 == row2:
                ans += matrix[row1][col1-1] 
                ans += matrix[row2][col2-1] 
            else:
                ans += matrix[row1][col2]
                ans += matrix[row2][col1]
        if(not encrypt): 
            # ans = ans.replace("Z", "") if ans[-1] == "Z" else ans
            start_idx = 1
            while True:
                try:
                    bogus = ans[start_idx:].index("X") + start_idx
                    if ans[bogus - 1] == ans[bogus + 1]:
                        ans = ans[:bogus] + ans[bogus + 1:]
                    start_idx = bogus + 1
                except:
                    break
            # i=0
            # while(i+2 < len(ans)):
            #     if ans[i] == ans[i+2] and ans[i+1] == "X":
            #         ans = ans.replace(ans[i+1], "")
            #     i += 1
           
    return ans

        
keyword = input("Enter Key: ")
matrix = key_matrix(keyword)

plaintext = "hello world"
pairs1 = pairs(plaintext)

encrypted_message = Codeword(matrix, pairs1, True)
print("Encrypted message is:" , encrypted_message)

pairs2 = pairs(encrypted_message)
decrypted_message = Codeword(matrix, pairs2, False)


print("Decrypted Message is:" , decrypted_message)
