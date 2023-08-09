import os

def delete_files_with_extension(folder_path, extension):
    # Lấy danh sách tệp trong thư mục
    files = os.listdir(folder_path)

    # Xóa các tệp với phần mở rộng tùy chọn
    for file in files:
        if file.endswith(extension):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print("Đã xóa tệp:", file)

# Ví dụ sử dụng

folder_path = input("thu muc: ").strip()
# folder_path = "/đường/dẫn/đến/thư/mục"  # Thay thế bằng đường dẫn thư mục thực tế
extension = ".xml"  # Phần mở rộng tệp

delete_files_with_extension(folder_path, extension)
