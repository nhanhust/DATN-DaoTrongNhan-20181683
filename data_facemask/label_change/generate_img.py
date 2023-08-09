import os

path_input_file = '/home/nhan/Downloads/data_facemask/YOLODataset/calib/images'
path_output_file = '/home/nhan/Downloads/data_facemask/YOLODataset/calib/calib.txt'

end_of_file = '.jpg'

name_of_path_for_output_file = ''

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        files.append("" + filename)

with open(path_output_file, "w") as outfile:
    for file in files:
        outfile.write(name_of_path_for_output_file + file + "\n")
    outfile.close()