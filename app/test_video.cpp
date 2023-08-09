/*
 * Copyright 2019 Xilinx Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#include <glog/logging.h>

#include <iostream>
#include <memory>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <vitis/ai/demo.hpp>
#include <vitis/ai/nnpp/yolov3.hpp>
#include <vitis/ai/yolov3.hpp>

#include "./process_result.hpp"
static cv::Mat process_result_datn(cv::Mat &image,
                              const std::vector<vitis::ai::YOLOv3Result> &result,
                              bool is_jpeg) {
  // for (const auto bbox : result.bboxes) {
  //   int label = bbox.label;
  //   float xmin = bbox.x * image.cols ;
  //   float ymin = bbox.y * image.rows ;
  //   float xmax = xmin + bbox.width * image.cols;
  //   float ymax = ymin + bbox.height * image.rows;
  //   float confidence = bbox.score;
  //   if (xmax > image.cols) xmax = image.cols;
  //   if (ymax > image.rows) ymax = image.rows;
  //   LOG_IF(INFO, is_jpeg) << "RESULT: " << label << "\t" << xmin << "\t" << ymin
  //                         << "\t" << xmax << "\t" << ymax << "\t" << confidence
  //                         << "\n";
  //   cv::rectangle(image, cv::Point(xmin, ymin), cv::Point(xmax, ymax),
  //                 getColor(label), 1, 1, 0);
  // }
  return image;
}

// extern int GLOBAL_ENABLE_NEW_IOU;
using namespace std;
int main(int argc, char* argv[]) {
  string model = argv[1];
  // GLOBAL_ENABLE_NEW_IOU = 1;
  vitis::ai::main_for_video_demo(
      argc, argv, [model] { return vitis::ai::yolo_datn::create(model); },
      process_result_datn, 2);
      return 0;
}
