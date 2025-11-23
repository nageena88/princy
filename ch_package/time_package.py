# import time

# t1 = time.time()
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# for i in range(3):
#     print(i)
#     time.sleep(1)
# print(time.localtime(320))

# print(time.asctime(time.localtime(320)))
# print(time.asctime((2025, 1, 1, 0, 0, 0, 0, 0, 0)))
# print(time.time() - t1)
# # get the process time of the current program
# # print(time.process_time())

from datetime import datetime

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.strftime("%Y-%m-%d->%H:%M:%S"))
