import tkinter
from tkinter import filedialog
import tkinter.ttk
import os.path
import tkinter.messagebox
import subprocess
from daemon import sftp_connect
import paramiko
import socket
import json


class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.pack(expand=True,fill="both", padx=4, pady=4)
        self.master.title("UNICLUST") 

        self.restart_daemon()


    def restart_daemon(self):
        try:
            self.kill_daemon()
        except Exception as ex:
            print(ex)

        try:
            self.start_daemon()
        except Exception as ex:
            print(ex)

    
    def kill_daemon(self):
        host = "localhost"
        port = 1337
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            s.sendall(b'end')

            s.recv(1024)


    def start_daemon(self):
        subprocess.Popen(['python3', 'daemon.py'])


    def on_conf_pr_task(self, evt):
        self.canvas_pr_task.itemconfig(self.canvas_frame_pr_task, width=evt.width)

    def on_frame_conf_pr_task(self, evt):
        self.canvas_pr_task.configure(scrollregion=self.canvas_pr_task.bbox("all"))


    def on_conf_ma_task(self, evt):
        self.canvas_ma_task.itemconfig(self.canvas_frame_ma_task, width=evt.width)

    def on_frame_conf_ma_task(self, evt):
        self.canvas_ma_task.configure(scrollregion=self.canvas_ma_task.bbox("all"))


    def on_conf_pr_fil(self, evt):
        self.canvas_pr_fil.itemconfig(self.canvas_frame_pr_fil, width=evt.width)

    def on_frame_conf_pr_fil(self, evt):
        self.canvas_pr_fil.configure(scrollregion=self.canvas_pr_fil.bbox("all"))


    def on_conf_up_fil(self, evt):
        self.canvas_up_fil.itemconfig(self.canvas_frame_up_fil, width=evt.width)

    def on_frame_conf_up_fil(self, evt):
        self.canvas_up_fil.configure(scrollregion=self.canvas_up_fil.bbox("all"))


    def on_conf_do_fil(self, evt):
        self.canvas_do_fil.itemconfig(self.canvas_frame_do_fil, width=evt.width)

    def on_frame_conf_do_fil(self, evt):
        self.canvas_do_fil.configure(scrollregion=self.canvas_do_fil.bbox("all"))


    def on_conf_del_fil(self, evt):
        self.canvas_del_fil.itemconfig(self.canvas_frame_del_fil, width=evt.width)

    def on_frame_conf_del_fil(self, evt):
        self.canvas_del_fil.configure(scrollregion=self.canvas_del_fil.bbox("all"))

    def create_widgets(self):
        ''' Notebook frame '''
        ntb = tkinter.ttk.Notebook(self)
        ntb.pack(fill="both", padx=4, pady=4, expand=True)
        ''' end '''
        

        ''' window on Notebook '''
        self.frame_pr_task = tkinter.ttk.Frame(ntb)
        self.sum_of_task = 0
        self.frame_ma_task = tkinter.ttk.Frame(ntb)
        self.frame_pr_fil = tkinter.ttk.Frame(ntb)
        self.sum_of_up_task = 0
        self.sum_of_do_task = 0
        self.frame_up_fil = tkinter.ttk.Frame(ntb)
        self.frame_do_fil = tkinter.ttk.Frame(ntb)
        self.frame_del_fil = tkinter.ttk.Frame(ntb)
        ''' end '''


        ''' add '''
        ntb.add(self.frame_pr_task, text="ПРОГРЕСС ЗАДАЧ", padding=4)
        ntb.add(self.frame_ma_task, text="СОЗДАТЬ ЗАДАЧУ", padding=4)
        ntb.add(self.frame_pr_fil, text="ПРОГРЕСС ФАЙЛОВ", padding=4)
        ntb.add(self.frame_up_fil, text="ЗАГРУЗИТЬ ФАЙЛЫ", padding=4)
        ntb.add(self.frame_do_fil, text="СКАЧАТЬ ФАЙЛЫ", padding=4)
        ntb.add(self.frame_del_fil, text="УДАЛИТЬ ФАЙЛЫ", padding=4)
        ''' end '''
        

        ''' scrollbar on self.frame_pr_task '''
        self.canvas_pr_task = tkinter.Canvas(self.frame_pr_task)
        self.canvas_pr_task.pack(side='left', fill='both', expand=True)

        self.frame_pr_task_dop = tkinter.ttk.Frame(self.canvas_pr_task)

        self.canvas_frame_pr_task = self.canvas_pr_task.create_window((0, 0), \
                window=self.frame_pr_task_dop, anchor=tkinter.NW)

        self.scrollbar_pr_task = tkinter.ttk.Scrollbar(self.frame_pr_task, orient='vertical', \
                command=self.canvas_pr_task.yview)
        self.scrollbar_pr_task.pack(side='right', fill = 'y')

        self.canvas_pr_task.config(yscrollcommand=self.scrollbar_pr_task.set)


        self.frame_pr_task_dop.bind('<Configure>', self.on_frame_conf_pr_task)
        self.canvas_pr_task.bind('<Configure>', self.on_conf_pr_task)
        ''' end '''


        ''' scrollbar on self.frame_ma_task '''
        self.canvas_ma_task = tkinter.Canvas(self.frame_ma_task)
        self.canvas_ma_task.pack(side='left', fill='both', expand=True)

        self.frame_ma_task_dop = tkinter.ttk.Frame(self.canvas_ma_task)

        self.canvas_frame_ma_task = self.canvas_ma_task.create_window((0, 0), \
                window=self.frame_ma_task_dop, anchor=tkinter.NW)

        self.scrollbar_ma_task = tkinter.ttk.Scrollbar(self.frame_ma_task, orient='vertical', \
                command=self.canvas_ma_task.yview)
        self.scrollbar_ma_task.pack(side='right', fill = 'y')

        self.canvas_ma_task.config(yscrollcommand=self.scrollbar_ma_task.set)


        self.frame_ma_task_dop.bind('<Configure>', self.on_frame_conf_ma_task)
        self.canvas_ma_task.bind('<Configure>', self.on_conf_ma_task)
        ''' end '''


        ''' scrollbar on self.frame_pr_fil '''
        self.canvas_pr_fil = tkinter.Canvas(self.frame_pr_fil)
        self.canvas_pr_fil.pack(side='left', fill='both', expand=True)

        self.frame_pr_fil_dop = tkinter.ttk.Frame(self.canvas_pr_fil)

        self.canvas_frame_pr_fil = self.canvas_pr_fil.create_window((0, 0), \
                window=self.frame_pr_fil_dop, anchor=tkinter.NW)

        self.scrollbar_pr_fil = tkinter.ttk.Scrollbar(self.frame_pr_fil, orient='vertical', \
                command=self.canvas_pr_fil.yview)
        self.scrollbar_pr_fil.pack(side='right', fill = 'y')

        self.canvas_pr_fil.config(yscrollcommand=self.scrollbar_pr_fil.set)


        self.frame_pr_fil_dop.bind('<Configure>', self.on_frame_conf_pr_fil)
        self.canvas_pr_fil.bind('<Configure>', self.on_conf_pr_fil)
        ''' end '''


        ''' scrollbar on self.frame_up_fil '''
        self.canvas_up_fil = tkinter.Canvas(self.frame_up_fil)
        self.canvas_up_fil.pack(side='left', fill='both', expand=True)

        self.frame_up_fil_dop = tkinter.ttk.Frame(self.canvas_up_fil)

        self.canvas_frame_up_fil = self.canvas_up_fil.create_window((0, 0), \
                window=self.frame_up_fil_dop, anchor=tkinter.NW)

        self.scrollbar_up_fil = tkinter.ttk.Scrollbar(self.frame_up_fil, orient='vertical', \
                command=self.canvas_up_fil.yview)
        self.scrollbar_up_fil.pack(side='right', fill = 'y')

        self.canvas_up_fil.config(yscrollcommand=self.scrollbar_up_fil.set)


        self.frame_up_fil_dop.bind('<Configure>', self.on_frame_conf_up_fil)
        self.canvas_up_fil.bind('<Configure>', self.on_conf_up_fil)
        ''' end '''


        ''' scrollbar on self.frame_do_fil '''
        self.canvas_do_fil = tkinter.Canvas(self.frame_do_fil)
        self.canvas_do_fil.pack(side='left', fill='both', expand=True)

        self.frame_do_fil_dop = tkinter.ttk.Frame(self.canvas_do_fil)

        self.canvas_frame_do_fil = self.canvas_do_fil.create_window((0, 0), \
                window=self.frame_do_fil_dop, anchor=tkinter.NW)

        self.scrollbar_do_fil = tkinter.ttk.Scrollbar(self.frame_do_fil, orient='vertical', \
                command=self.canvas_do_fil.yview)
        self.scrollbar_do_fil.pack(side='right', fill = 'y')

        self.canvas_do_fil.config(yscrollcommand=self.scrollbar_do_fil.set)


        self.frame_do_fil_dop.bind('<Configure>', self.on_frame_conf_do_fil)
        self.canvas_do_fil.bind('<Configure>', self.on_conf_do_fil)
        ''' end '''


        ''' scrollbar on self.frame_del_fil '''
        self.canvas_del_fil = tkinter.Canvas(self.frame_del_fil)
        self.canvas_del_fil.pack(side='left', fill='both', expand=True)

        self.frame_del_fil_dop = tkinter.ttk.Frame(self.canvas_del_fil)

        self.canvas_frame_del_fil = self.canvas_del_fil.create_window((0, 0), \
                window=self.frame_del_fil_dop, anchor=tkinter.NW)

        self.scrollbar_del_fil = tkinter.ttk.Scrollbar(self.frame_del_fil, orient='vertical', \
                command=self.canvas_del_fil.yview)
        self.scrollbar_del_fil.pack(side='right', fill = 'y')

        self.canvas_del_fil.config(yscrollcommand=self.scrollbar_del_fil.set)


        self.frame_del_fil_dop.bind('<Configure>', self.on_frame_conf_del_fil)
        self.canvas_del_fil.bind('<Configure>', self.on_conf_del_fil)
        ''' end '''

        
        ''' fill the window in the Notebook '''
        self.widgest_pr_task()
        self.widgets_pr_fil()
        self.widgets_up_fil()
        self.widgets_do_fil()
        self.widgets_ma_task()
        ''' end '''

        self.btnUpdatState.event_generate("<ButtonRelease>")


    def widgest_pr_task(self):
       pass


    def widgets_pr_fil(self):
        ''' make butoon '''
        self.btnUpdatState = tkinter.ttk.Button(self.frame_pr_fil_dop, text="ОБНОВИТЬ СОСТОЯНИЕ")
        self.btnUpdatState.bind("<ButtonRelease>", self.UpdateFil)
        self.btnDelComplTask = tkinter.ttk.Button(self.frame_pr_fil_dop, text="УДАЛИТЬ ЗАВЕРШЕННЫЕ ЗАДАЧИ", \
                command=self.DelFilTask)
        ''' end '''


        ''' button pack '''
        self.btnUpdatState.grid(row=0, column=0,  padx=4, pady=4)
        self.btnDelComplTask.grid(row=0, column=1, padx=4, pady=4)
        ''' end '''


        ''' grid expand.True '''
        for i in range(1):
            self.frame_pr_fil_dop.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.frame_pr_fil_dop.grid_columnconfigure(i, weight=1)
        ''' end '''


        ''' data and metadata for task '''
        self.task_up_name = []
        self.fil_name_up = []
        self.pr_fil_up_frame = []
        self.size_fil_up = []
        self.count_size_fil_up = []
            
        self.frame_up = [0] * len(self.fil_name_up)

        self.lbl_fil_name_up_frame = [[] for i in range(len(self.fil_name_up))]
        self.prgrbr_fil_up = [[] for i in range(len(self.fil_name_up))]
        self.lbl_info_fil_up = [[] for i in range(len(self.fil_name_up))]
        self.spn_pr_fil_up_frame = [[] for i in range(len(self.fil_name_up))]
        self.int_var_spn_pr_fil_up_frame = [[tkinter.IntVar() for j in range(len(self.fil_name_up[i]))] \
                for i in range(len(self.fil_name_up))]
        self.lbl_pr_fil_up = [[] for i in range(len(self.fil_name_up))]


        self.rbtn_up = [0] * len(self.fil_name_up) 
        self.rbtn_up_meta = [0] * len(self.fil_name_up) 


        self.task_down_name = []
        self.fil_name_down = []
        self.pr_fil_down_frame = []
        self.size_fil_down = []
        self.count_size_fil_down = []
        
        self.frame_down = [0] * len(self.fil_name_down)

        self.lbl_fil_name_down_frame = [[] for i in range(len(self.fil_name_down))]
        self.prgrbr_fil_down = [[] for i in range(len(self.fil_name_down))]
        self.lbl_info_fil_down = [[] for i in range(len(self.fil_name_up))]
        self.spn_pr_fil_down_frame = [[] for i in range(len(self.fil_name_down))]
        self.int_var_spn_pr_fil_down_frame = [[tkinter.IntVar() for j in range(len(self.fil_name_down[i]))] \
                for i in range(len(self.fil_name_down))]
        self.lbl_pr_fil_down = [[] for i in range(len(self.fil_name_down))] 


        self.rbtn_down = [0] * len(self.fil_name_down)
        self.rbtn_down_meta = [0] * len(self.fil_name_down) 
        ''' end '''


    def UpdateFil(self, evt):
        ''' delete old widgets '''
        self.btnUpdatState.grid_remove()
        self.btnDelComplTask.grid_remove()

        for i in self.frame_down:
            i.grid_remove()
            i.destroy()

        for i in self.frame_up:
            i.grid_remove()
            i.destroy()
        ''' end '''

        
        ''' set Null a new widgets '''
        self.task_up_name = []
        self.fil_name_up = []
        self.pr_fil_up_frame = []
        self.size_fil_up = []
        self.count_size_fil_up = []
            

        self.task_down_name = []
        self.fil_name_down = []
        self.pr_fil_down_frame = []
        self.size_fil_down = []
        self.count_size_fil_down = []
        ''' end '''


        ''' download information about request from db '''
        """
        run your database communication program 
        """
        ''' end '''


        ''' set widget size '''
        self.frame_up = [0] * len(self.fil_name_up)

        self.lbl_fil_name_up_frame = [[] for i in range(len(self.fil_name_up))]
        self.prgrbr_fil_up = [[] for i in range(len(self.fil_name_up))]
        self.lbl_info_fil_up = [[] for i in range(len(self.fil_name_up))]
        self.spn_pr_fil_up_frame = [[] for i in range(len(self.fil_name_up))]
        self.int_var_spn_pr_fil_up_frame = [[tkinter.IntVar() for j in range(len(self.fil_name_up[i]))] \
                for i in range(len(self.fil_name_up))]
        self.lbl_pr_fil_up = [[] for i in range(len(self.fil_name_up))]


        self.rbtn_up = [0] * len(self.fil_name_up) 
        self.rbtn_up_meta = [0] * len(self.fil_name_up) 


        self.frame_down = [0] * len(self.fil_name_down)

        self.lbl_fil_name_down_frame = [[] for i in range(len(self.fil_name_down))]
        self.prgrbr_fil_down = [[] for i in range(len(self.fil_name_down))]
        self.lbl_info_fil_down = [[] for i in range(len(self.fil_name_up))]
        self.spn_pr_fil_down_frame = [[] for i in range(len(self.fil_name_down))]
        self.int_var_spn_pr_fil_down_frame = [[tkinter.IntVar() for j in range(len(self.fil_name_down[i]))] \
                for i in range(len(self.fil_name_down))]
        self.lbl_pr_fil_down = [[] for i in range(len(self.fil_name_down))] 


        self.rbtn_down = [0] * len(self.fil_name_down)
        self.rbtn_down_meta = [0] * len(self.fil_name_down) 
        ''' end '''


        N = len(self.frame_up) + len(self.frame_down)

        self.btnUpdatState.grid(row=N, column=0, padx=4, pady=4)
        self.btnDelComplTask.grid(row=N, column=1, padx=4, pady=4)

        for i in range(len(self.fil_name_up)):
            self.frame_up[i] = tkinter.ttk.LabelFrame(self.frame_pr_fil_dop, text=self.task_up_name[i])
            self.rbtn_up_meta[i] = tkinter.IntVar()
            self.rbtn_up_meta[i].set(1)
            self.rbtn_up[i] = [tkinter.ttk.Radiobutton(self.frame_up[i], text="ЗАГРУЗКА", value=1, \
                    variable =self.rbtn_up_meta[i], command=self.Rbtn_pr_fil_sig_1),\
                               tkinter.ttk.Radiobutton(self.frame_up[i], text="ОСТАНОВКА", value=2, \
                               variable =self.rbtn_up_meta[i], command=self.Rbtn_pr_fil_sig_2),\
                               tkinter.ttk.Radiobutton(self.frame_up[i], text="ИЗМЕНЕНИТЬ ПРИОРИТЕТ", \
                               value=3, variable =self.rbtn_up_meta[i], command=self.Rbtn_pr_fil_sig_3)]

            for j in range(3):
                self.rbtn_up[i][j].grid(row=0, column=j, padx=4, pady=4)
            self.frame_up[i].grid_rowconfigure(0, weight=1)
            for k in range(4):
                self.frame_up[i].grid_columnconfigure(k, weight=1)

            self.frame_up[i].grid(row=i, columnspan=2, padx=4, pady=4)

            for j in range(len(self.fil_name_up[i])):
                self.lbl_fil_name_up_frame[i].append(tkinter.ttk.Label(self.frame_up[i], text=self.fil_name_up[i][j]))
                self.lbl_fil_name_up_frame[i][j].grid(row=j+1, column=0, padx=4, pady=4)

                self.prgrbr_fil_up[i].append(tkinter.ttk.Progressbar(self.frame_up[i], orient='horizontal', \
                        length=200, mode='determinate', maximum=self.size_fil_up[i][j], \
                        value=self.count_size_fil_up[i][j]))

                self.prgrbr_fil_up[i][j].grid(row=j+1, column=1, padx=4, pady=4)

                self.lbl_info_fil_up[i].append(tkinter.ttk.Label(self.frame_up[i], \
                        text=f"{self.count_size_fil_up[i][j]} / {self.size_fil_up[i][j]} " \
                                f"({100 * self.count_size_fil_up[i][j] / self.size_fil_up[i][j]:.2f} %)"))
                self.lbl_info_fil_up[i][j].grid(row=j+1, column=2, padx=4, pady=4)

                self.int_var_spn_pr_fil_up_frame[i][j].set(self.pr_fil_up_frame[i][j])
                self.spn_pr_fil_up_frame[i].append(tkinter.Spinbox(self.frame_up[i], textvariable=\
                        self.int_var_spn_pr_fil_up_frame[i][j], from_=1, to=100, increment=1, exportselection=0))

                self.lbl_pr_fil_up[i].append(tkinter.ttk.Label(self.frame_up[i], \
                        text=f"ПРИОРИТЕТ: {self.int_var_spn_pr_fil_up_frame[i][j].get()}"))
                self.lbl_pr_fil_up[i][j].grid(row=j+1, column=3, padx=4, pady=4)

                self.frame_up[i].grid_rowconfigure(j + 1, weight=1)

        for i in range(len(self.fil_name_down)):
            self.frame_down[i] = tkinter.ttk.LabelFrame(self.frame_pr_fil_dop, text=self.task_down_name[i])
            self.rbtn_down_meta[i] = tkinter.IntVar()
            self.rbtn_down_meta[i].set(1)
            self.rbtn_down[i] = [tkinter.ttk.Radiobutton(self.frame_down[i], text="СКАЧИВАНИЕ", value=1, \
                    variable=self.rbtn_down_meta[i], command=self.Rbtn_pr_fil_sig_1),\
                               tkinter.ttk.Radiobutton(self.frame_down[i], text="ОСТАНОВКА", value=2, \
                               variable=self.rbtn_down_meta[i], command=self.Rbtn_pr_fil_sig_2),\
                               tkinter.ttk.Radiobutton(self.frame_down[i], text="ИЗМЕНЕНИТЬ ПРИОРИТЕТ", \
                               value=3, variable=self.rbtn_down_meta[i], command=self.Rbtn_pr_fil_sig_3)]

            for j in range(3):
                self.rbtn_down[i][j].grid(row=0, column=j, padx=4, pady=4)
            self.frame_down[i].grid_rowconfigure(0, weight=1)
            for k in range(4):
                self.frame_down[i].grid_columnconfigure(k, weight=1)

            self.frame_down[i].grid(row=i+len(self.fil_name_up), columnspan=2, padx=4, pady=4)

            for j in range(len(self.fil_name_down[i])):
                self.lbl_fil_name_down_frame[i].append(tkinter.ttk.Label(self.frame_down[i], \
                        text=self.fil_name_down[i][j]))
                self.lbl_fil_name_down_frame[i][j].grid(row=j+1, column=0, padx=4, pady=4)

                self.prgrbr_fil_down[i].append(tkinter.ttk.Progressbar(self.frame_down[i], orient='horizontal', \
                        length=200, mode='determinate', maximum=self.size_fil_down[i][j], \
                        value=self.count_size_fil_down[i][j]))

                self.prgrbr_fil_down[i][j].grid(row=j+1, column=1, padx=4, pady=4)

                self.lbl_info_fil_down[i].append(tkinter.ttk.Label(self.frame_down[i], \
                        text=f" {self.count_size_fil_down[i][j]} / {self.size_fil_down[i][j]} "\
                                f"({100 * self.count_size_fil_down[i][j] / self.size_fil_down[i][j]:.2f} %)"))
                self.lbl_info_fil_down[i][j].grid(row=j+1, column=2, padx=4, pady=4)

                self.int_var_spn_pr_fil_down_frame[i][j].set(self.pr_fil_down_frame[i][j])
                self.spn_pr_fil_down_frame[i].append(tkinter.Spinbox(self.frame_down[i], \
                        textvariable=self.int_var_spn_pr_fil_down_frame[i][j], from_=1, to=100, increment=1, \
                        exportselection=0))

                self.lbl_pr_fil_down[i].append(tkinter.ttk.Label(self.frame_down[i], \
                        text=f"ПРИОРИТЕТ: {self.int_var_spn_pr_fil_down_frame[i][j].get()}"))
                self.lbl_pr_fil_down[i][j].grid(row=j+1, column=3, padx=4, pady=4)

                self.frame_down[i].grid_rowconfigure(j + 1, weight=1)


        for i in range(N+1):
            self.frame_pr_fil_dop.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.frame_pr_fil_dop.grid_columnconfigure(i, weight=1)


    def Rbtn_pr_fil_sig_1(self):
        pass
        
    def Rbtn_pr_fil_sig_2(self):
        pass

    def Rbtn_pr_fil_sig_3(self):
        pass

    def DelFilTask(self):
        pass


    def parser_fetchall(self):
        with open("data/3.txt", "r") as fd:
            while s := fd.readline():
                if s.split()[0] == 'down':
                    break

                lname, lsize, lserver = s.split()
                self.task_up_name.append(lname)

                self.fil_name_up.append([0] * int(lsize))
                self.pr_fil_up_frame.append([0] * int(lsize))
                self.size_fil_up.append([0] * int(lsize))
                self.count_size_fil_up.append([0] * int(lsize))


                with open(lserver, 'r') as fd:
                    server = json.load(fd)

                with open(server['password'], 'r') as fd:
                    server['password'] = fd.readline()[:-1]

                server['key'] = paramiko.RSAKey.from_private_key_file(server['key'], server['password'])

                sftp = sftp_connect(server['ip'], server['username'], server['key'], server['port'])

                for i in range(int(lsize)):
                    *vr, self.pr_fil_up_frame[-1][i], self.size_fil_up[-1][i] = fd.readline().split()
                    self.fil_name_up[-1][i] = ' '.join(vr)

                    #self.count_size_fil_up[-1][i] = os.path.getsize(self.fil_name_up[-1][i])
                    self.fil_name_up[-1][i] = os.path.basename(self.fil_name_up[-1][i])
                    self.pr_fil_up_frame[-1][i] = int(self.pr_fil_up_frame[-1][i])
                    self.size_fil_up[-1][i] = int(self.size_fil_up[-1][i])

                    try:
                        self.count_size_fil_up[-1][i] = sftp.stat(self.fil_name_up[-1][i]).st_size
                    except:
                        self.count_size_fil_up[-1][i] = 0

                sftp.close()

            while s := fd.readline():
                lname, lsize, lserver = s.split()
                self.task_down_name.append(lname)

                self.fil_name_down.append([0] * int(lsize))
                self.pr_fil_down_frame.append([0] * int(lsize))
                self.size_fil_down.append([0] * int(lsize))
                self.count_size_fil_down.append([0] * int(lsize))

                for i in range(int(lsize)):
                    *vr, self.pr_fil_down_frame[-1][i], self.size_fil_down[-1][i] = fd.readline().split()
                    self.fil_name_down[-1][i] = ' '.join(vr)

                    self.fil_name_down[-1][i] = os.path.basename(self.fil_name_down[-1][i])
                    self.pr_fil_down_frame[-1][i] = int(self.pr_fil_down_frame[-1][i])
                    self.size_fil_down[-1][i] = int(self.size_fil_down[-1][i])  

                    vr_path = os.path.join(os.path.getcwd(), 'data', self.fil_name_down[-1][i])
                    
                    if os.path.exists(vr_path):
                        self.count_size_fil_down[-1][i] = os.path.getsize(vr_path)
                    else:
                        self.count_size_fil_down[-1][i] = 0

                  
    def widgets_up_fil(self):
        ''' make button '''
        btnAddRow = tkinter.ttk.Button(self.frame_up_fil_dop, text="ДОБАВИТЬ СЛОТ ДЛЯ ЗАГРУЗКИ", \
                command=self.wid_AddRow)
        btnRemRow = tkinter.ttk.Button(self.frame_up_fil_dop, text="УДАЛИТЬ СЛОТ ДЛЯ ЗАГРУЗКИ", \
                command=self.wid_RemRow)
        btnAddUp = tkinter.ttk.Button(self.frame_up_fil_dop, text="СОЗДАТЬ ЗАПРОС", \
                command=self.wid_AddUp)
        ''' end '''
        

        ''' grid expand.True '''
        for i in range(2):
            self.frame_up_fil_dop.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.frame_up_fil_dop.grid_columnconfigure(i, weight=1)
        ''' end '''


        ''' bth pack '''
        btnAddRow.grid(row=1, column=0, padx=4, pady=4)
        btnAddUp.grid(row=1, column=2, padx=4, pady=4)
        btnRemRow.grid(row=1, column=1, padx=4, pady=4)
        ''' end '''

        
        ''' make LabelFrame for task for up_fil '''
        self.frame_n_z = tkinter.ttk.LabelFrame(self.frame_up_fil_dop, text="ЗАПРОС НА ЗАГРУЗКУ")
        ''' end '''


        ''' data and metadata about task '''
        self.name_of_up_fil_task = tkinter.StringVar()
        self.name_of_up_fil_task.set('Введите название запроса')
        self.ntr_name_of_up_fil_task = tkinter.ttk.Entry(self.frame_n_z, textvariable=self.name_of_up_fil_task)
        self.sum_of_fil_up = 0
        self.data_fil_name_up = []
        self.data_pr_fil_up = []
        self.lbl_fil_name_up = []
        self.pr_fil_up = []
        self.spn_pr_fil_up = []
        self.file_flag = True
        ''' end '''
        
        lblF_u = tkinter.ttk.Label(self.frame_n_z, text="ВЫБРАННЫЙ ФАЙЛ")
        lblP_u = tkinter.ttk.Label(self.frame_n_z, text="ПРИОРИТЕТ")

        lblF_u.grid(row=1, column=0, padx=4, pady=4)
        lblP_u.grid(row=1, column=1, padx=4, pady=4)

        self.frame_n_z.grid(row=0, column=0, columnspan=3, padx=4, pady=4, )

        self.ntr_name_of_up_fil_task.grid(row=0, columnspan=2, padx=4, pady=4)


    def open_file(self, evt):
        filename = filedialog.askopenfilename(title="test", filetypes=(("All", "*.*"), ))

        if filename:
            if filename in self.data_fil_name_up:
                if tkinter.messagebox.askretrycancel("ОШИБКА", "ДАННЫЙ ФАЙЛ УЖЕ НАХОДИТСЯ В ЗАДАЧЕ"):
                    self.open_file(evt)

                return

            self.file_flag = True
            self.sum_of_fil_up += 1
            self.btn_op_fil.grid_remove()
            self.data_fil_name_up.append(filename)
            filename = os.path.basename(filename)
            self.pr_fil_up.append(tkinter.DoubleVar())
            self.pr_fil_up[-1].set(0.0)
            self.spn_pr_fil_up.append(tkinter.Spinbox(self.frame_n_z, textvariable=self.pr_fil_up[-1], from_=0.0, \
                                                      to=1.0, increment=0.01, exportselection=0))
            self.spn_pr_fil_up[-1].grid(row=self.sum_of_fil_up+1, column = 1, padx=4, pady=4)
            self.lbl_fil_name_up.append(tkinter.ttk.Label(self.frame_n_z, text=filename))
            self.lbl_fil_name_up[-1].grid(row = self.sum_of_fil_up+1, column=0, padx=4, pady=4)
        else:
            self.btn_op_fil.grid_remove()
            self.file_flag = True


    def widgets_do_fil(self):
        pass


    def widgets_ma_task(sel):
        pass


    ''' foo when button <ДОБАВИТЬ СЛОТ ДЛЯ ЗАГРУЗКИ> press '''
    def wid_AddRow(self):
        if not self.file_flag:
            return 
        self.file_flag = False
        self.btn_op_fil = tkinter.ttk.Button(self.frame_n_z, text="FILE")
        self.btn_op_fil.bind("<ButtonRelease>", self.open_file)
        self.btn_op_fil.grid(row=(self.sum_of_fil_up+2), columnspan=2)
    ''' end '''


    def wid_RemRow(self):
        if tkinter.messagebox.askyesno("ПРЕДУПРЕЖДЕНИЕ", "ВЫ УВЕРЕНЫ,ЧТО ХОТИТЕ УДАЛИТЬ СЛОТ ДЛЯ ФАЙЛА"):
            if self.btn_op_fil in self.frame_n_z.grid_slaves():
                self.btn_op_fil.grid_remove()
                self.file_flag = True
            else:
                self.sum_of_fil_up -= 1
                self.data_fil_name_up.pop()
                vr = self.spn_pr_fil_up.pop()
                vr.grid_remove()
                vr.destroy()
                self.pr_fil_up.pop()
                vr = self.lbl_fil_name_up.pop()
                vr.grid_remove()
                vr.destroy()


    def gcd(a, b):
        while a * b:
            if a > b:
                a %= b
            else:
                b %= a

        return a + b


    def wid_AddUp(self):
        if self.sum_of_fil_up == 0:
            tkinter.messagebox.showwarning("ОШИБКА", "В ЗАДАЧЕ НЕТ НИ ОДНОГО ФАЙЛА")
            return

        sum_pr = 0

        for i in range(len(self.data_fil_name_up)):
            sum_pr += self.pr_fil_up[i].get()

        if sum_pr != 1.0:
            tkinter.messagebox.showwarning("ОШИБКА", "СУММА ПРИОРИТЕТОВ ФАЙЛОВ НЕ РАВНА 1")
            return

        deep = 0
        vr_pr = []
        for i in range(len(self.data_fil_name_up)):
            deep = max(len(str(self.pr_fil_up[i].get())) - 2)
            vr_pr.append(self.pr_fil_up[i].get())
        
        for i in range(len(vr_pr)):
            vr_pr[i] *= 10**deep
            vr_pr[i] = int(vr_pr[i])

        gcd_pr = vr_pr[0]
        
        for i in range(1, len(vr_pr)):
            gcd_pr = self.gcd(gcd_pr, vr_pr[i])

        for i in range(len(vr_pr)):
            vr_pr[i] /= gcd_pr

        if tkinter.messagebox.askyesno("ПРЕДУПРЕЖДЕНИЕ", "ВЫ УВЕРЕНЫ,ЧТО ХОТИТЕ ДОБАВИТЬ ЗАДАЧУ"):
            ''' make file for db '''
            with open("data/4.txt", "w") as fd:
                for i in range(len(self.data_fil_name_up)):
                    vr_s = '_'.join(self.name_of_up_fil_task.get().split())
                    print(f"{self.data_fil_name_up[i]} {vr_pr[i]} "\
                            f"{os.path.getsize(self.data_fil_name_up[i])} True up_{vr_s} andrew", file=fd)
            ''' end '''
            

            ''' upload information about this request in db '''
            """
            run your database communication program 
            """
            ''' end '''


            for i in self.lbl_fil_name_up:
                i.grid_remove()
                i.destroy()

            for i in self.spn_pr_fil_up:
                i.grid_remove()
                i.destroy()

            self.name_of_up_fil_task.set('Введите название запроса')

            self.sum_of_fil_up = 0
            self.data_fil_name_up = []
            self.data_pr_fil_up = []
            self.lbl_fil_name_up = []
            self.pr_fil_up = []
            self.spn_pr_fil_up = []
            self.file_flag = True

            self.btnUpdatState.event_generate("<ButtonRelease>")

            self.restart_daemon()



    def UpdateTask(self):
        pass
        


root = tkinter.Tk()
root.geometry("1280x720")
app = Application(root)
root.mainloop()

