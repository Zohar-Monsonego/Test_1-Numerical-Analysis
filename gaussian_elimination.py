import numpy as np
from colors import bcolors
from matrix_utility import swap_row
from condition_of_linear_equations import condition_number


def gaussianElimination(mat):
    N = len(mat)  # return the row's number

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"


    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)




def forward_substitution(mat):
    N = len(mat)  # return the row's number
    for k in range(N):

        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[k][pivot_row]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)
        # End Partial Pivoting

        #pivot_col = pivot_row
        #v_max = mat[pivot_row][pivot_col]
        #for t in range(k, N):
            #if mat[t][t] == 0:  #find max in row
                #for g in range(N):
                    #if abs(mat[t][g]) > v_max:
                        #v_max = mat[t][g]
                        #pivot_col = g

                #if pivot_col != t:
                    #mat = swap_col(mat, t, pivot_col)

        #for t in range(k, N):  #if after switching still principal diagonal is zero
            #if mat[t][t] == 0:
                #return k

        for i in range(k + 1, N):

            #  Compute the multiplier
            m = mat[i][k] / mat[k][k]
            #print("m-multiplier: " + str(m))

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m
                #print(mat[i][j])

            # filling lower triangular matrix with zeros
            mat[i][k] = 0
            #print(f"matrix after ++-+++ :\n {mat}")
            #  print("3-1/3= " + str(3 - 1 / 3))

    return -1


# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        if round(mat[i][i], 3) == 0:
            return "no solution"

        x[i] = (x[i] / mat[i][i])

    return x


if __name__ == '__main__':
    print("date:19/2/24\n"
          "group members: \n"
          "(1) name: Shulamit-mor-yossef. id: 206576977. \n"
          "(2) name: Zohar-monsonego. id: 214067662. \n"
          "(3) name: hodaya-shirazie. id: 213907785.\n"
          "submitted by: name: Zohar Monsonego, id: 214067662.\n"
          "input: \n"
          "output:\n ")

    A_b = np.array([[0, 1, 2, -1],
                    [1, 0, 1, -3],
                    [2, 3, 0, 0]])

    A_b_c = np.array([[0, 1, 2],
                      [1, 0, 1],
                     [2, 3, 0]])

    cond = condition_number(A_b_c)
    if int(cond) > 1:
        print("The condition number is too high, might be a significant error in the solution: ", cond)
    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
        print("The condition number is: ", str(cond))