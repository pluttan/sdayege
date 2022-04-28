from keras.datasets import mnist
 
#loading the dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()
 
from matplotlib import pyplot
for i in range(1000000):  
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(train_X[i], cmap=pyplot.get_cmap('gray'))
        print(train_X[i],train_y[i])
        pyplot.show()