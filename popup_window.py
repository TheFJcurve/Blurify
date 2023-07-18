import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


class ImageWindow(tk.Tk):
    
    '''
    Input window, takes in image in a GUI fashion
    Side Effects:       Inputs an Image path
                        Creates a window on output
    '''

    def __init__(self):
        
        '''
        Sets up the window properties
        '''

        super().__init__()
        self.title("Image Selector")
        self.geometry("700x700")
        
        # Create a label to display the image
        self.image_label = tk.Label(self)
        self.image_label.pack(padx=10, pady=50)
        
        # Register the drag and drop event handlers
        self.bind("<Button-1>", self.on_drop)

    def on_drop(self, event):
        
        '''
        A file explorer window opens to select the path of the image you want.
        '''

        # Prompt the user to select an image file
        global file_path

        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image files", "*.*"), ("All files", "*.*"))
        )
        
        if file_path:
            ## Destroy the window and return the file path.
            self.destroy()
            return file_path


def start_action(input_img, action):

    '''
    Getting the input image that will be used in the program.
    Side Effects: Initiates img variable, which is used in the rest of the code
    '''

    ## We read the original image using cv2.imread() function, and then convert the image 
    ## into numpy layers that would be easier doing convolution with. 
    img = cv2.imread(input_img)

    ## Showing the numpy array as an image using matplotlib.pyplot
    plt.imshow(img)
    plt.title("Input Image")
    plt.show()

    action(img)


def input_window(action):
    # Create an instance of the ImageWindow class
    window = ImageWindow()
    window.mainloop()

    start_action(file_path, action)
