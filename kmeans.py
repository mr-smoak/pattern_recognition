import math
def distance(instance1,instance2):
    distance=0
    for i in range(6):
        distance+=pow((instance1[i]-instance2[i]),2)
    return math.sqrt(distance)

def mean(numbers):
	return sum(numbers)/float(len(numbers))
k=2
train=list()
lines=list()
centroid=list()
new=[[],[]]
prev=[[0,0,0,0,0,0],[0,0,0,0,0,0]]
clusters=[[],[]]
with open("C:/Users/User/Downloads/kagglecatsanddogs_3367a/traindata.data") as f:
    lines1 = f.read().splitlines()
    for i in lines1:
        arr=list()
        arr=i.split(" ")
        train.append(arr)
    for i in range(len(train)):
        for j in range(7):
            train[i][j]=float(train[i][j])
for i in range(k):
    centroid.append(train[i])
count=0    
while (prev != centroid) & (count != 300):
    clusterstmp=[[],[]]
    newtmp=[[],[]]
    for i in train:
        b=distance(i,centroid[0])
        index=0
        for j in range(k):
            a=distance(i,centroid[j])
            if a < b:
                b=a
                index=j
        clusterstmp[index].append(i)        
    clusters=clusterstmp
    for i in range(k):
       for j in range(6):
         attrib=list()
         for p in clusters[i]:
             attrib.append(p[j])
         newtmp[i].append(mean(attrib))
    new=newtmp
    prev=centroid
    centroid=new
    print(count)
    print(prev)
    print(centroid)
    count=count+1
countright=0
countwrong=0
for i in clusters[0]:
    if i[6] == 0:
        countright=countright+1
    else:
        countwrong=countwrong+1
for i in clusters[1]:
    if i[6] == 1:
        countright=countright+1
    else:
        countwrong=countwrong+1    
accuracy=(countright/(countwrong+countright))*100
print("Accuracy:"+str(accuracy))
        
    


