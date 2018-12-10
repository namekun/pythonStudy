# n명 중 두명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들자

def makeCombo(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i],"-",a[j])


a = ['Tom', 'Jerry', 'Mike']

makeCombo(a)