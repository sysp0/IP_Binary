#Libs find class
def class_ip (ip):
    s=["",""];sp1=0;sp2=0
    def split(ip,c,d):
        for i in ip :
            if c == 2:
                break 
            elif i==".":c += 1;continue
            else: d[c] += i
    def class_ip (sp1,sp2):
        if  sp1 == "192":
            cls = "C"
            if sp2 == "168":
                pr = "Yes"
            else:
                pr = "No"    
        if sp1 == "172":
            cls = "B"
            if int(sp2) in range(16,32):
                pr = "Yes"
            else:
                pr = "No"
        if sp1 == "10":
            cls = "A"
            pr = "Yes"
        else :
            cls = "none"
            pr = "No"     
        print("IP Class : ",cls,"\nPrivet Network : ",pr )
    split(ip,c=0,d=s)
    class_ip(sp1=s[0],sp2=s[1])
ip = input("IP >>>")
# # class_ip(ip)
