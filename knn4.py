import math
import operator
def distance(instance1,instance2):
    distance=0
    for i in range(6):
        distance+=pow((instance1[i]-instance2[i]),2)
    return math.sqrt(distance)

def neighbours(instance,train,k):
    neighbours=[]
    distances=[]
    for i in range(len(train)):
        arr=[]
        arr.append(i)
        arr.append(distance(instance,train[i]))
        distances.append(arr) 
    distances.sort(key=operator.itemgetter(1))   
    for i in range(k):
        neighbours.append(distances[i])
    print(neighbours)    
    return neighbours

def getClass(instance,train,k):
    neighb=neighbours(instance,train,k)
    count0=0;
    count1=0;
    for i in range(k):
        print(train[neighb[i][0]][6])
        if train[neighb[i][0]][6] == 1:
           count1 = count1+1
        else:
            count0 = count0+1
        print(count0)
        print(count1)
    if count0 >= count1:
            return "cat"
    else:
            return "dog"  
        
lines1=list()
lines2=list()
train=list()
test=list()
with open("C:/Users/User/Downloads/kagglecatsanddogs_3367a/traindata.data") as f:
    lines1 = f.read().splitlines()
    for i in lines1:
        arr=list()
        arr=i.split(" ")
        train.append(arr)
    for i in range(len(train)):
        for j in range(7):
            train[i][j]=float(train[i][j])
with open("C:/Users/User/Downloads/kagglecatsanddogs_3367a/testdata.data") as f:
    lines2 = f.read().splitlines()
    for i in lines2:
        arr=list()
        arr=i.split(" ")
        test.append(arr)
    for i in range(len(test)):
        for j in range(7):
            test[i][j]=float(test[i][j]) 
maxk=3
maxacc=0
for k in range(7,8):            
 correct = 0
 wrong = 0
 for i in test:            
  a=getClass(i,train,k)  
  print(i)
  print(a)
  if i[6] == 0:
    if a == "cat":
        correct=correct+1
    else:
        wrong=wrong+1
  else:
    if a == "dog":
        correct=correct+1
    else:
        wrong=wrong+1
 accurracy=(correct/(correct+wrong))*100
 print("accuracy"+str(accurracy))
 if accurracy > maxacc:
    maxk=k
    maxacc=accurracy
print("max k:"+str(maxk))
print("max accuracy:"+str(maxacc))
            
