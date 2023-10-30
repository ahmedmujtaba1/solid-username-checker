import customtkinter, webbrowser, re, requests, random, os, json
from PIL import Image
from tkinter import filedialog

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("green")  


def outlook_checker(email : str) -> bool:
    headers = {
        'authority' : 'signup.live.com',
        'method' : 'POST',
        'path' : '/API/CheckAvailableSigninNames?lcid=1033&wa=wsignin1.0&rpsnv=16&ct=1697374912&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d4204f7c7-8309-bf03-41d8-afc7098e33b3&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=bd4f04e1be6743a5bbdd772ec21e283f',
        'scheme' : 'https',
        'Accept' : 'application/json',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Cache-Control' : 'no-cache',
        'Canary' : 'lDvQa5CsBb6yVklpGzJ3tKqGgvxmvYDiIPBbPZuo21tENCYeWuMA5T9Ej23nLsvsJooFbotUaRQqQlV8uN3UiZCGhAZLzciJOqJDDdwgTw9bKSX4oq/ykV8YMdLuI2d+NL1gokaCG8/82xIsB7ArRvYzmbM7caf46bltsjRb4gC1invq/nB8p+j7xN6s7Z5VeOR13bO2IKDGXogXGeKNHhA3Ra7A5xKNi276hJ9meSUdyPOxghQD3PGegMGSXI8A:2:3c',

        # 'Accept-Language' : 'en-US,en;q=0.9',
        'Content-Type' : 'application/json',
        'Content-Length' : '150',
        # 'Origin' : 'https://promoterkit.com',
        # 'Referer' : 'https://promoterkit.com/tools/email/checker.aspx/ValidateEmail',
        'Cookie' : 'MicrosoftApplicationsTelemetryDeviceId=9d2933a3-5863-4a8d-a8e6-1b53633dbab7; MUID=54f3c2fb1b4444dfaa99ae91b28e0350; MSFPC=GUID=f9ecddd83d0f454e9de0038743e9b691&HASH=f9ec&LV=202310&V=4&LU=1697201318786; amsc=qNSi7ymOfEcCsYp/EHHHvAM0O5ls59qoy8pn9ZmdtgVovSZZtfpWfNdJ3E47RJz9oKc1v8gQMh4vDr628ZzD4on/D2vhxyLDUqW6hLHMgQfeUsAn3WghojoD6xXkR14ZhrD9m8I1ELTvOSsxLNyO1ZHbc69MBedOh2I/yICUJcA8QEHhbSsu2wGkM3uVb0VOdj0WQHV1LzID7SmYishBIFYfGXIgugUN7+C1wCvdO+KUOVDbIAzRhirCWrwsxkwYl+cx+j8pOR49P2AMvJEk1YzkEjTpxklTn1mXom9+VkoNHwGB1N9cxuEDw+yxSdmW:2:3c; fptctx2=taBcrIH61PuCVH7eNCyH0J9Fjk1kZEyRnBbpUW3FKs%252fHBvH7FsNe%252fHNngZs4Nuom2oUgx8%252frch6X8dJs03aRL8vOrdOkJQ1RHUq2E46zBa6v0wnElbCUYyZhZTk5GijIcsggPGjktEJnLhhHbKbioG9SRpgmQ7spExmWrX0p8CVfX0ZXwFL7Mmbx0Ciat8T4R09THZP%252frMOpvf0gomsHdCQbwfsZMn%252fbakG04s8FRCnb400sqCYiaiYCx4%252f7Y%252fbrKy4IqR8Rnas%252fvuL8ZeWJCyegedMOGuFdqt7O4R1A9JW%252b3wfxIHaVa6mQ62lOjzFlYGj3cGyh2SqOqB%252fG2kXuwA%253d%253d; logonLatency=LGN01=638329717121443382; clrc={%2219646%22%3a[%22d7PFy/1V%22%2c%22+VC+x0R6%22%2c%22SLD3q8F4%22%2c%22eb4C4Wvc%22%2c%22PNVGSRqC%22]}; ai_session=CfcymzwFbvdp128ayRKZ0L|1697374922656|1697374922656; arp_scroll_position=180',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }

    formdata = {
        'hpgid' : '200639',
        'includeSuggestions' : True,
        'scid' : '100118',
        'signInName' : f'{email}',
        'uaid' : 'bd4f04e1be6743a5bbdd772ec21e283f',
        'uiflvr' : '1001',
    }

    json_data = json.dumps(formdata)

    r = requests.post("https://signup.live.com/API/CheckAvailableSigninNames?lcid=1033&wa=wsignin1.0&rpsnv=16&ct=1697374912&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d4204f7c7-8309-bf03-41d8-afc7098e33b3&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=bd4f04e1be6743a5bbdd772ec21e283f", headers=headers, data=json_data)
    res = r.json()
    return res["isAvailable"]

