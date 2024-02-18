import numpy as np

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # Print each element in the row
        print()  # Move to the next row
    print()

def row_addition_elementary_matrix(n, target_row, source_row, scalar):

    if target_row < 0 or source_row < 0 or target_row >= n or source_row >= n:
        raise ValueError("Invalid row indices.")

    if target_row == source_row:
        raise ValueError("Source and target rows cannot be the same.")

    elementary_matrix = np.identity(n)
    elementary_matrix[target_row, source_row] = scalar

    return np.array(elementary_matrix)

def scalar_multiplication_elementary_matrix(n, row_index, scalar):

    if row_index < 0 or row_index >= n:  # checks is the row index is not in range
        raise ValueError("Invalid row index.")

    if scalar == 0:
        raise ValueError("Scalar cannot be zero for row multiplication.")

    elementary_matrix = np.identity(n)  # creating an elementary matrix,identity matrix
    # put the scalar we received in the same place as the number we want to make 0
    elementary_matrix[row_index, row_index] = scalar

    return np.array(elementary_matrix)  # return the elementary matrix with the number we put into it


#  swapping between row i to row j in the matrix
def swap_row(mat, i, j):
    N = len(mat)
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp

def swap_rows_elementary_matrix(n, row1, row2):
    elementary_matrix = np.identity(n)
    elementary_matrix[[row1, row2]] = elementary_matrix[[row2, row1]]

    return np.array(elementary_matrix)
def Determinant(matrix, mul):
    """
    Recursive function for determinant calculation
    :param matrix: Matrix nxn
    :param mul: The double number
    :return: determinant of matrix
    """
    width = len(matrix)
    # Stop Conditions
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            # Change the sign of the multiply number
            sign *= -1
            #  Recursive call for determinant calculation
            det = det + mul * Determinant(m, sign * matrix[0][i])
    return det

# Partial Pivoting: Find the pivot row with the largest absolute value in the current column
def partial_pivoting(A,i,N,id):
    pivot_row = i
    v_max = A[pivot_row][i]
    for j in range(i + 1, N):
        if abs(A[j][i]) > v_max:
            v_max = A[j][i]
            pivot_row = j

    # if a principal diagonal element is zero,it denotes that matrix is singular,
    # and will lead to a division-by-zero later.
    if A[i][pivot_row] == 0:
        return "Singular Matrix"


    # Swap the current row with the pivot row
    if pivot_row != i:
        e_matrix = swap_rows_elementary_matrix(N, i, pivot_row)
        e_id = swap_rows_elementary_matrix(N, i, pivot_row)
        print(f"elementary matrix for swap between row {i} to row {pivot_row} :\n {e_matrix} \n")
        A = np.dot(e_matrix, A)
        id = np.dot(e_id, id)
        print(f"The matrix after elementary operation :\n {A}")
        print("------------------------------------------------------------------")

    return A, id

