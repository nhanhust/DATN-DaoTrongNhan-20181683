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
#pragma once
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

#include <string>
/*
 *   The color loops every 27 times,
 *    because each channel of RGB loop in sequence of "0, 127, 254"
 */

static cv::Scalar getColor(int label) {
  int c[3];
  if (label == 0) return cv::Scalar(0, 0, 255);
  else if (label == 1) return cv::Scalar(0, 255, 0);
  else if (label == 2) return cv::Scalar(0, 255, 255);
  else
  {
	for (int i = 1, j = 0; i <= 9; i *= 3, j++) {
		c[j] = ((label / i) % 3) * 127;
	}
	return cv::Scalar(c[2], c[1], c[0]);
  }
}

// static cv::Mat process_result(cv::Mat &image,
//                               const vitis::ai::YOLOv3Result &result,
//                               bool is_jpeg) {
//   // for (const auto bbox : result.bboxes) {
//   //   int label = bbox.label;
//   //   float xmin = bbox.x * image.cols ;
//   //   float ymin = bbox.y * image.rows ;
//   //   float xmax = xmin + bbox.width * image.cols;
//   //   float ymax = ymin + bbox.height * image.rows;
//   //   float confidence = bbox.score;
//   //   if (xmax > image.cols) xmax = image.cols;
//   //   if (ymax > image.rows) ymax = image.rows;
//   //   LOG_IF(INFO, is_jpeg) << "RESULT: " << label << "\t" << xmin << "\t" << ymin
//   //                         << "\t" << xmax << "\t" << ymax << "\t" << confidence
//   //                         << "\n";
//   //   cv::rectangle(image, cv::Point(xmin, ymin), cv::Point(xmax, ymax),
//   //                 getColor(label), 1, 1, 0);
//   // }
//   return image;
// }


namespace vitis 
{
  namespace ai 
  {

    struct yolo_datn 
    {
      static std::unique_ptr<yolo_datn> create(std::string model);
      yolo_datn(std::string model);
      std::vector<vitis::ai::YOLOv3Result> run(const cv::Mat  &image);

      int getInputWidth();
      int getInputHeight();
      size_t get_input_batch();

    private:
      std::unique_ptr<vitis::ai::YOLOv3> yolov3_model_facemask_;
    };

    std::unique_ptr<yolo_datn> yolo_datn::create(std::string model) 
    {
      return std::unique_ptr<yolo_datn> (new yolo_datn(model));
    }

    int yolo_datn::getInputWidth() { return yolov3_model_facemask_->getInputWidth(); }
    int yolo_datn::getInputHeight() { return yolov3_model_facemask_->getInputHeight(); }
    size_t yolo_datn::get_input_batch() { return yolov3_model_facemask_->get_input_batch(); }

    yolo_datn::yolo_datn(std::string model)
    {
      yolov3_model_facemask_ = vitis::ai::YOLOv3::create(model,true);
    }

    std::vector<vitis::ai::YOLOv3Result> yolo_datn::run(const cv::Mat &image) 
    {
      std::vector<vitis::ai::YOLOv3Result> mt_results;
      cv::Mat image_facemask = image;
      // DPU time
	    // float dpu_time = 0.0;
      // Get start time for performance evaluation
    	// auto t_start = chrono::high_resolution_clock::now();
      // // Get start DPU time
    	// auto t_dpu_1 = chrono::high_resolution_clock::now();
      
      auto yolov3_model_facemask_results = yolov3_model_facemask_->run(image_facemask);
      // // Get end DPU time
	    // auto t_dpu_2 = chrono::high_resolution_clock::now();
      // // Get DPU delta execution
	    // dpu_time += (float) chrono::duration_cast<chrono::milliseconds>(t_dpu_2 - t_dpu_1).count();
      
      for (const auto bboxes_facemask : yolov3_model_facemask_results.bboxes) 
      {
        std::string label_facemask;
        if (bboxes_facemask.label == 0) label_facemask = "nomask";
        else if (bboxes_facemask.label == 1) label_facemask = "mask";
        else if (bboxes_facemask.label == 2) label_facemask = "incorrect";

        auto bbox_facemask = cv::Rect{
                                        (int)(bboxes_facemask.x * image_facemask.cols),
                                        (int)(bboxes_facemask.y * image_facemask.rows),
                                        (int)(bboxes_facemask.width  * image_facemask.cols),
                                        (int)(bboxes_facemask.height * image_facemask.rows)
                                      };

        // LOG_IF(INFO, is_jpeg) << "RESULT: " << label << "\t" << xmin << "\t" << ymin
        //                       << "\t" << xmax << "\t" << ymax << "\t" << confidence
        //                       << "\n";
        cv::rectangle(image_facemask, bbox_facemask, getColor(bboxes_facemask.label), 1, 1, 0);
        cv::putText(image_facemask,label_facemask,cv::Point(bbox_facemask.x,bbox_facemask.y),cv::FONT_HERSHEY_SIMPLEX,0.5,
                                                      getColor(bboxes_facemask.label),1);
      }

      // auto t_end = chrono::high_resolution_clock::now();
      // auto duration = chrono::duration_cast<chrono::milliseconds>(t_end - t_start).count();
      // cout << "\n-----------------------------------------" << endl;  
      // cout << "Processing time : " << duration << " ms" << endl; 
      // float perfs =  1.0 / duration * 1000;
      // cout << "Performances : " << perfs << " fps" << endl;       
      // cout << "Execution time on DPU : " << dpu_time << " ms" << endl;
      mt_results.emplace_back(yolov3_model_facemask_results);
      return mt_results;
    }

  } // namespace ai
} // namespace vitis
