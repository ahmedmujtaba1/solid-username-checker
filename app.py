import customtkinter, webbrowser, re, requests, random, os
from PIL import Image
from tkinter import filedialog

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("green")  

def check_existence(email:str) -> bool:
    flag: bool = False
    if (email.endswith('@yahoo.com') == True) or (email.endswith("@hotmail.com") == True):
        r = requests.get(f"https://api.validemail.net/?email={email}&token=54d0bb46f65a4c0d9894454021f14560")
        re = r.json()
        additional = re["EmailAdditionalInfo"]
        if len(additional) > 1:
            flag = True
        elif re["IsValid"]:
            flag = True

    else:
        # api_lists = ["tQReT8Z7OINfadZ0qCv0N", "EWPfWcivWhA1T31WAJGfg", "hoq34RmyHE6Cqp9sQ0MYs"]

        api_lists = ''''' your list of apis here '''
        r = requests.get(f"https://apps.emaillistverify.com/api/verifEmail?secret={random.choice(api_lists)}&email={email}")
        if "ok" in str(r.content):
            flag = True

    return flag
    
    

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
        self.progressbar_1.grid(row=1, column=1, padx=(50, 210), pady=(0, 400))
        # self.tabview1.add("Output")
        self.tabview1.add("Valid Emails")
        self.tabview1.add("Invalid Emails")
        # self.tabview1.tab("Output").grid_columnconfigure(0, weight=10) 
        self.tabview1.tab("Valid Emails").grid_columnconfigure(1, weight=10)  
        self.tabview1.tab("Invalid Emails").grid_columnconfigure(2, weight=10)
        # self.textbox = customtkinter.CTkTextbox(self.tabview1.tab("Output"), width=500, height=400, state='disabled', fg_color="green")
        # self.textbox.grid(row=1, column=1, padx=(0, 40), pady=(50, 0), sticky="nsew")
        def open_in_explorer(file_path):
            print("FILE pATH : ", file_path)
            if file_path and os.path.exists(file_path):
                file_path = os.path.abspath(file_path)
                os.system(f'explorer "{file_path}"')

        self.textbox2 = customtkinter.CTkTextbox(self.tabview1.tab("Valid Emails"), width=500, height=400, state='disabled', text_color="green")
        self.textbox2.grid(row=1, column=1, padx=(25, 40), pady=(50, 0), sticky="nsew")
        self.textbox3 = customtkinter.CTkTextbox(self.tabview1.tab("Invalid Emails"), width=500, height=400, state='disabled', text_color="red")
        self.textbox3.grid(row=1, column=1, padx=(30, 25), pady=(50, 0), sticky="nsew")
        self.valid_file_button = customtkinter.CTkButton(self.tabview1.tab("Valid Emails"), text="Open Valid.txt in Explorer", command=lambda: open_in_explorer(self.selected_file_path2))
        self.valid_file_button.grid(row=1, column=1, padx=(400, 0), pady=(0,1400))
        self.valid_file_button = customtkinter.CTkButton(self.tabview1.tab("Invalid Emails"), text="Open Invalid.txt in Explorer", command=lambda: open_in_explorer(self.selected_file_path3))
        self.valid_file_button.grid(row=1, column=1, padx=(400, 0), pady=(0,1400))

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
        self.image_button_settings2 = customtkinter.CTkButton(self.tabview.tab("Settings"), text="valid(.txt)", image=photo_settings, compound="left", command=self.select_file2)
        self.image_button_settings2.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.image_button_settings3 = customtkinter.CTkButton(self.tabview.tab("Settings"), text="invalid(.txt)", image=photo_settings, compound="left", command=self.select_file3)
        self.image_button_settings3.grid(row=4, column=0, padx=20, pady=(10, 10))
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
        self.label_tab_2.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/ahmedmujtaba1/solid-username-checker"))

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.domain_select.set("Select Domain")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.stop()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path = file_path
            self.filename = os.path.basename(file_path)
            self.image_button_settings.configure(text=self.filename)
        

    def select_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path2 = file_path
            self.filename = os.path.basename(file_path)
            self.image_button_settings2.configure(text=self.filename)

    def select_file3(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.selected_file_path3 = file_path
            self.filename = os.path.basename(file_path)
            self.image_button_settings3.configure(text=self.filename)

    def start_button(self):
        print("Valid File TXT Path : ", self.selected_file_path2)
        print("Invalid File TXT Path : ", self.selected_file_path3)
        self.progressbar_1.start()
        threads = self.threads_entry.get()
        domain = self.domain_select.get()
        
        usernames = []
        if self.selected_file_path:
            with open(self.selected_file_path, 'r') as file:
                usernames = file.read().split('\n')
                
        
        self.textbox2.configure(state='normal')
        self.textbox2.insert('end', "----------------------------------------------------------------------------------------------------\n \n")
        self.textbox2.insert('end', "Output : \n \n")
        self.textbox3.configure(state='normal')
        self.textbox3.insert('end', "----------------------------------------------------------------------------------------------------\n \n")
        self.textbox3.insert('end', "Output : \n \n")
        self.textbox3.update_idletasks()
        def is_valid_email(email):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(pattern, email)
    
        for username in usernames:
            if not is_valid_email(username):
                validity = "Invalid email syntax"
            else:
                validity = check_existence(f'{username}')
                # validity = False
            if validity:
                self.textbox2.insert('end', username + f" ::---------::> {validity}" + "\n", 'green_text')
                self.progressbar_1.stop()
                self.textbox2.update_idletasks()
                with open(self.selected_file_path2, 'a') as valid_file:
                    valid_file.write(str(username) + '\n')
            else:
                self.textbox3.insert('end', username + f" ::---------::> {validity}" + "\n",'red_text')
                self.textbox3.update_idletasks()
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