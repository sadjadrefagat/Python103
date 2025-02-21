import copy

L1 = [1, 2, 2, [3, 2, 3], 5, 4, 2, 1]
L2 = copy.deepcopy(L1)
L1[1] = 7
L1[3][1] = 5
L2[3][0] = -8

print(L1)
print(L2)

S1 = {"A", 2, 5, 5, "C", "D", 5, "E"}
S3 = S1.copy()
S2 = {"B", 3, "D", "E"}
S3.add("WWW")
print(S1)