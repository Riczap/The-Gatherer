import customtkinter as ctk
from gadgets import *
from onnx_detextion import *
from window_capture import WindowCapture
from bot_thread import *
import cv2
import sys

#Move Albion Client to the corner of the screen

#Bot thread
go = Move()
go.start()

# Set custom theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.models = filter_models(get_files_in_folder())
        self.model = "rough_stone.onnx"
        self.is_cuda = len(sys.argv) > 1 and sys.argv[1] == "cuda"
        self.net = build_model(self.is_cuda, f"models/{self.model}")

        self.resolution = "1024x720"
        self.waiting_time = 3.5
        self.width, self.height = self.resolution.split('x')
        self.screen_center = [int(self.width)/2, int(self.height)/2]
        self.lock = threading.Lock()

        self.vision_status = "off"
        self.bot_status = "off"
        self.wincap = WindowCapture(None)

        self.class_ids, self.confidences, self.boxes, self.class_list, self.centers = [], [], [], [], []
        

        self.geometry("370x320")
        self.title("The Gatherer 2.0 - Wandering Eye")
        self.iconbitmap("wanderingeye.ico")

        self.protocol("WM_DELETE_WINDOW", self.on_close)


        def update_vision_status():
            self.vision_status = self.actions_frame.get_state1()
            print("Vision status updated to:", self.vision_status)


        def update_bot_status():
            self.bot_status = self.actions_frame.get_state2()
            print("Bot status updated to:", self.bot_status)
                

        def update_info():
            cv2.destroyAllWindows()
            self.actions_frame.reset_values()
            self.bot_status="off"
            self.vision_status="off"
            
            print(self.onnx_model_box.get_option())
            self.model = self.onnx_model_box.get_option()
            self.net = build_model(self.is_cuda, f"models/{self.model}")          
            print(f"Using: {self.model}")
            
            self.width, self.height = self.game_size_box.get_option().split('x')
            self.wincap = WindowCapture(None, width=int(self.width), height=int(self.height))
            print(f"Game resolution: {self.width}x{self.height}")
            
            self.waiting_time = float(self.waiting_time_frame.get_value())
            print(f"Waiting time: {self.waiting_time}\n")

        

        #Creating Objects
        self.actions_frame = SwitchesFrame(self, name="Actions", text1="Display bot's vision", text2="Gather resources", command_name1 = update_vision_status, command_name2 = update_bot_status)
        self.game_size_box = DropdownFrame(self, name="Select Window Size", text="Game resolution", default="1024x720" , options=["1024x720","1280x720", "1280x1024", "1366x768", "1600x900", "1680x1050", "1920x1080"])
        self.onnx_model_box = DropdownFrame(self, name="Select detection model", text="Onnx model", default="rough_stone.onnx", options=self.models)
        self.update_info_button = ctk.CTkButton(self, text="Save changes", command=update_info)
        self.waiting_time_frame = SingleEntryFrame(self, header_name="EntryFrame1", name="Waiting Time", text="3.5", default=3.5)
        

        #Drawing Objects
        self.actions_frame.grid(row=0, column=0, pady=12, padx=10)
        self.waiting_time_frame.grid(row=1, column=0, pady=12, padx=10)
        self.game_size_box.grid(row=0, column=1, pady=12, padx=10)
        self.onnx_model_box.grid(row=1, column=1, pady=12, padx=10)
        self.update_info_button.grid(row=2, column=0, padx=20, pady=10)



    def bot_gathering(self):
        if self.bot_status=="on":
            go.update(self.centers, True, self.waiting_time, self.screen_center)
        elif self.bot_status=="off":
            go.update([], False, self.waiting_time, self.screen_center)

    def update_screenshot(self):
        #Avoid running inference if there are no actions activated
        if(self.vision_status == "on" or self.bot_status =="on"):
            self.screenshot = self.wincap.get_screenshot()
            self.class_ids, self.confidences, self.boxes, self.class_list = results_objects(self.screenshot, self.net, self.model)
            self.centers = get_center(self.boxes)
            self.frame = results_frame(self.screenshot, self.class_ids, self.confidences, self.boxes, self.class_list)
        
        if (self.vision_status == "on"):
            cv2.imshow("Computer Vision", self.frame)
            cv2.waitKey(1)
            self.after(100,self.update_screenshot)
            self.after(100,self.bot_gathering)
            
        elif self.vision_status == "off":
            cv2.destroyAllWindows()
            self.after(100,self.update_screenshot)
            self.after(100,self.bot_gathering)

            
            
    def on_close(self):
        print("Closing")
        go.stop()
        self.destroy()    



if __name__ == "__main__":

    app = App()
    app.after(100, app.update_screenshot)
    app.mainloop()
