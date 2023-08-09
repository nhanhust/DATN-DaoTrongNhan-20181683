import os

def find_and_delete_file(folder_path, file_name):
    # Lấy danh sách tất cả các tệp trong thư mục
    files = os.listdir(folder_path)

    # Tìm kiếm tên tệp trong danh sách
    for file in files:
        if file[:file.find(".rf.")] == file_name[:file_name.find(".rf.")] and file.endswith(('.xml', '.txt', '.jpg')):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            # print("Đã xóa tệp:", file)

# Ví dụ sử dụng
# path_input_file = input("file chuan: ").strip()
path_input_file = "/home/nhan/Downloads/data_facemask/new_data/mask_label.v5i.voc(v2 xoay anh va them anh xin hon)/train"
folder_path = input("file xoa: ").strip()  # Thay thế bằng đường dẫn thư mục thực tế
# file_name = "example.txt"  # Thay thế bằng tên tệp bạn đang tìm


end_of_file = '.jpg'

files = []
for filename in os.listdir(path_input_file):
    if filename.endswith(end_of_file):

        find_and_delete_file(folder_path, filename)
