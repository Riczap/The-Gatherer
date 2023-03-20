
# The-Gatherer
This was made using YOLOv5 and OpenCV. The model is working with the CPU so if you know how to use PyTorch you can implement GPU processing for better performance. But you can use this code as a template for any kind of PVE (not heavily dependent on high FPS) botting. You can load your custom YOLO models by using your own .pt file.
I'm also working on a full guide on how to tinker with the source code to add your custom bot actions and to use your own data set to train the model. For now I'ld recomend following this tutorial for custom training. [https://www.youtube.com/watch?v=GRtgLlwxpc4](https://www.youtube.com/watch?v=GRtgLlwxpc4)

Showcase: [https://www.youtube.com/watch?v=y669rc18ia4](https://www.youtube.com/watch?v=y669rc18ia4)

You can check out the rewritten version on C++ that uses Onnx to run inference here: https://github.com/Riczap/The-Gatherer-Cpp

This runs with Python and you'll need to follow this steps for running it:

 1. Clone the repository on GitHub (Download the files).
 2. Install Anaconda: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
 3. Create an Environment with Python 3.8 using the following command on the anaconda prompt: `conda create -n "myenv" python=3.8` (you can choose any name you want for the env)
 4. Activate the environment and open the directory where you downloaded the source code for the bot. Run the following line to install all of the dependencies: `pip install -r requirements.txt`
 5. Now you can run the **main.py** file through the conda environment using `conda activate myenv` `followed by python main.py`
 6. The default windowed screen size for the bot is *1024x768* resolution. Move the game window to the upper left corner of the screen. You can use any resolution and just adjust two variables in the code. Instructions at the end of the post.



 - **Note:** The Bot and the Vision are independent, you can have the bot running without the Computer Vision function activated. The model is running on the background all the time.

The hotkeys that I used for the bot actions are kind of awkward so I recommend unbinding them on Albion so you don't get menus opening all the time in game.

Sadly I'm having no success compiling the code to a .exe file because OpenCV and other dependencies are causing problems with that.

Feel free to use the code for your own projects!

If you have any issues and need assistance send me a message or post something on:
Discord: WanderingEye#0330
Forum: https://www.unknowncheats.me/forum/usercp.php

I'm working on a new version that works fully on C++ that also implements a GUI, I'll create a new repo for it and add the link here once I have a prototype done.
