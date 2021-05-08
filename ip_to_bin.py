binr=[];dec=["","","",""];b= [0,0,0,0,0,0,0,0]
ip = input("ip ->>")    #get ip
def ip_len(ip_get,c,d):
    for i in ip_get:            #split num from "."
        if i==".":c += 1;continue
        else: d[c] += i
    
def ip_bin(d,b1,b2):
    for i in d :          #change num  in [dec] to binary
        iplen = int(i);bin2=''
        for i in range(0,8):
            if iplen >= b1[i]:b2[i]=1;iplen = iplen - b1[i]
        for i in b2 :len2 = str(i);bin2 = bin2 + len2    #send one by one ip binary in bin2 
        binr.append(bin2)     
ip_len(ip,c=0,d=dec)
ip_bin(d=dec,b1= [128,64,32,16,8,4,2,1],b2=b)
binary =  ".".join(binr);print(binary)