########################################################################################################
                            #   YOUTUBE DOWNLOADER || BY ANAS HIDAOUI (Septenber 26 2020) #
#########################################################################################################
##########################################################
    # IMPORT ALL REQUIREMENTS
###########################################################
import tkinter as tk
from tkinter import StringVar
import pafy
from tkinter import ttk
from ttkthemes import themed_tk
from tkinter import messagebox,filedialog
###########################################################



class YoutubeAPP:
    """
    This class is the main part of YOUTUBE DOWNLOADER APP.
    It based on tkinter and pafy(youtube-dl)
    """
   
    
    def __init__(self) :

        
        # Run all the main programe
        ############################################################
        self.root_wind = themed_tk.ThemedTk()  # Make the main window
        ################<variables>############################
        self.getURL  = StringVar()
        self.getPATH = StringVar()
        self.theme_choise = StringVar()

        #self.playliste = {}
        ######################<file picture>###################
        self.file_picture()
        ########################<>############################
        self.add_menu()
        self.themePicture() # defind the picturs
        self.addbind(self.root_wind) # add the bind
        ###################<VARtheme>##########################
        self.color_icons = (self.light_default_icon,
            self.light_plus_icon,
            self.dark_icon,
            self.red_icon,
            self.monokai_icon,
            self.night_blue_icon)
        self.color_dict ={
            "Light Theme":('#000000','#ffffff','xpnative'),
            "Light Plus Theme":('#474747','#e0e0e0','clam'),
            "Dark Theme":('#c4c4c4','#2d2d2d','black'),
            "Red Theme":('#2d2d2d','#ffe8e8','radiance'),
            "Monokai Theme":('#d3b774','#474747','ubuntu'),
            "Night Blue Theme":('#ededed','#6b9dc2','itft1')
        }
        ###############<>###########################
        self.addcolore()    # add the colore in yhe window
        #################<!end variables!>#####################
        self.desingRootWind(self.root_wind)    # Desinged the main window
        self.widgets(self.root_wind)           # Designed the widjets

        self.root_wind.mainloop()  # Run the main window
    
    def clickDownload(self) :
        if self.getURL.get() == "" :
            messagebox.showerror('Error','Enter the URL')
        elif self.getPATH == "" :
            messagebox.showerror('Error','Enter the path')
        else :
            try :
                select   = self.qualitybox.curselection()
                print(select)
                quality = self.all[select[0]]
                print(quality)
                path = str(self.getPATH)
                quality.download(path)
            except Exception as e :
                messagebox.showerror('Error','Connection Error.....Check the url and try again')
            else :
                #self.playliste[str(self.ved_obj.title)] = path + "/" + str(self.ved_obj.title)
                messagebox.showinfo('Downloading Finish',"The video(audio) was downloaded Sucessfully!!!")

    def setURL(self) :
        try :
            # get the url from the user
            url = self.getURL.get()
            # creat pafy object
            self.ved_obj = pafy.new(url) 
            #get the quility of the video(audio)
            self.quilities_video = self.ved_obj.streams
            print(self.quilities_video )
            self.quilities_audio = self.ved_obj.audiostreams
            ####################################################"
            # # some information 
            self.title_label.configure(text="Title: "+str(self.ved_obj.title))
            print(self.ved_obj.title)
            self.author_label.configure(text="Author: "+str(self.ved_obj.author))
            self.vieus_label.configure(text="Vieus: "+str(self.ved_obj.viewcount))
        except Exception as e :
            messagebox.showerror('Error',e)
        else :
            self.all = self.quilities_video + self.quilities_audio
            print(self.all)
            c = 1
            s = 1
            for q in self.all:
                self.qualitybox.insert('end', str(c) +". "+str(q)+"\n\n")
                c += 1
    def clickBrowse(self):
        location_of_download = filedialog.askdirectory()
        self.getPATH.set(location_of_download)
    def clickclear(self):
        self.getURL.set("")
        self.getPATH.set("")
        self.qualitybox.delete(0,"end")
    def desingRootWind(self,window) :
        window.geometry('940x600+320+90')
        window.title('Youtube*Downloader')
        window.resizable(False,False)
        icon = tk.PhotoImage(file=r"icons/icon1.png")
        window.tk.call("wm",'iconphoto',window._w,icon)
        window.configure(background='#ffe8e8')


    def widgets(self,window,bg_="#ffe8e8",fg_="#000000") :
        ########################<labels>################################
        self.headerlabel = tk.Label(window,text="YOUTUBE VIDEO DOWNLOADER",
            foreground = "#00D47C", 
            background = bg_ ,
            width = 50,
            font=('times', 20,'italic bold underline '))
        self.url_label = tk.Label(window,text="URL:",
            foreground = fg_, 
            background = bg_ ,
            font=('times', 15,'italic'))
        self.qualityLabel = tk.Label(window,
            text="Qualities:",
            foreground = fg_, 
            background = bg_ ,
            font=("Century Gothic",15))
        self.path_label = tk.Label(window,text="Save as:",
            foreground = fg_, 
            background = bg_ ,
            font=('times', 15,'italic'))
        self.title_label = tk.Label(window,text="",
            foreground = fg_, 
            background = bg_ ,
            font=('times', 15,'italic'))
        self.author_label = tk.Label(window,text="",
            foreground = fg_, 
            background = bg_ ,
            font=('times', 15,'italic'))
        self.vieus_label = tk.Label(window,text="",
            foreground = fg_, 
            background = bg_ ,
            font=('times', 15,'italic')) 
        #########################<!entries!>####################################
        url_entry = tk.Entry(window,font=('Century Gothic',12),
            textvariable = self.getURL,
            width=60,
            bd=3,relief="solid",
            borderwidth=2)
        path_entry = tk.Entry(window,font=('Century Gothic',12),
            textvariable = self.getPATH,
            width=30,
            bd=3,relief="solid",
            borderwidth=2)
        ##############################<!button!>##########################################
        self.seturl = tk.Button(window,text='set URL',font=("Century Gothic",10),
            width=10,relief='solid',
            activebackground="#64b3d9",
            cursor='hand2',
            borderwidth=2,
            command=self.setURL
        )
        browseButton = tk.Button(window,text = "BROWSE",
            font=("Century Gothic",10),
            width=10,
            activebackground="#64b3d9",
            cursor='hand2',
            relief='solid',borderwidth=1, 
            command=self.clickBrowse)
            
        downloadButton = tk.Button(window, text = "DOWNLOAD",
            font=("Century Gothic",10),
            width=15,relief='solid',
            activebackground="#64b3d9",
            cursor='hand2',
            borderwidth=1,
            command=self.clickDownload)
            
        clearButton= tk.Button(window, text = "CLEAR ALL",
            font=("Century Gothic",10),
            width=15,relief='solid',
            activebackground="#64b3d9",
            cursor='hand2',
            borderwidth=1,command=self.clickclear
            )
        #####################<!liste box!>################
        self.qualitybox = tk.Listbox(window,
            font=("Century Gothic",11),
            width = 56, height = 12,
            bg='#fff',
            bd=3, relief='solid',
            borderwidth=1)

        ###############################################
        self.exit_btn = tk.Button(window,text="EXIT",
            width=10,
            activebackground="#64b3d9",
            cursor='hand2',
            relief='solid',
            borderwidth=1,
            command=self.exit)
        ###########<!GEOMETRY MANAGEMENT!>#############
        self.headerlabel.place(x=180,y=0)
        self.url_label.place(x=10,y=80)
        url_entry.place(x=100,y=80)
        self.qualityLabel.place(x=10,y=200)
        self.qualitybox.place(x=180,y=140)
        self.title_label.place(x=700,y=140)
        self.author_label.place(x=700,y=200)
        self.vieus_label.place(x=700,y=260)
        self.path_label.place(x=10,y=400)
        path_entry.place(x=100,y=400)
        self.seturl.place(x=760,y=80)
        browseButton.place(x=460,y=400)
        clearButton.place(x=500,y=500)
        downloadButton.place(x=300,y=500)
        self.exit_btn.pack(side="bottom")
    
    ##################################<!COLOR THEME!>###############################################
    def theme_change(self) :
        theme = self.theme_choise.get()
        color_tuple = self.color_dict.get(theme)
        fg_color,bg_color = color_tuple[0],color_tuple[1]
        self.root_wind.configure(background=bg_color)
        ######################################"
        self.headerlabel.config(bg=bg_color)
        self.url_label.config(bg=bg_color,foreground=fg_color)
        self.path_label.config(bg=bg_color,foreground=fg_color)
        self.qualitybox.config(bg=bg_color,foreground=fg_color)
        self.qualityLabel.config(bg=bg_color,foreground=fg_color)
        ######################################
        #self.root.set_theme(color_tuple[2])
    def themePicture(self) :
        # THEAME ICONS
        self.light_default_icon = tk.PhotoImage(file=r'icons/light_default2.png')
        self.light_plus_icon    = tk.PhotoImage(file=r'icons/light_plus2.png')
        self.dark_icon          = tk.PhotoImage(file=r'icons/dark2.png')
        self.red_icon           = tk.PhotoImage(file=r'icons/monokai2.png')
        self.monokai_icon       = tk.PhotoImage(file=r'icons/monokai2.png')
        self.night_blue_icon    = tk.PhotoImage(file=r'icons/night_blue2.png')
    def file_picture(self) :
        #FILE ICONS 
        self.new_icon = tk.PhotoImage(file=r'icons/new.png')
        self.exit_icon = tk.PhotoImage(file=r'icons/exit.png')
        """
        self.open_icon = tk.PhotoImage(file=r'icons2/open.png')
        self.save_icon = tk.PhotoImage(file=r'icons2/save.png')
        self.save_as_icon = tk.PhotoImage(file=r'icons2/save_as.png')
        self.exit_icon = tk.PhotoImage(file=r'icons2/exit.png')
        """

    def addcolore(self) :
        count = 0
        for i in self.color_dict:
            self.Theme.add_radiobutton(label=i,image=self.color_icons[count],
                variable=self.theme_choise,
                compound="left",
                command=self.theme_change)
            count += 1

    def about(self) :
        about_info = '''Name: PyTube
Type: Youtube-Downloader
Creator: Anas Hidaoui
E-mail: anas12hid@gmail.com
Technology: Tkinter (Python)'''
        messagebox.showinfo('PyTube',about_info)
    
    def exit(self) :
        choice = messagebox.askyesnocancel("PyTube","Do you want to quit 'PyTube'?")
        if choice:
            self.root_wind.quit()
        elif choice is None:
            return
    

    ####################<ADD BIND>###################### 
    def addbind(self,root) :
        #root.bind_all("<Control-o>",open_file)
        #text_editor.bind_all("<Control-O>",open_file)
        root.bind_all("<Control-e>",self.exit)
        root.bind_all("<Control-E>",self.exit)
        """
        text_editor.bind_all("<Control-s>",save_file)
        text_editor.bind_all("<Control-S>",save_file)
        text_editor.bind_all("<Control-q>",save_as_file)
        text_editor.bind_all("<Control-Q>",save_as_file)
        text_editor.bind_all("<Control-F>",find_show_hide)
        text_editor.bind_all("<Control-f>",find_show_hide)
        text_editor.bind_all("<Control-t>",tts)  
        """  

    def add_menu(self) :
        self.main_menu = tk.Menu(self.root_wind) 
        self.root_wind.configure(menu=self.main_menu)
        #MENU OPTIONS
        self.File     = tk.Menu(self.main_menu,tearoff=False)
        self.Theme    = tk.Menu(self.main_menu,tearoff=False)
        self.About    = tk.Menu(self.main_menu,tearoff=False)
        # Cascading thre menu
        self.main_menu.add_cascade(label='File',menu=self.File)
        self.main_menu.add_cascade(label='Theme',menu=self.Theme)
        self.main_menu.add_cascade(label='About',menu=self.About)
        #
        self.About.add_command(label='About PyTube',command=self.about)
        #
        self.File.add_command(label='Exit',image=self.exit_icon,
                compound='left',
                accelerator='CTRL+E',
                command=self.exit)
    




    
    


