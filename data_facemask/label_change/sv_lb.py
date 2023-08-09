import os
import json

def save_labels(data, path):
  os.chdir(path)

  classes = {'nomask' : 0, 'mask': 1, 'incorrect' : 2, 'face_mask' : 1, 'face' : 0} # class label

  imgheight = data['imageHeight']
  imgweight = data['imageWidth']

  f = open(data['imagePath'].replace('.jpg', '') + '.txt', 'a')

  for i in range(len(data['shapes'])):
    label = data['shapes'][i]['label']
    [xmin, ymin], [xmax,ymax] = data['shapes'][i]['points']
    x_c = (xmin + xmax)/(2*imgweight)
    y_c = (ymin + ymax)/(2*imgheight)
    w = (xmax - xmin)/imgweight
    h = (ymax - ymin)/imgheight
    a = str(classes[label]) + ' ' + str(x_c)  + ' ' + str(y_c) + ' ' + str(w) + ' ' + str(h) + '\n'
    f.write(a)


# path luu anh voi json
path = 'D:/Pycharm/Nhan/yolov4_fmask/drive-download-20230528T013010Z-001/FPT_maskdata (json)/FPT_maskdata/dataset/images/train'

for item in os.listdir(path):
  if('.json') in item:
    f = open(path + '/' + item)
    data = json.load(f)
    save_labels(data, path)