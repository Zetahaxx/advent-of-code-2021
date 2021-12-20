fhand=open("day2_2.txt")
horizontal=0
depth=0
aim=0
for line in fhand:
    if line.startswith("forward"):
        lx=line.split()
        horizontal+=int(lx[1])
        depth+=aim*int(lx[1])
    elif line.startswith("down"):
        lx=line.split()
        aim+=int(lx[1])
    else:
        lx=line.split()
        aim-=int(lx[1])

  
    
    
  
  #print(aim,depth)
#print(horizontal,depth)
print(horizontal*depth)