from LIB_bin import ip_bin #add function_for IP to bin
from LIB_class import class_ip #add function_for find class IP
ip =input("IP >>>")
while True: 
    q = int(input("1.Cal Binary IP\n2.Find Class IP or pub & privet\n3.Full Information\n"))
    if q==1 or q==2 or q==3:break    #for not closed program when user input wrong num
def main(ip,num):       #call func with input user 
    if num == 1 :ip_bin(ip)
    if num == 2 :class_ip(ip)
    if num == 3 :ip_bin(ip);class_ip(ip)
main(ip,q)
