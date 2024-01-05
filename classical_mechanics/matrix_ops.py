from sympy import Matrix, Symbol, solve

# Declare symbolic variables and set matrix
k, omega, m, M = Symbol('k'), Symbol('\U000003C9'), Symbol('m'), Symbol('M')
matrix = Matrix([
    [k-omega**2*m, -k, 0],
    [-k, 3*k-omega**2*M, -k],
    [0, -k, k-omega**2*m]
])

# Set the matrix determinant equal to zero and solve for omega
ans = solve(matrix.det(), omega)
print(ans)

# Double check
ans2 = solve((k-omega**2*m)*((3*k-omega**2*M)*(k-omega**2*m)-k**2) - k*(k*(k-omega**2*m)),omega)
print(ans2)

# pprint(M.det())

# print('eigenvalues:')
# for evs in M.eigenvals():
#     print(evs)
#
# print('eigenvectors:')
# for evs in M.eigenvects():
#     print(evs)
