b= [0,0,0,0,0,0,0,0];b1= [128,64,32,16,8,4,2,1];dec=["","","",""];binr=[];c=0
ip = input("your ip >>>")    #get ip
for i in ip:            #split num from "."
    if i==".":
        c += 1
        continue
    else:
        dec[c] += i
for i in dec :          #change num  in [dec] to binary
    iplen = int(i);bin2=''
    for i in range(0,8):
        if iplen >= b1[i]:
            b[i]=1
            iplen = iplen - b1[i]
    for i in b :len2 = str(i);bin2 = bin2 + len2    #send one by one ip binary in bin2 
    binr.append(bin2)     
binary =  ".".join(binr);print(binary)



       
