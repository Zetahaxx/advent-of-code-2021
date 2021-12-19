data=input()
numbers=[int(line) for line in data.rsplit()]
count=0
for i in range(1,len(numbers)):
  if numbers[i]>numbers[i-3]:
    count=count+1
print(count)

