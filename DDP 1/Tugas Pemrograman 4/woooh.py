import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
import pygame as pg
import sys

class PopUpWindow(object):

    def __init__(self, master):
        self.top=top=tk.Toplevel(master)
        top.title("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.info1 = tk.Label(top, text="Please set a time")
        self.info1.grid(row=0, column=0, columnspan=4, sticky=tk.N)

        #Entries
        self.entryhour = tk.Entry(top, width=4)
        self.spacer1 = tk.Label(top, text=":")
        self.entryminute = tk.Entry(top, width=4)
        self.spacer2 = tk.Label(top, text=":")
        self.entrysecond = tk.Entry(top, width=4)
        self.confbutton = tk.Button(top, text="Confirm", command=self.confirm)

        #Assign to grid
        self.entryhour.grid(row=1, column=0)
        self.spacer1.grid(row=1, column=1)
        self.entryminute.grid(row=1, column=2)
        self.spacer2.grid(row=1, column=3)
        self.entrysecond.grid(row=1, column=4)
        self.confbutton.grid(row=2, column=1, columnspan=3)
    
    def confirm(self):
        global hour, minute, second
        hour = str(self.entryhour.get())
        minute = str(self.entryminute.get())
        second = str(self.entrysecond.get())
        
        #if the user uses single digit instead of double digit
        if len(hour) == 1:
            hour = '0' + hour
        if len(minute) == 1:
            minute = '0' + minute
        if len(second) == 1:
            second = '0' + second

        # self.top.protocol("WM_DELETE_WINDOW", MainWindow.reset)   
        self.top.destroy()

        
class MainWindow(object):


    def __init__(self, master):
        self.master = master
        self.master.title("Timer and Alarm")

        self.frametime = tk.Frame(master)
        self.framebuttons = tk.Frame(master)
        self.frametime.grid(row=0)
        self.framebuttons.grid(row=1)

        '''Conditions'''
        self.alarm_is_set = 0
        self.music_is_set = 0
        self.music_is_playing = 0
        self.curr_vol = 1

        '''label in frametime'''
        self.clock = tk.Label(self.frametime, font=("Helvetica", 28, "bold"),
                         width = 16, height=2)
        self.tick()
        self.clock.grid(row=0, column=1, columnspan=3)

        '''Volume slider'''
        self.vol = tk.Scale(self.frametime, from_=100, to=10, resolution=10)
        self.vol.set(100)
        self.vol.grid(row=0, column=0, rowspan=2)
        self.vol.bind('<ButtonRelease-1>', self.setvol)

        '''buttons in framebutton'''
        self.buttonreset = tk.Button(self.framebuttons, text='Reset', width=15, command=self.reset)
        self.buttonstop = tk.Button(self.framebuttons, text='Stop', width=15, command=self.stop)
        self.buttonsettimer = tk.Button(self.framebuttons, text='Set Alarm', width=15,
                         command=self.popup)
        self.buttonsong = tk.Button(self.framebuttons, text='Select Music',
                         width=15, command=self.music)

        self.buttonreset.grid(row=1, column=0, padx=2)
        self.buttonstop.grid(row=1, column=1, padx=2)
        self.buttonsettimer.grid(row=1, column=2, padx=2)
        self.buttonsong.grid(row=1, column=3, padx=2)

    '''pop-up to set alarm'''
    def popup(self):
        self.window = PopUpWindow(self.master)
        self.buttonsettimer["state"] = "disabled" 
        self.master.wait_window(self.window.top)
        try:
            if 0 <= int(hour) <= 24 and 0 <= int(minute) <= 60 and 0 <= int(second) <= 60:
                    self.alarm_is_set = 1
                    global alarmhms
                    alarmhms = hour+":"+minute+":"+second            
        except ValueError:
            self.buttonsettimer["state"] = "normal"
            messagebox.showerror("Error : Input", "Please input digits (0-9)")
        except NameError:
            self.buttonsettimer["state"] = "normal"

        if self.alarm_is_set == 1 :                     #SoTheUserWillInputTheCorrectNumberFirst
            if self.music_is_set == 0:
                self.music()
            if self.music_is_set == 1:
                self.addalarmui()
        self.buttonsettimer["state"] = "normal"         #MakeTheButton"Press-able"

    '''displays the user's alarm in the main GUI'''     
    def addalarmui(self):
        self.labelalarm = tk.Label(self.frametime, text="Alarm set at {}:{}:{}".format(hour,minute,second),
                             font=("Helvetica", 10))
        self.clock.grid_configure(row=1,column=1,columnspan=3)
        self.labelalarm.grid(row=0, column=1, columnspan=3)

    '''checks if the time is same as the alarm'''
    def tick(self):
        timestr = time.strftime("%H:%M:%S")
        self.clock.config(text=timestr)
        self.clock.after(200,self.tick)
        if self.alarm_is_set == 1:
            if timestr == alarmhms:
                self.music_is_playing = 1
                pg.mixer.music.play(-1)
    
    '''prompts the user to select song for alarm'''
    def music(self):
        # set up the mixer (reference from the internet)
        freq = 44100                        # audio CD quality
        bitsize = -16                       # unsigned 16 bit
        channels = 2                        # stereo
        buffer = 2048                       # number of samples (experiment to get best sound)
        pg.mixer.init(freq, bitsize, channels, buffer)

        file_name = filedialog.askopenfilename()
        if not file_name:                                   # Jika pengguna membatalkan dialog, langsung return.
            return None
        pg.mixer.music.load(file_name)
        self.music_is_set = 1
    
    '''STOP DA MUSEEECCC'''
    def stop(self):
        if self.music_is_playing == 1:
            self.music_is_playing == 0
            pg.mixer.music.stop()        
    
    '''set volume'''
    def setvol(self,event):
        self.curr_vol = self.vol.get()
        pg.mixer.music.set_volume(self.curr_vol/100)

    def reset(self):
        self.buttonsettimer["state"] = "normal" 
        if self.alarm_is_set == 1:
            self.labelalarm.grid_remove()
            self.clock.grid_configure(row=0,column=1,columnspan=3)
            alarmhms = ''
            hour = ''
            minute = ''
            second = ''
            self.alarm_is_set = 0
        elif self.alarm_is_set == 0:
            self.labelalarm.grid_remove()
            self.clock.grid_configure(row=0,column=1,columnspan=3)
            alarmhms = ''
            hour = ''
            minute = ''
            second = ''
        else:
            pass



def main():
    root = tk.Tk()
    userinterface = MainWindow(root)
    root.mainloop()

if __name__=='__main__':
    main()
