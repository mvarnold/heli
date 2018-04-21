from keras import backend as K
from keras.utils.generic_utils import get_custom_objects
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from unidecode import unidecode
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import io
import docopt

data = np.genfromtxt('dataShuffled.csv',dtype=float, delimiter=',')
input_data = data[:,0:4]
output_data = data[:,4:6]
print()
print(np.shape(data))
print()
model = Sequential()
model.add(Dense(10,input_shape=(4,)))
model.add(Dense(10))
def custom_activation(x):
    return (K.tanh(x/8) *24)

get_custom_objects().update({'custom_activation': Activation(custom_activation)})

model.add(Dense(2,activation=custom_activation))

model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])

history = model.fit(input_data[:5000000],output_data[:5000000],
	epochs = 3,
	verbose=1,
	validation_data =(input_data[5000000:],output_data[5000000:]))
model.save_weights("twolayer_railed")
plt.plot(history.history['loss'],'o')
plt.title("Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.savefig("heli.pdf")
