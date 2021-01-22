import re
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import getData
import tkinter.scrolledtext as tkst
from jinja2 import Environment, FileSystemLoader
#from weasyprint import HTML
import subprocess
import sqlite3
import datetime


class Editor(tk.Tk):
    def __init__(self, master=None, fileName=None):
        super().__init__(master)
        self.master = master
        self.fileName = fileName
        #self.configure(bg='lightgrey')
        self.FONT_SIZE = 12
        self.WINDOW_TITLE = "Check Editor"
        self.open_file = ""
        self.title(self.WINDOW_TITLE)
        self.geometry("960x640")
        #self.config(bg='#2B2B2B')
        self.stateVar=StringVar()
        self.stateVar.set("Initial Value")
        # Initailize ttk style
        self.style = Style()

        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
        self.file_menu = tk.Menu(self.menubar, tearoff=0,  fg="black")
        self.file_menu.add_command(label="Open", command=self.openfile, accelerator="Ctrl+O")
        #self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
        #self.file_menu.add_command(label="Save", accelerator="Ctrl+S")
        #self.edit_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        #self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X")
        #self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V")
        #self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z")
        #self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y")

        self.menubar.add_cascade(label="File", menu=self.file_menu)
        #self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.configure(menu=self.menubar)

        # send menu
        self.send_menu = tk.Menu(self.menubar, tearoff=0,  fg="black")
        self.send_menu.add_command(label="To DB", command="", accelerator="Ctrl+O")
        self.send_menu.add_command(label="To Email", command="", accelerator="Ctrl+O")
        self.menubar.add_cascade(label="Send", menu=self.send_menu)
        # export menu
        self.export_menu = tk.Menu(self.menubar, tearoff=0,  fg="black")
        self.export_menu.add_command(label="PDF", command="", accelerator="Ctrl+O")
        self.export_menu.add_command(label="CDA", command="", accelerator="Ctrl+O")
        self.export_menu.add_command(label="DOC", command="", accelerator="Ctrl+O")
        self.menubar.add_cascade(label="Export", menu=self.export_menu)


        ################################## Toolbar ########################################
        toolbar = Frame(self)
        toolbar.grid(column = 0, row = 0, sticky='W' ,columnspan = 4, padx = 5, pady= 5)
        openfiletb = Button(toolbar, text="Open File", width=9, command=self.openfile)
        openfiletb.grid(column = 0, row = 0, padx = 5, pady= 5)
        runbtn = Button(toolbar, text="Populate", width = 8, command=self.populateButtonPressed)
        runbtn.grid(column=1, row=0, padx = 5, pady= 5)
        dicbtn = Button(toolbar, text="To PDF", width = 8, command=self.onPrintButtonPressed)
        dicbtn.grid(column=2, row=0, padx = 5, pady= 5)
        dbbtn = Button(toolbar, text="To DB", width = 8, command=self.onDbButtonPressed)
        dbbtn.grid(column=3, row=0, padx = 5, pady= 5)

        #runfiletb = Button(toolbar, text="Run File", width=6, command=self.set)
        #runfiletb.grid(column=2, row=0)

        ################################# Status Bar ######################################

        ################################## frame and grid ###################################
        #### Initalize ######
        #### Frame and FrameLabel for device & settings #####
        
        ##self.style.configure('TFrame', background='#2B2B2B')
        content = Frame(self)
        
        
        device_frame = LabelFrame(content, text="Device", borderwidth=5, width=200, height=150)
        settings_notebook = Notebook(content, padding= 10)
        settings_frame = Frame(settings_notebook)
        settings_frame_2 = Frame(settings_notebook)
        self.tree = Treeview(settings_frame_2, height=4, selectmode='browse') # The height is in rows


        # treeview columns
        self.tree["columns"] = ("one", "two", "three", "four")
        self.tree.column("#0", width=75, minwidth=25, stretch=1)
        self.tree.column("one", width=75, minwidth=25, stretch=1)
        self.tree.column("two", width=75, minwidth=25, stretch=1)
        self.tree.column("three", width=75, minwidth=25, stretch=1)
        self.tree.column("four", width=75, minwidth=25, stretch=1)
        
        # Treeview headings
        self.tree.heading("#0", text="Chamber", anchor=W)
        self.tree.heading("one", text="Voltage", anchor=W)
        self.tree.heading("two", text="Pulse Width", anchor=W)
        self.tree.heading("three", text="Polarity", anchor=W)
        self.tree.heading("four", text="Sensitivity", anchor=W)

        self.tree.insert("","end", iid=0, text="RA", values=("0.6", "0.7", "0.8", "0.9", "1.0", "1.1"))
        self.tree.insert("","end", iid=1, text="RV", values=("0.6", "0.7", "0.8", "0.9", "1.0", "1.1"))
        self.tree.insert("","end",iid=2, text="LV", values=("0.6", "0.7", "0.8", "0.9", "1.0", "1.1"))

        settings_notebook.add(settings_frame, text="Settings 1")
        settings_notebook.add(settings_frame_2, text="Settings 2")
        
        ##### Frame and FrameLabel for Episodes  #####
        episode = Frame(self)
        episode_frame = LabelFrame(episode, text="Episodes", borderwidth=5, width=200, height=150)
        ##### Frame for test editor #####
        editor_content = Frame(self)


        self.name_full_lbl = Label(device_frame, text="Full Name")
        self.name_full_entry = Entry(device_frame, textvariable="full_name")
        self.man_lbl = Label(device_frame, text="Manufacturer")
        self.man_entry = Entry(device_frame, textvariable="man")
        self.model_lbl = Label(device_frame, text="Model")
        self.model_entry = Entry(device_frame, text="model")
        self.serial_lbl = Label(device_frame, text="Serial")
        self.serial_entry = Entry(device_frame, textvariable="serial")
        self.type_lbl = Label(device_frame, text="Type")
        self.type_entry = Entry(device_frame, textvariable="type")
        self.lowrate_lbl = Label(device_frame, text="Low Rate")
        self.lowrate_entry = Entry(device_frame, textvariable="low_rate")
        self.implant_lbl = Label(device_frame, text="Implant Date")
        self.implant_entry = Entry(device_frame, textvariable="implant")
        self.sess_date_lbl = Label(device_frame, text="Session Date")# to change the font color / its a ttk widget add , background='white
        self.sess_date_entry = Entry(device_frame, textvariable="sess_date")
        

        # Settings tab 1
        self.dev_mode_lbl = Label(settings_frame, text="Mode")
        self.dev_mode_entry = Entry(settings_frame, textvariable="mode")
        self.dev_sensed_AV_delay_lbl = Label(settings_frame, text="Sensed AV")
        self.dev_sensed_AV_delay_entry = Entry(settings_frame, textvariable="sensed_AV_delay")
        
 
        self.dev_lrl_lbl = Label(settings_frame, text="Low Rate")
        self.dev_lrl_entry = Entry(settings_frame, textvariable="low_rate")
        self.dev_lrl_lbl_test_1 = Label(settings_frame, text="Lower Rate")
        self.dev_lrl_entry_test_1 = Entry(settings_frame, textvariable="lower_rate")


        self.dev_max_tracking_lbl = Label(settings_frame, text="Max Tracking")
        self.dev_max_tracking_entry = Entry(settings_frame, textvariable="max_tracking")

        # Settings tab 2


        # Episode Frame
        self.ep_af_lbl = Label(episode_frame, text="AF Burden")
        self.ep_af_entry = Entry(episode_frame, textvariable="af_burden")
        self.ep_ms_lbl = Label(episode_frame, text="Mode Switches")
        self.ep_ms_entry = Entry(episode_frame, textvariable="ms_episodes")



        ####### add to gui #####
        content.grid(column=0, row=1, sticky = (N,E,W), padx = 10, pady = 10)
        episode.grid(column=0, row=2, sticky= (N,E,W), padx = 10, pady=10)
        episode_frame.grid(column=0, row=0)
        editor_content.grid(column=0, row=3)

        ##### Sub frames of content frame
        device_frame.grid(column=0, row=0)
        settings_notebook.grid(column=1, row=0, padx= 10, pady = 10)
        self.tree.grid(column=0, row=0, sticky = (N,E,W))

        ############ Device Fields #############
        self.name_full_lbl.grid(column=0, row=1, sticky = E, padx = 5, pady = 3)
        self.name_full_entry.grid(column=1, row=1, columnspan=2, padx = 5, pady = 3)
        self.man_lbl.grid(column=0, row=2, sticky = E, padx = 5, pady = 3)
        self.man_entry.grid(column=1, row=2, columnspan=2, padx = 5, pady = 3)
        self.model_lbl.grid(column=0, row=3, sticky = E, padx = 5, pady = 3)
        self.model_entry.grid(column=1, row=3, columnspan=2, padx = 5, pady = 3)
        self.serial_lbl.grid(column=0, row=4, sticky = E, padx = 5, pady = 3)
        self.serial_entry.grid(column=1, row=4, columnspan=2, padx = 5, pady = 3)
        self.type_lbl.grid(column=3, row=1, sticky = E, padx = 5, pady = 3)
        self.type_entry.grid(column=4, row=1, columnspan=2, padx = 5, pady = 3)
        self.lowrate_lbl.grid(column=3, row=2, sticky = E, padx = 5, pady = 3)
        self.lowrate_entry.grid(column=4, row=2, columnspan=2, padx = 5, pady = 3)
        self.implant_lbl.grid(column=3, row=3, sticky = E, padx = 5, pady = 3)
        self.implant_entry.grid(column=4, row=3, columnspan=2, padx = 5, pady = 3)
        self.sess_date_lbl.grid(column=3, row=4, sticky=E, padx=5, pady=3)
        self.sess_date_entry.grid(column=4, row=4, columnspan=2, padx=5, pady=3)


        ############ Settings Tab 1 Fields #############
        self.dev_mode_lbl.grid(column=0, row=1, sticky = E, padx = 5, pady = 3)
        self.dev_mode_entry.grid(column=1, row=1, columnspan=2, padx = 5, pady = 3)
        self.dev_sensed_AV_delay_lbl.grid(column=3, row=1, sticky = E, padx = 5, pady = 3)
        self.dev_sensed_AV_delay_entry.grid(column=4, row=1, columnspan=2, padx = 5, pady = 3)

        self.dev_lrl_lbl.grid(column=0, row=2, sticky = E, padx = 5, pady = 3)
        self.dev_lrl_entry.grid(column=1, row=2, columnspan=2, padx = 5, pady = 3)
        self.dev_max_tracking_lbl.grid(column=0, row=3, sticky = E, padx = 5, pady = 3)
        self.dev_max_tracking_entry.grid(column=1, row=3, columnspan=2, padx = 5, pady=3)
        self.dev_lrl_lbl_test_1.grid(column=3, row=2, sticky = E, padx = 5, pady = 3)
        self.dev_lrl_entry_test_1.grid(column=4, row=2, columnspan=2, padx = 5, pady = 3)

        ############ Settings Tab 2 Fields #############
    


        ########## Episode Fields ########
        self.ep_af_lbl.grid(column=0, row=0, sticky = E, padx = 5, pady = 3)
        self.ep_af_entry.grid(column=1, row=0, columnspan=2, padx = 5, pady = 3)
        self.ep_ms_lbl.grid(column=0, row=1, sticky = E, padx = 5, pady = 3)
        self.ep_ms_entry.grid(column=1, row=1, columnspan=2, padx = 5, pady = 3)
        
        ########## Comment Editor ########
        self.editor = tkst.ScrolledText(master = editor_content, wrap = WORD, width = 75, height = 15, font=("Helvetica", 12))
        self.editor.grid(column = 0, columnspan = 3, padx = 10, pady = 10)

        self.treeview = self.tree


    def openfile(self):
        global fileName
        fileName = tk.filedialog.askopenfilename(
                               filetypes=(("Abbott", "*.log"), ("Biotronik", "*.xml"), ("Boston Scientific", "*.bnk")),
                               title="Choose a file."
                               )
        print(fileName)
        return fileName
        # Using try in case user types in unknown file or closes without choosing a file.
        #try:
            #with open(name, 'r') as UseFile:
                #print(UseFile.read())
        #except:
            #print("No file exists")
    
    def populateButtonPressed(self):
        #Bring in Data class and instatiate it.
        d = getData.Data()
        self.dataDict = d.data(fileName)
        print(self.dataDict)
        # Clear contents of entry widgets
        self.model_entry.delete(0, END)
        self.dev_mode_entry.delete(0, END)
        self.type_entry.delete(0, END)
        self.serial_entry.delete(0, END)
        self.man_entry.delete(0, END)
        self.name_full_entry.delete(0, END)
        self.lowrate_entry.delete(0, END)
        self.sess_date_entry.delete(0, END)
        self.dev_max_tracking_entry.delete(0, END)
        self.dev_sensed_AV_delay_entry.delete(0, END)
        # Populate entry widgets
        self.model_entry.insert(0, self.dataDict['model'])
        self.dev_mode_entry.insert(0, self.dataDict['mode'])
        self.type_entry.insert(0, self.dataDict['type'])
        self.serial_entry.insert(0, self.dataDict['serial'])
        self.man_entry.insert(0, self.dataDict['mfg'])
        self.name_full_entry.insert(0, self.dataDict['name_given']+ ' ' + self.dataDict['name_family'])
        self.lowrate_entry.insert(0, self.dataDict['lowrate'])
        check_date = datetime.datetime.strptime(self.dataDict['sess_date'], "%Y%m%dT%H%M%S%z").replace(tzinfo=None)
        self.sess_date_entry.insert(0, check_date)
        self.treeview.set(0,"two", value="5.0")
        self.dev_max_tracking_entry.insert(0, self.dataDict['max_tracking'])
        self.dev_sensed_AV_delay_entry.insert(0, self.dataDict['sensed_AV_delay'])

        

    def onPrintButtonPressed(self):
        text = self.editor.get("1.0",END)
        #comments = {'comments':text}
        #bioDict.update = (comments)
        self.dataDict.update({'comments':text})
        print(self.dataDict)
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("./templates/report.html")
        html_out = template.render(self.dataDict)
        HTML(string=html_out).write_pdf("report.pdf")
        #subprocess.Popen("~/Documents/GitHub/xml_report/report.pdf",shell=True)
        print(text)
    
    def onDbButtonPressed(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        print("Opened database successfully")   
        c.execute('''INSERT INTO device ( serial, type, model, mode, mfg, lowrate, max_tracking_rate, name_given, name_family, sess_date) VALUES (?,?,?,?,?,?,?,?,?,?)''', (self.dataDict['serial'], self.dataDict['type'], self.dataDict['model'], self.dataDict['mode'], self.dataDict['mfg'], self.dataDict['lowrate'], self.dataDict['max_tracking_rate'], self.dataDict['name_given'], self.dataDict['name_family'], self.dataDict['sess_date']))
        conn.commit()
        conn.close()
        print(self.typeentry.get())
    
if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()

