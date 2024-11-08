#Muhammad Alif Risaldy_F55123055_B
import numpy as np

#dengan Library
def dengan_library():
    A = np.array([[2, 0, -3], [1, 4, 5]])
    B = np.array([[3, 1], [-1, 0], [4, 2]])
    C = np.array([[4, 7], [2, 1], [1, -1]])


    AB = np.dot(A, B)
    AC = np.dot(A, C)

    result = AB + AC

    print("Dengan numpy:")
    print("AB:\n", AB)
    print("AC:\n", AC)
    print("AB + AC:\n", result)
    print("\n" + "="*30 + "\n")

#tanpa Library
def tanpa_library():
    def perkalian_matrix(X, Y):
        result = [[0] * len(Y[0]) for _ in range(len(X))]
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        return result


    def tambah_matrix(X, Y):
        result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
        return result


    A = [[2, 0, -3], [1, 4, 5]]
    B = [[3, 1], [-1, 0], [4, 2]]
    C = [[4, 7], [2, 1], [1, -1]]

    AB = perkalian_matrix(A, B)
    AC = perkalian_matrix(A, C)

    result = tambah_matrix(AB, AC)

    print("Tanpa Library:")
    print("AB:")
    for row in AB:
        print(row)
    print("\nAC:")
    for row in AC:
        print(row)
    print("\nAB + AC:")
    for row in result:
        print(row)


dengan_library()
tanpa_library()
