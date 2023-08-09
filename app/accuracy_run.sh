chmod +x ./accuracy.sh
#nms #conf
# # 0.45 0.3
# echo yolov3
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov3_facemask_acc/dpu_yolov3_facemask_acc.prototxt 0.4 0.3,0.25,0.2,0.15,0.1,0.05
# echo "3-2"
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov3_facemask_acc/dpu_yolov3_facemask_acc.prototxt 0.45,0.4,0.35,0.3,0.25,0.2 0.25
# # 0.6 0.3
# echo yolov4
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov4_facemask_acc/dpu_yolov4_facemask_acc.prototxt 0.55 0.3,0.25,0.2,0.15,0.1,0.05
# echo "4-2"
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov4_facemask_acc/dpu_yolov4_facemask_acc.prototxt 0.6,0.55,0.5,0.45,0.4,0.35 0.25
# # 0.65 0.5
# echo yolov5m
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov5m_facemask_acc/dpu_yolov5m_facemask_acc.prototxt 0.6 0.5,0.45,0.4,0.35,0.3,0.25
# echo "5-2"
# ./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov5m_facemask_acc/dpu_yolov5m_facemask_acc.prototxt 0.65,0.6,0.55,0.5,0.45,0.4 0.45
# echo "done"

#nms #conf
# 0.35 0.15
echo yolov3
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov3_facemask_acc/dpu_yolov3_facemask_acc.prototxt 0.35 0.2,0.15,0.1
# 0.4 0.2
echo yolov4
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov4_facemask_acc/dpu_yolov4_facemask_acc.prototxt 0.4 0.25,0.2,0.15
# 0.45 0.25
echo yolov5m
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov5m_facemask_acc/dpu_yolov5m_facemask_acc.prototxt 0.45 0.3,0.25,0.2
echo "done"

#nms #conf
# 0.35 0.15
echo yolov3-tiny
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov3-tiny_facemask_acc/dpu_yolov3-tiny_facemask_acc.prototxt 0.35 0.2,0.15,0.1
# 0.4 0.2
echo yolov4-tiny
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov4-tiny_facemask_acc/dpu_yolov4-tiny_facemask_acc.prototxt 0.4 0.25,0.2,0.15
# 0.45 0.25
echo yolov5s
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov5s_facemask_acc/dpu_yolov5s_facemask_acc.prototxt 0.45 0.3,0.25,0.2
echo yolov5n
./accuracy.sh /usr/share/vitis_ai_library/models/dpu_yolov5n_facemask_acc/dpu_yolov5n_facemask_acc.prototxt 0.45 0.3,0.25,0.2
echo "done"

