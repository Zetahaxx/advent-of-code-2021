#input given data here
data='''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
horizontal=0
depth=0
aim=0
for line in data.splitlines():
  command,n=line.split()
  if command=="forward":
    horizontal+=int(n)
    depth+=aim*int(n)
    #print(depth)
  elif command=="down":
    aim+=int(n)
  else:
    aim-=int(n)
  
  #print(aim,depth)
#print(horizontal,depth)
print(horizontal*depth)
