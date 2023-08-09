#!/bin/bash

# Check if the model file name and decrease value are provided as command-line arguments
if [ $# -ne 3 ]; then
  echo "Usage: $0 <model_file> <decrease_value_nms> <decrease_value_conf>"
  exit 1
fi

# Get the model file name, decrease value for nms_threshold, and decrease value for conf_threshold from the command-line arguments
model_file="$1"
# decrease_value_nms="$2"
# decrease_value_conf="$3"

# # Create arrays of nms_threshold and conf_threshold values in decreasing order
# nms_thresholds=(0.65)
# conf_thresholds=(0.5)

# # Calculate the nms_threshold values based on the decrease_value_nms
# while (( $(echo "${nms_thresholds[-1]} > 0.2" | bc -l) )); do
#   nms_value=$(echo "${nms_thresholds[-1]} - $decrease_value_nms" | bc -l)
#   nms_thresholds+=($nms_value)
# done

# # Calculate the conf_threshold values based on the decrease_value_conf
# while (( $(echo "${conf_thresholds[-1]} > 0.2" | bc -l) )); do
#   conf_value=$(echo "${conf_thresholds[-1]} - $decrease_value_conf" | bc -l)
#   conf_thresholds+=($conf_value)
# done

#tu viet
model_filename=$(basename "$model_file" .prototxt)
# base_name="${file_name%.*}"

# nms_thresholds=(0.65 0.6 0.55 0.5 0.45 0.4 0.35 0.3)
# conf_thresholds=(0.65 0.6 0.55 0.5 0.45 0.4 0.35 0.3 0.25 0.2 0.15 0.1)

nms_thresholds=(${2//,/ })
conf_thresholds=(${3//,/ })

#---------------------------------------------------------------------
# Loop through the arrays and execute the command for each combination of nms_threshold and conf_threshold
for nms_value in "${nms_thresholds[@]}"; do
  for conf_value in "${conf_thresholds[@]}"; do
    # Save the modified content back to the original model file
    # echo "$modified_content" > "$model_file"
    # echo "ahihi"
    # echo "$model_filename"
    # echo iou = 0.5 map
    # python  scripts/evaluation.py -gt_file result/labels_anchors.txt -result_file version1/"$model_filename"_"$conf_value"_"$nms_value".txt -detection_iou 0.5 -detection_thresh "$conf_value"
    # echo iou = 0.25 map
    python  scripts/evaluation.py -gt_file result/labels_anchors.txt -result_file version1/"$model_filename"_"$conf_value"_"$nms_value".txt -detection_iou 0.25 -detection_thresh "$conf_value"
    # echo iou = 0.5
    # python  scripts/evaluation1.py -detection_metric pr -gt_file result/labels_anchors.txt -result_file version1/"$model_filename"_"$conf_value"_"$nms_value".txt -detection_iou 0.5 -detection_thresh "$conf_value"
    # echo iou = 0.25
    python  scripts/evaluation1.py -detection_metric pr -gt_file result/labels_anchors.txt -result_file version1/"$model_filename"_"$conf_value"_"$nms_value".txt -detection_iou 0.25 -detection_thresh "$conf_value"
    echo "$model_filename"_"$conf_value"_"$nms_value".txt evaluated!
  done
done
