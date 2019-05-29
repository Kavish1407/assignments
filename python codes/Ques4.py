import threading


def printline(filename):
    with open(filename,"r") as f:
        flist=f.readlines()
        #for i in flist:
        #   print(i)
        print(flist[len(flist)-2])

thread1 = threading.Thread(target=printline, args=("file1.txt",))
thread2 = threading.Thread(target=printline, args=("file2.txt",))
thread3 = threading.Thread(target=printline, args=("file3.txt",))
thread1.start()
thread2.start()
thread3.start()
