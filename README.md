
# The-Gatherer-2.0
You can still access the previous version by changing the branch on Github.

This was made using YOLOv5 and OpenCV. The model is now comaptible with CPU and GPU and it detects automaticly the best option for your computer. You can load your custom YOLO models (exported to **ONNX**) by using your own .onnx file.

On how to use your own data set to train a custom model, for now I'ld recomend following this tutorial for custom training. [https://www.youtube.com/watch?v=GRtgLlwxpc4](https://www.youtube.com/watch?v=GRtgLlwxpc4). I'm also uploading very soon a simple guide to export your .pt model to .onnx so it can run in this version of the bot.

If you want to train and export your own custom onnx model you can follow the steps that are set up in the following Google Colab: https://colab.research.google.com/drive/19kVzBERhRwB1jywcKeJ3dALARNd5-dR7?usp=sharing

You can check out the rewritten version on C++ (with no UI) that also uses Onnx to run inference here: https://github.com/Riczap/The-Gatherer-Cpp

- **Known Issue:** Trying to move the window of The Gatherer 2 while having the Bot Vision activated, will crash the program. (You can move the command prompt at any time without issues)

 - **Note:** The Bot and the Vision are independent, you can have the bot running without the Computer Vision function activated. The model is running on the background whenever you activate either of them.
 
 - **Note:** All of the parameters have default values, so you can leve them blank and it'll work fine.

- Training Data (Demo): https://drive.google.com/drive/u/2/folders/17X_f17WpzoxHMURSj5QIZ4lMUWPImf5V

- Showcase: Note that the following video is of the previous 1.0 version with an outdated GUI. [https://www.youtube.com/watch?v=y669rc18ia4](https://www.youtube.com/watch?v=y669rc18ia4)
![Showcase](https://user-images.githubusercontent.com/77018982/230541525-271eea09-be75-47e8-be8f-6c8bb133668a.PNG)

## New Features
I've implemented some quality of live updates so it's easier to use for general purposes.
- You can choose the resolution that you are currently using for your game manually

![Resolution](https://user-images.githubusercontent.com/77018982/230542772-f769a8ff-7da7-4b67-9fbb-f76bdfd8fa6f.PNG)
- You can add and select your custom models with a drop down menu

![Models](https://user-images.githubusercontent.com/77018982/230542819-248199e9-3c06-4323-b472-fce2487b5446.PNG)
- You can now input your desired waiting time between the actions of the bot.

Just remember to click the **Save changes** button after you selected your custom parameters
![Save](https://user-images.githubusercontent.com/77018982/230543242-8bdbd567-e4e6-493d-bb11-cf7b62abba1e.PNG)


## Installation
To use the new version of The Gatherer you can install the dependencies either in your main python environment, using anaconda or as an executable file.

-Download Tutorial: https://www.youtube.com/watch?v=dljCXzuKTKo
### Python
 1. Clone the repository on GitHub (Download the files).
 2. Open a console terminal and run the following command to install all of the dependencies: `pip install -r requirements.txt`
### Conda
 1. Clone the repository on GitHub (Download the files).
 2. Install Anaconda: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
 3. Create an Environment using the following command on the anaconda prompt: `conda create -n myenv` (you can choose any name you want for the env)
 4. Activate the environment using `conda activate myenv` and open the directory where you downloaded the source code for the bot. Run the following line to install all of the dependencies: `pip install -r requirements.txt`
 5. Now you can run the **main.py** file through the conda environment using `python main.py`
### Executable
 1. Download and extract the zip file: https://drive.google.com/file/d/1HImNmd06msfE_RuhBxIzT-rLlXL6LCa5/view?usp=share_link
 2. Right click and create a shortcut of **The Gatherer 2.exe** file and move it to your desired location
 3. Remeber that you'll need to acces the **models** directory to add new custom models.

## How to Add a Custom Model
### Exporting to Onnx
 I'm also finishing up a video tutorial explaining how to export your custom models. And here is a step by step guide on how to do it.
- Open the Google Colab link and follow the steps: https://colab.research.google.com/drive/1uJMeZP4QbSVuA5TNkfeXQDIpFDHVTeAB?usp=share_link
 ### Adding the model to The Gatherer 2.0
 2. Once you've you custom model as a yolov5.onnx file you can proceede to create a text file with a matching name to the name of your model containing the name of your custom classes.
 
 ![Text File](https://user-images.githubusercontent.com/77018982/230546123-b4ef79b7-b65a-42ce-be44-0ad4ee847e22.PNG)
 
 3. Move both files into the **models** directory.

Feel free to use the code for your own projects!

If you have any issues and need assistance send me a message or post something on:
Discord: WanderingEye#0330
Forum: https://www.unknowncheats.me/forum/usercp.php

