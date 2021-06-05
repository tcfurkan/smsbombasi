from socket import *
from threading import *
import optparse

print("""
 
 
  _____           _                                                _         _     _ _       _ _   _           
 |_   _|         | |                                   _     ____ | |       | |   (_) |     | | | (_)          
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   (_)   / __ \| |_ ___  | |__  _| | __ _| | |_ _ _ __ ___  
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \       / / _` | __/ __| | '_ \| | |/ _` | | __| | '_ ` _ \ 
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | |  _  | | (_| | || (__  | | | | | | (_| | | |_| | | | | | |
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| (_)  \ \__,_|\__\___| |_| |_|_|_|\__,_|_|\__|_|_| |_| |_|
                            __/ |                           \____/      ______                                 
                           |___/                                       |______|                                
                                 
                                               

                                               FURKAN - ESİLŞAH - ALEYNA

""")

def portScan(targethost,targetport):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        print(f"[+] {targetport} => Port Open")
    except:
        print(f"[-] {targetport} => Port Close")
    finally:
        sock.close()



def hostScan(targethost,targetports):
    try:
        targetIp = gethostbyname(targethost)
        print("*"*15,"*"*len(targetIp),sep="")
        print(f"[+] Ip Adresi: {targetIp}")
        try:
            targetName = gethostbyaddr(targetIp)
            print(f"[+] Ip Yolu: {targetName[0]}")
            print("*"*13,"*"*len(targetName[0]),sep="")
        except:
            print(f"[-] Yol Bulunamadı")
            print("*"*15,"*"*len(targetIp),sep="")
    except:
        print(f"[-] Host Bulunamadı: {targethost}")

    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=portScan,args=(targethost,int(targetport)))
            t.start()
        except ValueError:
            print("Hatal işlem")

def main():
    parser = optparse.OptionParser("Kullanım : python3 porttarama.py -İ <İp adresi>")
    parser.add_option("-H", dest="targetHost", type="string", help="Hedef Ana makine")
    parser.add_option("-p", dest="targetPort", type="string", help="(,) veya (,)'süz port belirtin")
    (options,args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    if (targetHost == None) or (targetPorts[0] == None):
        print(parser.usage)
        exit(0)
    hostScan(targetHost,targetPorts)

if __name__ == "__main__":
    main()




