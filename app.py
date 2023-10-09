import tkinter
import tkinter.messagebox
import customtkinter, webbrowser
from PIL import Image
from tkinter import filedialog
from check import check_existence

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("green")  


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Email Validation Bot - [Ahmed Mujtaba]")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Email Validation Bot", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.start_button, text="Start")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.stop_button, text="Stop", fg_color="red", hover_color="red")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.tabview1 = customtkinter.CTkTabview(self, width=700)
        self.tabview1.grid(row=1, column=1, padx=(10, 0), pady=(20, 0), sticky="nsew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self, width=450)
        self.progressbar_1.grid(row=1, column=1, padx=(0, 0), pady=(0, 400))
        # self.tabview1.add("Output")
        self.tabview1.add("Valid Emails")
        self.tabview1.add("Invalid Emails")
        # self.tabview1.tab("Output").grid_columnconfigure(0, weight=10) 
        self.tabview1.tab("Valid Emails").grid_columnconfigure(1, weight=10)  
        self.tabview1.tab("Invalid Emails").grid_columnconfigure(2, weight=10)
        # self.textbox = customtkinter.CTkTextbox(self.tabview1.tab("Output"), width=500, height=400, state='disabled', fg_color="green")
        # self.textbox.grid(row=1, column=1, padx=(0, 40), pady=(50, 0), sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self.tabview1.tab("Valid Emails"), width=500, height=400, state='disabled', text_color="green")
        self.textbox2.grid(row=1, column=1, padx=(25, 40), pady=(50, 0), sticky="nsew")
        self.textbox3 = customtkinter.CTkTextbox(self.tabview1.tab("Invalid Emails"), width=500, height=400, state='disabled', text_color="red")
        self.textbox3.grid(row=1, column=1, padx=(30, 25), pady=(50, 0), sticky="nsew")

        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create tabview
        
        self.tabview = customtkinter.CTkTabview(self, width=250, height=700)
        self.tabview.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Settings")
        self.tabview.add("Contact")
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Contact").grid_columnconfigure(0, weight=1)

        self.threads_entry = customtkinter.CTkEntry(self.tabview.tab("Settings"), validate="key", placeholder_text="Threads")
        self.threads_entry.grid(row=1, column=0, padx=20, pady=(20, 10))
        def validate_number_input(P):
            if P == "" or P.isdigit():
                return True
            else:
                return False
        self.validate_number = self.tabview.tab("Settings").register(validate_number_input)

        light_image_settings = Image.open('folder.png')
        photo_settings = customtkinter.CTkImage(light_image=light_image_settings)
        self.image_button_settings = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Usernames(.txt)", image=photo_settings, compound="left", command=self.select_file)
        self.image_button_settings.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.image_button_settings = customtkinter.CTkButton(self.tabview.tab("Settings"), text="valid(.txt)", image=photo_settings, compound="left", command=self.select_file2)
        self.image_button_settings.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.image_button_settings = customtkinter.CTkButton(self.tabview.tab("Settings"), text="invalid(.txt)", image=photo_settings, compound="left", command=self.select_file2)
        self.image_button_settings.grid(row=4, column=0, padx=20, pady=(10, 10))
        # self.selected_file_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="  Usernames: None")
        # self.selected_file_label.grid(row=3, column=0, padx=20, pady=(0, 10))

        self.selected_file_path2 = None
        self.selected_file_path3 = None
        self.selected_file_path = None
        self.threads_entry.configure(validate="key", validatecommand=(self.validate_number, "%P"))
        self.domain_select = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), dynamic_resizing=False,
                                                        values=["@gmail.com","@yahoo.com","@mail.com","@hotmail.com","@gmx.com"])
        self.domain_select.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Contact"), text="Github [@ahmedmujtaba1]")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_2.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/AhmedMujtaba1"))

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.domain_select.set("Select Domain")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.stop()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path = file_path

    def select_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path2 = file_path

    def select_file3(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path3 = file_path

    def start_button(self):
        self.progressbar_1.start()
        file_path = rf"{self.selected_file_path}"
        threads = self.threads_entry.get()
        domain = self.domain_select.get()
        
        usernames = []
        if self.selected_file_path:
            with open(self.selected_file_path, 'r') as file:
                usernames = file.read().split('\n')
                
        
        self.textbox2.configure(state='normal')
        self.textbox2.delete('1.0', 'end')
        self.textbox2.insert('end', f"Selected File: {file_path}\nThreads: {threads}\nDomain: {domain}\n")
        self.textbox2.insert('end', "----------------------\n \n")
        self.textbox3.configure(state='normal')
        self.textbox3.delete('1.0', 'end')
        self.textbox3.insert('end', f"Selected File: {file_path}\nThreads: {threads}\nDomain: {domain}\n")
        self.textbox3.insert('end', "----------------------\n \n")
    
        for username in usernames:
            validity = check_existence(f'{username}')
            if validity:
                self.textbox2.insert('end', username + f" ::---------::> {validity}" + "\n", 'green_text')
                with open(self.selected_file_path2, 'a') as valid_file:
                    valid_file.write(str(username) + '\n')
            else:
                self.textbox3.insert('end', username + f" ::---------::> {validity}" + "\n",'red_text')
                with open(self.selected_file_path3, 'a') as invalid_file:
                    invalid_file.write(str(username) + '\n')
                
        self.textbox2.configure(state='disabled')
        self.textbox3.configure(state='disabled')



    def stop_button(self):
        self.progressbar_1.stop()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()