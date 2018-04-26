import math
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

lines1=list()
lines2=list()
train=list()
test=list()
cat=list()
dog=list()
catattr=list()
dogattr=list()
meancat=list()
meandog=list()
stdcat=list()
stddog=list()
truepositive=0
truenegative=0
falsepositive=0
falsenegative=0
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
for i in train:
    if i[6] == 0:
        cat.append(i)
    else:
        dog.append(i)          
for i in range(6):
    catattrib=list()
    dogattrib=list()
    for j in cat:
        catattrib.append(j[i])
    catattr.append(catattrib)
    for j in dog:
        dogattrib.append(j[i])
    dogattr.append(dogattrib)
for i in catattr:
    meancat.append(mean(i))
    stdcat.append(stdev(i))
for i in dogattr:
    meandog.append(mean(i))
    stddog.append(stdev(i))
countright=0
countwrong=0
for i in test:
    print(i)
    probc=len(cat)/(len(cat)+len(dog))
    probd=len(dog)/(len(cat)+len(dog))

    for j in range(6):
      print(j)  
      a=calculateProbability(i[j],meancat[j],stdcat[j])
      b=calculateProbability(i[j],meandog[j],stddog[j])
      probc=probc*a
      probd=probd*b
      print(a)
      print(probc)
      print(b)
      print(probd)  
    if probc >= probd:
        print("cat")
        if i[6] == 0:
            countright=countright+1
            truepositive=truepositive+1
        else:
            countwrong=countwrong+1
            falsepositive=falsepositive+1
    else:
        print("Dog")
        if i[6] == 1:
            countright=countright+1
            truenegative=truenegative+1
        else:
            countwrong=countwrong+1
            falsenegative=falsenegative+1
accuracy=(countright/(countwrong+countright))*100
print("accuracy:"+str(accuracy))
print("truepositive:"+str(truepositive/(truepositive+falsepositive+truenegative+falsenegative)))
print("truenegative:"+str(truenegative/(truepositive+falsepositive+truenegative+falsenegative)))
print("falsepositive:"+str(falsepositive/(truepositive+falsepositive+truenegative+falsenegative)))
print("falsenegative:"+str(falsenegative/(truepositive+falsepositive+truenegative+falsenegative)))
        
      
        
