import matplotlib.pyplot as plt
import re

num = []
acc = []

"""
[0 0 0 4 1 2 1 1 0 1 0 1 0 3 0 3 1 1 5 3]
[0 0 1 4 1 1 0 4 0 1 1 0 1 1 0 0 0 1 1 3]
val_acc=0.8875
latency_sum=130.0000
"""

with open('train_batch_1_210119.log') as f:
    for st in f:
        if st.find('test_accuracy') != -1:
            num.append(len(num)+1)
            acc.append(float(re.search('0\.\d+', st)[0]))
            print(acc)

plt.plot(num,acc,'b')

num = []
acc = []

"""
[1 0 1 0 0 1 2 0 1 3 0 1 4 1 3 0 1 0 0 4]
[1 4 0 0 0 0 0 0 0 4 1 4 2 0 2 0 2 4 1 0]
val_acc=0.6944
latency_sum=84.0000
"""

with open('train_batch_2_210119.log') as f:
    for st in f:
        if st.find('test_accuracy') != -1:
            num.append(len(num)+1)
            acc.append(float(re.search('0\.\d+', st)[0]))
            print(acc)

plt.plot(num,acc,'r')

plt.axis([0,314,0.5,1.0])
plt.show()
