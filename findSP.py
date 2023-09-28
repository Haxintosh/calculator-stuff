# License: MIT

def listDivisors(n):
    ans = []
    if n < 0:
        ans.append(-1)
    n = abs(int(n))
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans


def findSP(mtn, mpn):
    divsList = listDivisors(mtn)
    if mpn < 0:
        divsList.append(-1)
    mpn = abs(mpn)
    ans = []
    y = divsList[0]
    divsList[0] = 1
    for i in divsList:
        mtnDi = round(mtn*y/i)  # breaking every coding conventions known to mankind
        if mtnDi + i == mpn:
            ans += [i, mtnDi]
            break  # out of the calculatoe
    if divsList[-1] == -1:  # Jank to the max!
        ans[0] *= -1
        ans[1] *= -1
    return ans


def verify(mtn, mpn, ans):
    truth = False
    if mpn == ans[0]+ans[1]:
        truth = True
    else:
        truth = False

    if mtn == ans[0]*ans[1]:
        truth = True
    else:
        truth = False

    return truth


def main():
    mtn = int(input("m*n: "))
    mpn = int(input("m+n: "))
    ans1 = findSP(mtn, mpn)
    truth = verify(mtn, mpn, ans1)
    print(ans1)
    if truth:
        print("VERIFIED!")
    else:
        print("BAD!")


main()
