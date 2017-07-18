import threading





def counter(thread_id, counter_limit):
    global l
    global i
    l.acquire()
    for u in range(counter_limit):
        temp = i
        temp += 1
        i = temp
        print("Thread #" + str("%02i" % thread_id) + " Counter is at " + str(i) + "\n", end = "", sep = "")
    l.release()




i = 0
p = 0

l = threading.Lock()

counter_limit = int(input("Counter Limit: "))
for p in range(counter_limit):
    thread = threading.Thread(target = counter, args = (i, counter_limit))
    thread.start()

