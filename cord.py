from xmlrpc.client import ServerProxy
import sys, xmlrpc, os, socket
import time, logging
import multiprocessing, sys
import func_timeout
from pathlib import Path
from datetime import datetime




node1 = ServerProxy("http://localhost:10001", allow_none= True)
node2 = ServerProxy("http://localhost:10002", allow_none= True)




def Start():
    list = []
    list1 = []
    def positive():
        print("Transaction----->successful")
        now = datetime.now()
        list.append("Transaction----->Successful"+now.strftime("%d-%m-%Y %H:%M:%S"))
        node1.success(list)
        node2.success(list)
        path1 = "coordinate.log"
        with open(path1, 'a') as f:
                for ele in list:
                    f.write(f"{ele}\n")
    def negative():
        print("Transaction----->Aborted")
        now = datetime.now()
        list.append("Transaction----->Aborted"+now.strftime("%d-%m-%Y %H:%M:%S"))
        node1.failure(list, list1)
        node2.failure(list, list1)
        path1 = "coordinate.log"
        with open(path1, 'a') as f:
                for ele in list:
                    f.write(f"{ele}\n")
    
    print("Connected----->Node1")
    now = datetime.now()
    list.append("Connected----->Node1"+now.strftime("%d-%m-%Y %H:%M:%S"))
    print("Connected----->Node2")
    now = datetime.now()
    list.append("Connected----->Node2"+now.strftime("%d-%m-%Y %H:%M:%S"))
    def tccommit():
        listtt = [0,0]
        def commit1():
            listtt[0] = 1   
            b = 1
            a = node1.commitment()
            if a == 1:
                m = "FinalizeCommit----->received from node1 "
                now = datetime.now()
                list.append(m+now.strftime("%d-%m-%Y %H:%M:%S"))
                print(m)
            x = a
            return x
        def commit2():
            listtt[1] = 1   
            b = 1
            a = node2.commitment()
            if a == 1:
                m = "FinalizeCommit----->received from node2 "
                now = datetime.now()
                list.append(m+now.strftime("%d-%m-%Y %H:%M:%S"))
                print(m)
            x = a
            return x
        







        snoozebetweencommition = 1









        x = commit1()
        # y = commit2()
        m = "Sleeping for----->"+str(snoozebetweencommition)+" seconds"
        now = datetime.now()
        list1.append(m+now.strftime("%d-%m-%Y %H:%M:%S"))
        print(m)
        time.sleep(snoozebetweencommition)
        if listtt[0] == listtt[1] == 0:
            print("sent commit-----> none..,sending now")
            now = datetime.now()
            list.append("sent commit-----> none..,sending now"+now.strftime("%d-%m-%Y %H:%M:%S"))
            x = commit1()
            y = commit2()
        elif listtt[0] == 0:
            print("sent commit----->Node2, so sending node1")
            now = datetime.now()
            list.append("sent commit----->Node2, so sending node1"+now.strftime("%d-%m-%Y %H:%M:%S"))
            x = commit1()
        elif listtt[1] == 0:
            print("sent commit----->Node1, so sending node2")
            now = datetime.now()
            list.append("sent commit----->Node1, so sending node2"+now.strftime("%d-%m-%Y %H:%M:%S"))
            y = commit2()

        if x == y == 1:
            positive()
        
            
        
        
    
    def preparation():







        timetosleep = 1







        node1.timer(timetosleep)
        node2.timer(timetosleep)
        time.sleep(timetosleep)
        def big_function():
            print("Prepared----->sent to Node 1.")
            now = datetime.now()
            list.append("Prepared----->sent to Node 1."+now.strftime("%d-%m-%Y %H:%M:%S"))
            print("awaiting----->vote...")
            now = datetime.now()
            list.append("awaiting----->vote..."+now.strftime("%d-%m-%Y %H:%M:%S"))
            a = node1.set()
            return a
        def run_function(f, max_wait, default_value):
            try:
                return func_timeout.func_timeout(max_wait, big_function)
            except func_timeout.FunctionTimedOut:
                pass
            return default_value
        x = run_function(big_function, 10, 0)
        def big_function2():
            print("Prepared----->sent to Node 2.")
            now = datetime.now()
            list.append("Prepared----->sent to Node 2."+now.strftime("%d-%m-%Y %H:%M:%S"))
            print("awaiting----->vote...")
            now = datetime.now()
            list.append("awaiting----->vote..."+now.strftime("%d-%m-%Y %H:%M:%S"))
            b = node2.set()
            return b
        def execute_function2(f, max_wait, default_value):
            try:
                return func_timeout.func_timeout(max_wait, big_function2)
            except func_timeout.FunctionTimedOut:
                pass
            return default_value
        y = execute_function2(big_function2, 10, 0)
        z = 1
        if x == 1:
            print("Obtaining----->yes from Node1")
            now = datetime.now()
            list.append("Obtaining----->yes from Node1"+now.strftime("%d-%m-%Y %H:%M:%S"))
        else:
            print("Node1 responded with a no, or it took too long. Aborting the transaction as a result")
            now = datetime.now()
            list.append("Node1 responded with a no, or it took too long. Aborting the transaction as a result"+now.strftime("%d-%m-%Y %H:%M:%S"))
            try:
                negative()
                z = 0
            except Exception as e:
                print("Transaction----->Aborted")
                now = datetime.now()
                list.append("Transaction----->Aborted"+now.strftime("%d-%m-%Y %H:%M:%S"))
                z = 0
        if y == 1:
            print("Obtaining----->yes from Node2")
            now = datetime.now()
            list.append("Obtaining----->yes from Node1"+now.strftime("%d-%m-%Y %H:%M:%S"))
        else:
            print("Node2 responded with a no, or it took too long. Aborting the transaction as a result")
            now = datetime.now()
            list.append("Node2 responded with a no, or it took too long. Aborting the transaction as a result"+now.strftime("%d-%m-%Y %H:%M:%S"))
            try:
                negative()
            except Exception as e:
                print("Transaction----->Aborted")
                now = datetime.now()
                list.append("Transaction----->Aborted"+now.strftime("%d-%m-%Y %H:%M:%S"))        
        if x == 1 and y == 1:
            print("Proceeding----->Transaction")
            now = datetime.now()
            list.append("Proceeding----->Transaction"+now.strftime("%d-%m-%Y %H:%M:%S"))
            tccommit()
    preparation()



if __name__ =="__main__": 
    Start()