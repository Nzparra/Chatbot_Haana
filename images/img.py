from tkinter import *

imagelist = {
  'banner': ['banner.jpg', None],
  'Haanna': ['Haana.png', None],
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
      print('loading image:', name)
      imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None