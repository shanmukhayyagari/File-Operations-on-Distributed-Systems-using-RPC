from glob import glob
from importlib.resources import path
from xmlrpc.server import SimpleXMLRPCServer
import sys, xmlrpc, os
import time, random
import multiprocessing, sys
import func_timeout
from pathlib import Path
from datetime import datetime




node1 = SimpleXMLRPCServer(('localhost', 10001), logRequests = True, allow_none = True)




class Node1:

    path = "node1.log"
    f=open(path,"a")


    p = 0
    list1 = []
    x = 1
    ye = 0
    i = 0
#     x = random.randint(0, 1)
    def timer(self,h):
        path = "node1.log"
        f=open(path,"a")
        list1 = []
        global i
        self.i = h
        print("linked----->coordinator")
        now = datetime.now()
        list1.append("linked----->coordinator"+now.strftime("%d-%m-%Y %H:%M:%S"))
        print("Preparation----->Awaiting...")
        now = datetime.now()
        list1.append(("Preparation----->Awaiting..."+now.strftime("%d-%m-%Y %H:%M:%S")))
        
        if h>10:
            global x
            self.x = 0
        for i in list1:
            f.write("\n")
            f.write(i)
    def set(self):
        path = "node1.log"
        f=open(path,"a")
        list1 = []
        global x
        global i 
        if self.i>10:
            print("Coordinator----->didnt send prepare yet.... so----->aborting")
            now = datetime.now()
            list1.append("Coordinator----->didnt send prepare yet.... so----->aborting"+now.strftime("%d-%m-%Y %H:%M:%S"))
            print("Transaction----->Aborted")
            now = datetime.now()
            list1.append("Transaction----->Aborted"+now.strftime("%d-%m-%Y %H:%M:%S"))

            print("Sent----->no to prepare....coordinator-----> too long to send prepare")
            now = datetime.now()
            list1.append("Sent----->no to prepare....coordinator-----> too long to send prepare"+now.strftime("%d-%m-%Y %H:%M:%S"))
        else:
            print("received----->preparation")
            now = datetime.now()
            list1.append("received----->preparation"+now.strftime("%d-%m-%Y %H:%M:%S"))
            
            start = time.time()





            time.sleep(1)







            elapse = time.time() - start
            if self.x != 0:
                print("Sent Yes after----->"+str(elapse)+" seconds")
                now = datetime.now()
                list1.append("Sent Yes after----->"+str(elapse)+" seconds"+now.strftime("%d-%m-%Y %H:%M:%S"))
                if elapse<10:
                    print("awaiting----->Commit...")
                    now = datetime.now()
                    list1.append("awaiting----->Commit..."+now.strftime("%d-%m-%Y %H:%M:%S"))
                else:
                    print("Voting took far too long... Transaction----->Aborting.")
                    now = datetime.now()
                    list1.append("Voting took far too long... Transaction----->Aborting."+now.strftime("%d-%m-%Y %H:%M:%S"))
                return self.x
            elif self.x == 0:
                print("Sent----->No")
                now = datetime.now()
                list1.append("Sent----->No"+now.strftime("%d-%m-%Y %H:%M:%S"))
                return 0
        for i in list1:
            f.write("\n")
            f.write(i)
    def commitment(self):
        path = "node1.log"
        f=open(path,"a")
        list1 = []
        global p
        global ye






        commitmentsleep = 11







        self.p = commitmentsleep
        print("Commit----->Received")
        now = datetime.now()
        list1.append("Commit----->Received"+now.strftime("%d-%m-%Y %H:%M:%S"))
        time.sleep(commitmentsleep)
        if commitmentsleep>10:
            print("slept too much after the request")
            now = datetime.now()
            list1.append("slept too much after the request"+now.strftime("%d-%m-%Y %H:%M:%S"))
            self.ye = 5
            
        else:
            print("Sent----->Committed")
            now = datetime.now()
            list1.append("Sent----->Committed"+now.strftime("%d-%m-%Y %H:%M:%S"))
            print("Waiting----->Transaction Result....")
            now = datetime.now()
            list1.append("Waiting----->Transaction Result...."+now.strftime("%d-%m-%Y %H:%M:%S"))
        for i in list1:
            f.write("\n")
            f.write(i)    
        return 1
   
    def success(self, list):
        list1 = []
        path = "node1.log"
        f=open(path,"a")
        if self.p>10 and self.ye == 5:
                print("I waited too long to send the commit, thus I'm asking TC for transaction details.")
                now = datetime.now()
                f.write("I waited too long to send the commit, thus I'm asking TC for transaction details."+now.strftime("%d-%m-%Y %H:%M:%S"))
                print("----------Begin----->transaction information----------")
                now = datetime.now()
                f.write("----------Begin----->transaction information----------\n\n\n"+now.strftime("%d-%m-%Y %H:%M:%S"))
                for i in list:
                    print("\n")
                    print(i)

                for i in list:
                    f.write("\n")
                    f.write(i)
                # for i in list1:
                #     print("\n")
                #     print(i)
                print("----------End----->transaction information----------\n\n\n")
                now = datetime.now()
                f.write("----------End----->transaction information----------\n\n\n"+now.strftime("%d-%m-%Y %H:%M:%S"))
        print("Transaction----->Successful")
        now = datetime.now()
        list1.append("Transaction----->Successful"+now.strftime("%d-%m-%Y %H:%M:%S"))
        for i in list1:
            f.write("\n")
            f.write(i)
    def failure(self, list, list2):
        list1 = []
        path = "node1.log"
        f=open(path,"a")
        global p
        global i
        global ye
        if  self.i<10:
            
            print("Transaction----->Aborting..")
            now = datetime.now()
            list1.append("Transaction----->Aborting.."+now.strftime("%d-%m-%Y %H:%M:%S"))
        for i in list1:
            f.write("\n")
            f.write(i)


node1.register_instance(Node1())




if __name__ == '__main__':
    try:
        print('Node1----->Active')
        
        node1.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')