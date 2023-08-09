import os
import shutil
import numpy as np
import pandas as pd

from tqdm import tqdm
from pathlib import Path

import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from collections import Counter

# label_dir = '/media/ductm/01D96A7484F6FCF0/train-colab/char/backup/darknet/data/valid'
label_dir = input("duong dan thu muc chua cac file txt: ").strip()
# label_list_file = input("duong dan file txt list cac file trong thu muc tren: ").strip()

# --------------------------------------------------------
# import os

# path_input_file = '/content/drive/MyDrive/yolov4/data/YOLODataset/images/train'
# path_output_file = '/content/drive/MyDrive/yolov4/prepare/train.txt'
end_of_file = '.txt'

name_of_path_for_output_file = 'train/'

path_input_file = label_dir
path_output_file = label_dir + '/train.txt'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        files.append("" + filename)

with open(path_output_file, "w") as outfile:
    for file in files:
        outfile.write(name_of_path_for_output_file + file + "\n")
    outfile.close()


label_dir = Path(label_dir)
label_list_file = Path(path_output_file)

sns.set(font_scale=1.3)
sns.set_style("darkgrid", {"axes.facecolor": ".95"})
# set fonttype
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype']  = 42

#%matplotlib inline


class_counter = {'train': Counter(), 'valid': Counter()}
class_freqs = {}
files_train = []
# files_valid = []
with open(label_list_file, 'r') as f:
    for line in f:
        newline = line.strip()
        files_train.append(newline)
        #image_id = line.split('/')[-1].split('.+?/(?=[^/]+$)')[-1]
        #basename = os.path.basename(line)
        #image_id = os.path.splitext(basename)[0]
        #df = np.loadtxt(label_dir / f'{image_id}.txt',ndmin=2)
        #class_counter['train'].update(df[:, 0].astype(int))
for fil in files_train:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]
    df = np.loadtxt(label_dir / f'{filename}.txt',ndmin=2)
    class_counter['train'].update(df[:, 0].astype(int))
# get class freqs
total = sum(class_counter['train'].values()) #tong so lan xuat hien
print("train")
for v in class_counter['train'].items():
    print(v)
print("\n")
class_freqs['train'] = {k: v / total for k, v in class_counter['train'].items()}


os.remove(path_output_file)

# label_dir = '/media/ductm/01D96A7484F6FCF0/train-colab/char/backup/darknet/data/valid'
        
# with open(Path('/media/ductm/01D96A7484F6FCF0/train-colab/char/backup/darknet/data') / 'valid.txt', 'r') as f:
#     for line in f:
#         newline = line.strip()
#         files_valid.append(newline)
#         # image_id = line.split('/')[-1].split('.+?/(?=[^/]+$)')[-1]
#         # basename = os.path.basename(line)
#         # image_id = os.path.splitext(basename)[0]
#         # df = np.loadtxt(label_dir / f'{image_id}.txt',ndmin=2)
#         # class_counter['valid'].update(df[:, 0].astype(int))
# for fil in files_valid:
#     basename = os.path.basename(fil)
#     filename = os.path.splitext(basename)[0]
#     #df = np.loadtxt(label_dir / f'{filename}.txt',ndmin=2)
#     df = np.loadtxt(label_dir / f'{filename}.txt',ndmin=2)
#     class_counter['valid'].update(df[:, 0].astype(int))
# # get class freqs
# total = sum(class_counter['valid'].values())
# print("valid\n")
# for v in class_counter['valid'].items():
#     print(v)
# print("\n")
# class_freqs['valid'] = {k: v / total for k, v in class_counter['valid'].items()}

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(range(3), [class_freqs['train'][i] for i in range(3)], color='navy', label='train');
# ax.plot(range(5), [class_freqs['valid'][i] for i in range(5)], color='tomato', label='valid');
ax.legend();
ax.set_xlabel('Class ID');
ax.set_ylabel('Class Frequency');
#plt.imshow(ax)
plt.show()
