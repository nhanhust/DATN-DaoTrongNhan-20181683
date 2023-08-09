
// #include <fstream>
#include <iostream>
// #include <chrono>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <vitis/ai/yolov3.hpp>  

#include <filesystem>

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

bool getFilesFromFolder(std::string folderPath, std::vector<std::string> &fileNames) 
{
	// Reset list content
	fileNames.clear();
	// Check whether folder exists
	if(std::filesystem::exists(folderPath)) 
	{
		// Process folder content
		for (const auto& entry : std::filesystem::directory_iterator(folderPath)) 
		{
			fileNames.push_back(entry.path().filename().string());
		}
		return true;
	}
	else 
	{
		std::cout << "The specified folder " <<  folderPath << " does not exist." << std::endl;
		return false;
	}		
}

int main(int argc, char** argv) 
{

	const std::string model_name = argv[1];
	const std::string input_folder = argv[2];
	const std::string output_folder = argv[3];
	// const std::string output_file = argv[4];

	std::vector<std::string> image_names;
	if (!getFilesFromFolder(input_folder, image_names)) 
	{
		return EXIT_FAILURE;
	}
	auto nb_images = image_names.size();
	if(nb_images == 0) 
	{
		std::cerr << "No images to process from specified input data folder " << input_folder << ". Exiting program..." << std::endl;
		return EXIT_FAILURE;
	}

    // std::ofstream file;
    // file.open(output_file);

	auto yolov3_model_facemask_ = vitis::ai::YOLOv3::create(model_name, true);
	
	for (auto image_file_name : image_names)
	{
		cv::Mat image_facemask = cv::imread(input_folder + "/" + image_file_name, cv::IMREAD_COLOR);
		// std::cout << "Image " << image_file_name << " :" << std::endl;
		//out_file << "Image " << name << " :" << endl;

		// Check whether image has been successfully loaded
		// if (image_facemask.empty()) {
		// 	std::cout << "Failed to load image " << image_file_name << std::endl; 
		// 	// Proceed to next image
		// 	break;	
		// }
	
		// DPU time
		// float dpu_time = 0.0;
		// Get start time for performance evaluation
		// auto t_start = std::chrono::high_resolution_clock::now();

		// Get start DPU time
		// auto t_dpu_1 = std::chrono::high_resolution_clock::now();
		auto yolov3_model_facemask_results = yolov3_model_facemask_->run(image_facemask);
		// Get end DPU time
		// auto t_dpu_2 = std::chrono::high_resolution_clock::now();
		
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

		// auto t_end = std::chrono::high_resolution_clock::now();
		// std::cout << "\n-----------------------------------------" << std::endl;
		// // Get DPU delta execution
		// float dpu_time = (float) std::chrono::duration_cast<std::chrono::milliseconds>(t_dpu_2 - t_dpu_1).count();
		// std::cout << "Execution time on DPU : " << dpu_time << " ms" << std::endl;
		
		// Display FPS
		// dpu_time += (float) chrono::duration_cast<chrono::milliseconds>(t_dpu_2 - t_dpu_1).count();
		// float perfs =  roundf((nb_images / (float) (dpu_time / 1000.0)) * 100.0) / 100.0;
		// cout << "Performances : " << perfs << " fps" << endl;       
		// cout << "Execution time on DPU : " << dpu_time << " ms" << endl;

		// auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t_end - t_start).count();
		// std::cout << "Processing time : " << duration << " ms" << std::endl; 

		// float perfs =  1.0 / duration * 1000;
		// std::cout << "Performances : " << perfs << " fps" << std::endl;       

		auto out_file =	image_file_name.substr(0, image_file_name.size() - 4) + "_result.jpg";
		//tao file anh ket qua
		cv::imwrite(output_folder + "/" + out_file, image_facemask);
	}
	return EXIT_SUCCESS;
}
