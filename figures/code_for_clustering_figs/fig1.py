import numpy as np
import matplotlib.pyplot as plt


# set seed for reproducibility
np.random.seed(0)

# generate Gaussian data
mus = np.array([[-1,-2],[2,1],[-2,2],[1,0],[-1,1.5]])*4
data = None
for mu in mus:
    x = mu + np.random.randn(100,2)
    if data is None:
        data = x
    else:
        data = np.concatenate((data, x), axis=0) 

plt.scatter(data[:,0], data[:,1], color='k', s=20)
#plt.show()
plt.xlabel('x1',fontsize=20)
plt.ylabel('x2',fontsize=20)
plt.savefig('./fig1.pdf')