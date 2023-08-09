import xml.etree.ElementTree as ET
import os
import shutil

def check_label(xml_file, label):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for obj in root.findall('object'):
        name = obj.find('name').text
        if name == label:
            return True

    return False

# Provide the XML file path and the label to check
# xml_file = 'path/to/your/xml/file.xml'
label = '14'

# Check if the label is present in the XML file
# is_present = check_label(xml_file, label)

# if is_present:
#     print(f"The label '{label}' is present in the XML file.")
# else:
#     print(f"The label '{label}' is not present in the XML file.")


path_input_file = input("duong dan thu muc chua cac file xml: ").strip()
path_outnput_file = input("duong dan thu muc chua cac file moi:  ").strip()

end_of_file = '.xml'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):
        if check_label(path_input_file + os.sep + filename, label):
            shutil.copy2(path_input_file + os.sep + filename, path_outnput_file + os.sep + filename)
            image_name = filename.replace('xml', 'jpg')
            shutil.copy2(path_input_file + os.sep + image_name, path_outnput_file + os.sep + image_name)