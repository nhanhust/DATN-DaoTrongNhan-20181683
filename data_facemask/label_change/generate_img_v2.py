
import os

path_input_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/train'
path_output_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/train.txt'
end_of_file = '.txt'

name_of_path_for_output_file = 'data/obj/'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        files.append("" + filename)

files = sorted(files)
files = [os.path.splitext(filename)[0] for filename in files]

with open(path_output_file, "w") as outfile:
    for file in files:
        outfile.write(name_of_path_for_output_file + file + "\n")
    outfile.close()

# --------------------------------------------------------------------------
path_input_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/val'
path_output_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/val.txt'
end_of_file = '.txt'

name_of_path_for_output_file = 'data/obj/'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        files.append("" + filename)

files = sorted(files)
files = [os.path.splitext(filename)[0] for filename in files]

with open(path_output_file, "w") as outfile:
    for file in files:
        outfile.write(name_of_path_for_output_file + file + "\n")
    outfile.close()

# --------------------------------------------------------------------------
path_input_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/test'
path_output_file = '/home/nhan/Downloads/data_facemask/YOLODataset/labels/test.txt'
end_of_file = '.txt'

name_of_path_for_output_file = 'data/obj/'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        files.append("" + filename)

files = sorted(files)
files = [os.path.splitext(filename)[0] for filename in files]

with open(path_output_file, "w") as outfile:
    for file in files:
        outfile.write(name_of_path_for_output_file + file + "\n")
    outfile.close()
