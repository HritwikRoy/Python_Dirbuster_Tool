import requests
import threading


try:


    ip_address = input("Enter full URL ( ex=https://hackstarswebtechnology.com )  :")

    f = open("text.txt", "r")
    for x in f:
        main_address=(ip_address+"/"+x.replace('\n', ''));
        req = requests.get(main_address)
        def dir_print():
            #print(req.status_code)
            #print(req.url)
            if (req.status_code==200):
                print(req.status_code)
                print(req.url)


        t1=threading.Thread(target=dir_print)

        t1.start()

        #dir_print()

except:
    print("Enter Valid URL .....")
