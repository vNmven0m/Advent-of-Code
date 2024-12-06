import numpy as np
import re

regex = r"XMAS"

x_mas = [np.array([["M", "O", "M"], ["O", "A", "O"], ["S", "O", "S"]]),
         np.array([["M", "O", "S"], ["O", "A", "O"], ["M", "O", "S"]]),
         np.array([["S", "O", "S"], ["O", "A", "O"], ["M", "O", "M"]]),
         np.array([["S", "O", "M"], ["O", "A", "O"], ["S", "O", "M"]]),]


def findxmas(matrix):
    #horizontal
    result = 0
    for row in matrix:
        string = ""
        for char in row:
            string += char
        result += len(re.findall(regex,string))
    #diagnonal
    for i in reversed(range(matrix.shape[1])):
        shift = 0
        string = ""
        for n in range(i,matrix.shape[1]):
            string += matrix[i+shift][shift]
            shift += 1
        result += len(re.findall(regex,string))
    for col in range (1,matrix.shape[1]): 
        shift = 0
        string = ""
        for row in range(matrix.shape[0]-col):
            string += matrix[row][col+shift]
            shift += 1
        result += len(re.findall(regex,string))
    return result

def check_matrix (matrix):
    for a in x_mas:
        if np.array_equal(a, matrix):
            return True
    return False



def findx_mas(matrix):
    result = 0
    for row in range(matrix.shape[0]-2):
        for col in range(matrix.shape[1]-2):
            a = np.array([[matrix[row][col], "O", matrix[row][col + 2]], 
                          ["O", matrix[row + 1][col + 1], "O"],
                          [matrix[row + 2][col], "O", matrix[row + 2][col + 2]]])
            if check_matrix(a):
                result +=1
    return result


input = np.loadtxt("Day 4/input/input.txt",dtype=str)
matrix = np.array([ list(word) for word in input ])
result = 0

print("Part 2",findx_mas(matrix))

for x in range(4):
    matrix = np.rot90(matrix)
    result += findxmas(matrix)
print("Part 1",result)


