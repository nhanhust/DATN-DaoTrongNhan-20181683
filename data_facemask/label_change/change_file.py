import os

folder_path = input("thu muc: ").strip()
# folder_path = '/đường_dẫn_đến_thư_mục'  # Thay thế bằng đường dẫn đến thư mục của bạn
old_string = '.jpg'  # Chuỗi cần thay thế
new_string = '-jpg'  # Chuỗi mới

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    file_name, file_extension = os.path.splitext(filename)

    if old_string in file_name:
        new_file_name = file_name.replace(old_string, new_string)
        new_file_path = os.path.join(folder_path, new_file_name + file_extension)
        os.rename(file_path, new_file_path)
        print(f"Đã đổi tên tệp tin: {filename} -> {new_file_name + file_extension}")
