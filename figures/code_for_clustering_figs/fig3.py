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
        

def plot_kmeans(data, k, y, mu, name):
    fig = plt.figure()
    colors = np.array([[216, 27, 96], [30, 136, 229], [255, 193, 7], [0, 77, 64], [50, 69, 125]])/255
    for j in range(k):
        plt.scatter(data[y==j,0], data[y==j,1], color=colors[j], s=20)
        plt.scatter(mu[j,0], mu[j,1], marker='X', color=colors[j], s=200, edgecolors='w', linewidth=5)
        plt.scatter(mu[j,0], mu[j,1], marker='X', color=colors[j], s=200, edgecolors='k', linewidth=2)
    plt.xlabel('x1',fontsize=20)
    plt.ylabel('x2',fontsize=20)
    plt.savefig(name)

def kmeans(k,T,data):
    # run k-means
    mu = np.random.randn(k,2)*4 # init
    y = np.random.randint(k,size=data.shape[0]) # init
    for t in range(T):
        y_old = y
        
        # assign
        for i in range(data.shape[0]):
            dists = np.zeros((data.shape[0],k))
            for j in range(k):
                dists[:,j] = ((data - mu[j,:])**2).sum(axis=1)
            y = dists.argmin(axis=1)
        
        # update means
        for j in range(k):
            if (y==j).any():
                mu[j,:] = data[y==j,:].mean(axis=0)
        
        if (y==y_old).all():
            print('converged')
            break
    return y, mu

T = 100
k = 4
y, mu = kmeans(k,T,data)
plot_kmeans(data, k, y, mu, './fig3_k=4.pdf')
k = 5
y, mu = kmeans(k,T,data)
plot_kmeans(data, k, y, mu, './fig3_k=5.pdf')