def userExists(username, s):
    print("Checking the availability of {}".format(username))
    link = 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = s.get(link, headers=headers).text
    except:
        print("Failed to open {}".format(link))
        return None
    specData = re.findall(r'value="(.*?)" name="specData"', resp)[0]
    crumb = re.findall(r'value="(.*?)" name="crumb"', resp)[0]
    acrumb = re.findall(r'value="(.*?)" name="acrumb"', resp)[0]
    sessionIndex = re.findall(r'value="(.*?)" name="sessionIndex"', resp)[0]
    link = "https://login.yahoo.com/account/module/create?validateField=yid"
    headers = {
        'Referer': 'https://login.yahoo.com/account/create?.intl=us&.lang=en-US&src=ym&activity=ybar-mail&pspid=2023538075&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail&specId=yidReg&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3Fpspid%3D2023538075%26activity%3Dybar-mail',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-360,"timezone":"Asia/Dhaka","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"1","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0, D3D11-20.19.15.4380)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1624081774716,"render":1624081773747}}',
        'specId': 'yidregsimplified',
        'cacheStored': '',
        'crumb': crumb,
        'acrumb': acrumb,
        'sessionIndex': sessionIndex,
        'done': 'https://mail.yahoo.com/d?pspid=2023538075&activity=ybar-mail',
        'googleIdToken': '',
        'authCode': '',
        'attrSetIndex': '0',
        'specData': specData,
        'multiDomain': '',
        'tos0': 'oath_freereg|us|en-US',
        'firstName': '',
        'lastName': '',
        'userid-domain': 'yahoo',
        'userId': username,
        'password': '',
        'phone': '',
        'mm': '',
        'dd': '',
        'yyyy': '',
        'signup': '',
    }
    try:
        resp = s.post(link, headers=headers, data=data).json()
    except:
        print("Failed to open {}".format(link))
        return None
    # print(resp)
    all_errors = resp.get('errors', [])
    if len(all_errors) == 0:
        return None
    for errors in all_errors:
        if errors.get('name') == "userId":
            # print(errors.get('error'))
            return True
    return False

def verify(email, ouputAlive = None):
	url = "https://mail.google.com/mail/gxlu?email={}".format(email)
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
	}
	resp_headers = requests.get(url=url, headers=headers).headers
	if "Set-Cookie" in resp_headers:
		if ouputAlive == 1:
			return "Alive"
		else:
			pass
	else:
		return "Unregistered"

def check_existence(email:str) -> bool:
    flag: bool = False
    if (email.endswith('@yahoo.com') == True):
        s = requests.Session()
        check = userExists(username=email.split('@')[0], s=s)
        if check:
            flag = True

    elif (email.endswith('@aol.com') == True):
        s = requests.Session()
        check = userExists(username=email.split('@')[0], s=s)
        if check:
            flag = True

    elif (email.endswith('@gmail.com') == True):
        check = verify(email, 1)
        print(f'{email} : ', check )
        if "Unregistered" in str(check):
            flag = True
        
    elif (email.endswith('@hotmail.com') == True) or (email.endswith('@outlook.com') == True):
        res = outlook_checker(email=email)
        if not res:
            flag = True

    else:
        api_lists = ["Hr5OEWWwjWvZfA46cTFEf", "t3DEMdZa996KCs2rpENLS", "dBOkerlYKvA5cmmgUP2Uo"]

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
                                                        values=["@gmail.com","@yahoo.com","@mail.com","@hotmail.com","@gmx.com", "@outlook.com", "@aol.com"])
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
        self.textbox2.delete('1.0', 'end')
        self.textbox2.insert('end', "----------------------------------------------------------------------------------------------------\n \n")
        self.textbox2.insert('end', "Output : \n \n")
        self.textbox3.configure(state='normal')
        self.textbox3.delete('1.0', 'end')
        self.textbox3.insert('end', "----------------------------------------------------------------------------------------------------\n \n")
        self.textbox3.insert('end', "Output : \n \n")
        self.textbox3.update_idletasks()
        with open(self.selected_file_path2, 'w') as valid_file:
            valid_file.write('')
        with open(self.selected_file_path3, 'w') as invalid_file:
            invalid_file.write('')
        def is_valid_email(email):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(pattern, email)
        
        valid_emails = []
        invalid_emails = []

        # Process each username and check its validity and existence
        remaining_emails = []  # List to store remaining emails
    
        for username in usernames:
            email_full = f"{username}{domain}"
            username_w = username.split(domain)[0]
            if username.endswith(f'{domain}'):
                if not is_valid_email(username):
                    validity = "Invalid email syntax"
                    invalid_emails.append(username)
                else:
                    validity = check_existence(f'{username}')
                    print(username + f" : {validity}" + f" {type(validity)}")
                    # validity = False
                    # if (domain == "@hotmail.com") or (domain == "@outlook.com"):
                    #     if (validity == False):
                    #         self.textbox3.insert('end', username + "\n",'red_text')
                    #         self.textbox3.update_idletasks()
                    #         invalid_emails.append(username)
                    #         with open(self.selected_file_path3, 'a') as invalid_file:
                    #             invalid_file.write(str(username) + '\n')
                    #     else:
                            
                    #         self.textbox2.insert('end', username + "\n", 'green_text')
                    #         self.textbox2.update_idletasks()
                    #         valid_emails.append(username)
                    #         with open(self.selected_file_path2, 'a') as valid_file:
                    #             valid_file.write(str(username) + '\n')
                    
                    if (validity == False):
                        self.textbox2.insert('end', username + "\n",'red_text')
                        self.textbox2.update_idletasks()
                        valid_emails.append(username)
                        with open(self.selected_file_path2, 'a') as invalid_file:
                            invalid_file.write(str(username_w) + '\n')
                    else:
                        
                        self.textbox3.insert('end', username + "\n", 'green_text')
                        self.textbox3.update_idletasks()
                        invalid_emails.append(username)
                        with open(self.selected_file_path3, 'a') as valid_file:
                            valid_file.write(str(username_w) + '\n')
                    # Extract remaining emails using list comprehension
                    remaining_emails = [f"{email}" for email in usernames if f"{email}" not in valid_emails and f"{email}" not in invalid_emails]
                    # print("[+] Remaining Emails  : ", remaining_emails)
                    # Overwrite the original file with remaining emails
                    with open(self.selected_file_path, 'w') as file:
                        file.write('\n'.join(remaining_emails))
                            
                        
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