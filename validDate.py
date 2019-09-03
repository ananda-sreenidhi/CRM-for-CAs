def validdate(d,m,y):
    c=0
    if m in [1,3,5,7,8,10,12]:
        if d>=1 and d<=31:
                c+=1
        elif m==2:
                if ((y%4==0 and y%100<>0) or y%400==0):
                    if d>=1 and d<=29:
                        c+=1
                    else:
                        if d>=1 and d<=28:
                            c+=1
    elif m in [4,6,9,11]:
        if d>=1 and d<=30:
            c+=1

    if c!=0:
        return True
    else:
        return False
