import numpy as np
import win32gui, win32ui, win32con

class WindowCapture:
    
    #Properties
    w = 0
    h = 0
    hwnd = None
    offset_x = 0
    offset_y = 0


    def __init__(self, window_name=None, width=1024, height=768):
        
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
        #Call specific window to capture
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception("Window not found: {}".format(window_name))
        
        #Define monitor dimentions
        self.w = width #1366
        self.h = height #768
    
    def get_screenshot(self):
        #bmpfilenamename = "out.bmp" #set this

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype = "uint8")
        img.shape = (self.h,self.w,4)
        #save screenshot
        #dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        
        img = img[...,:3]
        img = np.ascontiguousarray(img)
        
        return img
    
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
