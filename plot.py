import matplotlib.pyplot as plt
import re

num = []
acc = []

with open('log_210113.log') as f:
    for st in f:
        if st.find('test_accuracy') != -1:
            num.append(len(num)+1)
            acc.append(float(re.search('0\.\d+', st)[0]))
            print(acc)

plt.plot(num,acc)
plt.axis([0,314,0.5,1.0])
plt.show()
