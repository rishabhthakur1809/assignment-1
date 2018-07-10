#Question1
import numpy as np
a=np.random.random([10,1])
b=a.mean()
print(b)

#Question2
import numpy as np
a=np.random.random([20,1])
b=a.std()
print(b)

#Question3

import numpy as np
a=np.random.random([10,20])
print(a)
b=np.random.random([20,25])
print(b)
c=np.matmul(a,b)
print(c)
print(np.sum(c))


#Question4
import numpy as np
a=np.random.random([10,1])
b=np.empty([10,1])
for i in np.nditer(a,op_flags=['readwrite']):
    i[...] =1/(1+np.exp(-i))
print(b)


this is the class is the system to increase the async :
    print("this is the best ")