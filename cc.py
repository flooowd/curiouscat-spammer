import os
import requests as req
import time as  t

def asciilogo():
    os.system('cls && color 3')
    print(' ██████╗ ██████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ ')
    t.sleep(0.05)
    print('██╔════╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗')
    t.sleep(0.05)
    print('██║     ██║         ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝')
    t.sleep(0.05)
    print('██║     ██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗')
    t.sleep(0.05)
    print('╚██████╗╚██████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║')
    t.sleep(0.05)
    print(' ╚═════╝ ╚═════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝')
    print('')
def spam():
    tries = 0
    asciilogo()
    os.system('title CuriousCat Spammer')
    profileid = str(input('Profile ID (https://curiouscat.qa/<profileid>/): ' ))
    checkprofileid = profileid.startswith("http")
    if checkprofileid == True:
        print('Put only the ProfileID not the link.')
        os.system('pause')
        os.system('cls')
        spam()

    question = str(input('Question: '))
    if len(question) < 4:
        print('Too short, please 5 or more characters')
        os.system('pause')
        os.system('cls')
        spam()
    time = float(input('Delay between requests (recommended: 2): '))
    os.system('cls')
    while 1:
        t.sleep(time)
        tries = tries + 1
        data = req.post("https://curiouscat.qa/api/v2/post/create", verify=True, data={"to": profileid, "anon": "true","question": question}).json()
        
        if "error" in data:
            print('ERROR: ' + data["error"])
            if data["error"] == 'Wait a bit':
                os.system('color 2')
                print('Rate limited, wait some time to do requests again.')
                break
            exit()
        elif "success" in data:
            os.system('title Submits: {} && color b'.format(tries))
            print('Submitted question: {} '.format(question))

def main():
    spam()
if __name__ == "__main__":
    main()
