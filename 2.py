n = [0,1]
for x in n:
    for y in n:
        for z in n:
            for w in n:
                f = not x and (y or z) and w
                #if f==True:
                print(x,y,z,w,'  ',f)