def listDivisors(n):
    ans = []
    if n < 0:
        ans.append(-1)
    n = abs(int(n))
    ans = []
    for i in range(1, n+1):
        if n%i == 0:
            ans.append(i)

    return ans

def findSP(mtn, mpn):
    divsList = listDivisors(mtn)
    ans = []
    y = divsList[0]
    divsList[0] = 1
    for i in divsList:
        mtnDi = round(mtn*y/i) # breaking every coding conventions known to mankind
        if mtnDi + i == mpn:
            ans += [i, mtnDi]
            break # out of the calculatoe
    return ans


mtn = int(input("m*n: "))
mpn = int(input("m+n: "))
ans1 = findSP(mtn, mpn)
if ans1 == []:
    print("Oh noes not a single answer was found, what a shame really!")
else:
    print(ans1)
