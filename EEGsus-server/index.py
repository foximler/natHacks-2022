import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
  '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

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
  sio.emit('clientPlay', data-1)
if __name__ == '__main__':
  eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
