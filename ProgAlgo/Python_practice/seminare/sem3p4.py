prim = input ("primul: ")
secund = input("al doilea: ")

dp = {}
ds = {}

for litera in prim:
    if litera in dp:
        dp[litera] += 1
    else:
        dp[litera] = 1

for litera in secund:
    if litera in ds:
        ds[litera] += 1
    else:
        ds[litera] = 1
# print(ds)
# print(dp)
if ds == dp:
    print("da, sunt anagrame")
else:
    print("nu sunt anagrame")