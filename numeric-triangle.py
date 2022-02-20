'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def numeric_triangle (triangle):
    tr = [row[:] for row in triangle] 
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]