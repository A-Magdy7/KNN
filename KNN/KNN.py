InTrain = open("TrainData.txt","r")
InTest = open("TestData.txt","r")

Tr = InTrain.readlines()
Tst = InTest.readlines()

L = []
cnt = 0
K = 10


for i in Tr:
    L.append(i.split(','));

for i in range(len(Tst)-1):
    t1 = Tst[i].split(',')

    dist = []

    for k in range(len(L)-1):
        j = L[k]
        dist.append([((float(t1[0])-float(j[0]))*(float(t1[0])-float(j[0])) + (float(t1[1])-float(j[1]))*(float(t1[1])-float(j[1]))
                    + (float(t1[2])-float(j[2]))*(float(t1[2])-float(j[2])) + (float(t1[3])-float(j[3]))*(float(t1[3])-float(j[3]))
                    + (float(t1[4])-float(j[4]))*(float(t1[4])-float(j[4])) + (float(t1[5])-float(j[5]))*(float(t1[5])-float(j[5]))
                    + (float(t1[6])-float(j[6]))*(float(t1[6])-float(j[6])) + (float(t1[7])-float(j[7]))*(float(t1[7])-float(j[7])))**0.5 , j[8]])

    dist.sort()
    dic = []
    mx = 0
    ans = ""

    for j in range(K):

        B = 0

        for k in dic:
            if k[0] == dist[j][1]:
                B = 1
                k[1] += 1

        if B == 0:
            dic.append([dist[j][1], 1])

    for j in dic:
        if j[1] > mx:
            mx = j[1]
            ans = j[0]

    if ans == t1[8]:
        cnt += 1


print(cnt*1.0/len(Tst))