import os
import json

# path luu anh voi json
path = '/home/nhan/Downloads/img_facemask_all/public_test/archive/images'
classes = {'face_mask': 'mask', 'face': 'nomask', 'with_mask': 'mask', 'without_mask': 'nomask', 'mask_weared_incorrect': 'incorrect'} # class label

for item in os.listdir(path):
  if('.json') in item:
    with open(path + '/' + item, "r") as jsonFile:
      jsonFile = open(path + '/' + item)
      data = json.load(jsonFile)
      for shape in data['shapes']: shape['label'] = classes[shape['label']]
    with open(path + '/test/' + item, "w") as jsonFile:
      json.dump(data, jsonFile, indent=2)
    # for i in range(len(data['shapes'])):
    #   label = data['shapes'][i]['label']
    #   data['shapes'][i]['label'] = classes[label]
