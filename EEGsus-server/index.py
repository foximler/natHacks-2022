import eventlet
import socketio
import tensorflow
import numpy
import numpy as np
#### input_shape = (numpy array from raw)
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import datasets, layers, models
import pywt
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
  '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
#load test numpy array to suppliment live values
with open('values.npy', 'rb') as f:
    data={}
    data[1] = np.load(f,allow_pickle=True)
    data[2] = np.load(f,allow_pickle=True)
    data[3] = np.load(f,allow_pickle=True)
    data[4] = np.load(f,allow_pickle=True)
    data[5] = np.load(f,allow_pickle=True)

@sio.event
def connect(sid, environ):
  print('connect ', sid)

@sio.event
def changePage(sid, data):
  print('page change requested ', data)

@sio.event
def disconnect(sid):
  print('disconnect ', sid)

@sio.event
def playSound(sid,data):
  print(data)
  sio.emit('indexPlay', data-1)

@sio.event
def playSentence(sid,data):
  print(data)
  sio.emit('instructionPlay', data)

@sio.event
def feedModel(sid,input):
  dataHandler(data[input][:,:271])
  
def dataHandler(data):
  model = create_model()
  model.load_weights('./model')
  coef, freqs = pywt.cwt(data,len(data),'morl',method='fft')
  modelOut = model.predict( np.expand_dims(min_max_scaler.fit_transform(coef[0]), axis=0))
  sio.emit("wsUpdate",{'intput':str(np.argmax(modelOut[0])),'confidence':str(np.max(modelOut[0]))})

def create_model():
  model = models.Sequential()
  batches = 14
  #model.add(layers.Conv2D(filters = 2,  kernel_size = (1,2), strides= (1,1), activation = 'relu', dilation_rate = 2, input_shape = [135, 14 , 1]))
  #model.add(layers.Conv2D(filters = 2, kernel_size = (1,2), strides = (1,1), activation = 'relu', dilation_rate = 2))

  model.add(layers.DepthwiseConv2D(kernel_size = (1,2), strides= 2, activation = 'relu', padding = 'same', depth_multiplier = 8, input_shape = [5,271,1]))
  model.add(layers.DepthwiseConv2D(kernel_size = (1,2), strides = 2, activation = 'relu', padding = 'same', depth_multiplier = 16))
  model.add(layers.MaxPooling2D(pool_size = (1,2), padding = 'same')) #play around with pool_size 
  model.add(layers.Flatten())
  model.add(layers.Dense(128, activation = 'relu')) #128
  model.add(layers.Dense(32, activation = 'relu'))
  model.add(layers.Dense(16, activation = 'relu'))
  model.add(layers.Dense(10, activation = 'softmax'))
  patience=2
  optimizer = tf.keras.optimizers.Adam()
  loss = tf.keras.losses.CategoricalCrossentropy()
  metrics = ['val_loss']
  accuracy = tf.keras.metrics.CategoricalAccuracy()
  model.compile(loss = loss, optimizer = optimizer,
      metrics=[
          tf.keras.metrics.MeanSquaredError(), 'accuracy'],)
  return model
if __name__ == '__main__':
  eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)
