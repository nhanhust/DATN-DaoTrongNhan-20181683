import cv2

def extract_frames_from_video(input_video_path, output_folder, frames_per_second=5):
    # Đọc video
    video_capture = cv2.VideoCapture(input_video_path)

    # Kiểm tra xem video có thể mở thành công hay không
    if not video_capture.isOpened():
        print("Không thể mở video")
        return

    # Khởi tạo biến đếm số khung hình
    frame_count = 0
    frame_rate = int(video_capture.get(cv2.CAP_PROP_FPS))

    # Tính toán số khung hình cần nhảy qua giữa các khung hình (bước nhảy)
    frame_skip = frame_rate // frames_per_second

    # Lặp qua từng khung hình trong video
    while True:
        # Đọc một khung hình
        ret, frame = video_capture.read()

        # Nếu không thể đọc được khung hình, thoát khỏi vòng lặp
        if not ret:
            break

        # Lưu khung hình vào tệp mỗi khi số khung hình hiện tại là bội số của bước nhảy
        if frame_count % frame_skip == 0:
            # Tạo tên tệp cho khung hình hiện tại (ví dụ: frame_0.jpg, frame_1.jpg, ...)
            output_file = f"{output_folder}/frame_{frame_count}.jpg"

            # Lưu khung hình vào tệp
            cv2.imwrite(output_file, frame)

        # Tăng biến đếm số khung hình
        frame_count += 1

    # Giải phóng tài nguyên và đóng video
    video_capture.release()
    cv2.destroyAllWindows()

# Gọi hàm để cắt các khung hình từ video, lấy 5 khung hình trong mỗi giây
input_video_path = input("video:").strip()
output_folder = input("thu muc:").strip()
extract_frames_from_video(input_video_path, output_folder, frames_per_second=3)

