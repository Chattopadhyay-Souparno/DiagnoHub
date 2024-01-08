import tkinter as tk
from tkinter import ttk

from PIL import Image , ImageTk

from Chatbot_Logic import get_user_input , get_chatbot_response
from tkinter import filedialog

import random

import folium
import webbrowser
import os
from Geolocation_OOP import Pharmacy

import tensorflow_lung_cancer_model

class ChatBotGUI:
    def __init__(self, parent):
        self.parent = parent
        #self.parent.configure(bg="black")
        image = Image.open("Medbot3.png")  # Replace with the actual path
        image = image.resize((200, 200), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(parent, image=photo, bg="midnight blue")
        label.image = photo  # Keep a reference to the image
        label.pack(padx=10, pady=10)
        
        label2 = tk.Label(parent, font=("Helvetica", 12),text="This Chatbot is a proof of concept and can handle single queries at a time. \n A more advanced version has been provided in the GitHub Repo", bg="midnight blue", fg="white")
        label2.pack(padx=10, pady=10)
        
        label3 = tk.Label(parent, font=("Helvetica", 12),text="Type in your symptoms one at a time", bg="midnight blue", fg="white")
        label3.pack(padx=10, pady=10)
        
        #style = ttk.Style()
        #style.configure("BW.TLabel", background="white")

        self.chat_frame = tk.Frame(parent, bg="midnight blue")
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_entry = tk.Entry(self.chat_frame, width=50, font=("Helvetica", 12))
        self.chat_entry.grid(row=0, column=0, padx=5, pady=5)

        self.send_button = tk.Button(
            self.chat_frame,
            text="Send",
            command=self.send_message,
            font=("Helvetica", 12),
            bg="yellow",
            fg="black",
        )
        self.send_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.chat_display = tk.Text(
            self.chat_frame,
            width=50,
            height=10,
            font=("Helvetica", 12),
            fg="white",
            bg="black",
            state=tk.DISABLED,
        )
        self.chat_display.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def send_message(self):
        user_message = self.chat_entry.get()
        self.display_message(f"User: {user_message}")

        # Basic chatbot logic with conditional responses
        bot_response = get_chatbot_response(user_message)
        self.display_message(f"ChatBot: {bot_response}")

        self.chat_entry.delete(0, tk.END)


    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state=tk.DISABLED)




class MyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Diagnohub")
        self.master.geometry("800x600")  # Set a larger window size

        # Create a notebook (tabs container)
        self.notebook = ttk.Notebook(master)

        # Create tabs
        style = ttk.Style()
        style.configure("BW.TLabel", background="midnight blue")
        self.Home = ttk.Frame(self.notebook, style="BW.TLabel")
        self.tab1 = ttk.Frame(self.notebook, style="BW.TLabel")  # Set black background
        self.tab2 = ttk.Frame(self.notebook, style="BW.TLabel")
        #self.tab3 = ttk.Frame(self.notebook, style="BW.TLabel")

        # Add tabs to notebook
        self.notebook.add(self.Home, text="Home Page")
        self.notebook.add(self.tab1, text="Chatbot")
        self.notebook.add(self.tab2, text="Emergency Services")
        #self.notebook.add(self.tab3, text="Lung Cancer")

        # Initialize each tab's content
        self.init_Home()
        self.init_tab1()
        self.init_tab2()
        #self.init_tab3()

        # Pack the notebook
        self.notebook.pack(expand=1, fill="both")
        
    def init_Home(self):
        image = Image.open("LOGO2.png")  # Replace with the actual path
        image = image.resize((400, 400), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.Home, image=photo, bg="midnight blue")
        label.image = photo  # Keep a reference to the image
        label.pack(padx=10, pady=10)

        # Add a text label in the Home tab
        text_label = tk.Label(
            self.Home,
            text="An AI Enabled Service for Detection and Diagnosis",
            font=("Helvetica", 16),
            fg="white",
            bg="midnight blue",
        )
        text_label.pack(padx=10, pady=10)
        
        text_label2 = tk.Label(
            self.Home,
            text="Switch Tabs for Several Functionalities",
            font=("Helvetica", 12),
            fg="white",
            bg="midnight blue",
        )
        text_label2.pack(padx=10, pady=10)

    def init_tab1(self):
        chatbot_gui = ChatBotGUI(self.tab1)

    #def init_tab2(self):
        #label = tk.Label(self.tab2, text="Greetings from Tab 2!", bg="white", fg="blue")
        #label.pack(padx=10, pady=10)
        
    def init_tab2(self):
        image = Image.open("Pharma.png")  # Replace with the actual path
        image = image.resize((200, 200), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.tab2, image=photo, bg="white")
        label.image = photo  # Keep a reference to the image
        label.pack(padx=10, pady=10)
        
        paragraph_text = (
            "This Page contains the Contact Information of all the Pharmacies and Hospitals Near you \n \n"
            "Hospital Du Creusot: 03 85 77 20 00 \n"
            "Hospital Creusot Site Harfleur : 03 85 77 74 00 \n"
            "Pharmacie des Acacias : 03 85 55 05 90 \n"
            "Pharmacie des 4 Chemins : 03 85 55 07 84 \n"
            "Pharmacie de la Molette : 03 85 55 04 59 \n"
            "Pharmacie du Parc - Place Schneider : 03 85 77 91 71 \n"
        )
        
        
        label1 = tk.Label(self.tab2, text=paragraph_text, font=("Helvetica", 10), fg="white",bg="midnight blue")
        label1.pack(padx=10, pady=10)

        # Button to open the map
        open_map_button = tk.Button(
            self.tab2,
            text="Click to View the Locations",
            command=self.open_random_map,
            font=("Helvetica", 12),
            bg="deep pink",
            fg="white",
        )
        open_map_button.pack(pady=10)

    def open_random_map(self):
        # Generate random latitude and longitude coordinates
        Pharmacy()

    #def init_tab3(self):
        #label = tk.Label(self.tab3, text="Hello from Tab 3!", bg="black", fg="yellow")
        #label.pack(padx=10, pady=10)
        




class LungCancerPredictionTab:
    def __init__(self, parent, model_path):
        self.parent = parent
        self.model_path = model_path
        
        style = ttk.Style()
        style.configure("BW.TLabel", background="midnight blue")

        # Create Tab 3
        self.tab3 = ttk.Frame(self.parent.notebook , style="BW.TLabel")
        self.parent.notebook.add(self.tab3, text="Lung Cancer Prediction")

        # Initialize tab content
        self.init_tab_content()

    def init_tab_content(self):
        image = Image.open("lung.png")  # Replace with the actual path
        image = image.resize((200, 200), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.tab3, image=photo, bg="midnight blue")
        label.image = photo  # Keep a reference to the image
        label.pack(padx=10, pady=10)
        
        self.result_label = tk.Label(
            self.tab3,
            text="Our Diagnosis: Please click the upload button to select and upload an image",
            font=("Helvetica", 12),
            fg="white",
            bg="black",
        )
        self.result_label.pack(pady=10)

        # Button to upload an image
        upload_button = tk.Button(
            self.tab3,
            text="Upload Image",
            command=self.upload_image,
            font=("Helvetica", 12),
            fg="white",
            bg="deep pink",
        )
        upload_button.pack(pady=10)

        # Image display area
        self.image_label = tk.Label(self.tab3, bg="black")
        self.image_label.pack()



    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        if file_path:
            # Display the uploaded image
            photo = ImageTk.PhotoImage(image=Image.open(file_path))
            self.image_label.config(image=photo)
            self.image_label.photo = photo

            # Make a prediction using the TensorFlow model
            prediction = tensorflow_lung_cancer_model.predict(self.model_path, file_path)
            self.result_label.config(text=f"Our Diagnosis: {prediction}")


def main():
    root = tk.Tk()
    app = MyGUI(root)
    
    model_path = 'lung_cancer_detection_model.h5'
    lung_cancer_tab = LungCancerPredictionTab(app, model_path)

    
    root.mainloop()

if __name__ == "__main__":
    main()
