import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CannonSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Cannon Simulator')
        self.maxsize(width=350, height=300)
        self.minsize(width=350, height=300)
        self.geometry('300x350')

        self.weight = 0
        self.air_resistance = 0
        self.shot_angle = 0
        self.initial_speed = 0

        self.str_weight = tk.StringVar()
        self.str_air_resistance = tk.StringVar()
        self.str_shot_angle = tk.StringVar()
        self.str_initial_speed = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        self.weight_label = tk.Label(self, text='Weight:')
        self.weight_label.grid(row=0, column=0, padx=15, pady=15, sticky='W')
        self.weight_entry = tk.Entry(self, textvariable=self.str_weight)
        self.weight_entry.grid(row=0, column=1, padx=15, pady=15)
        self.weight_entry.bind('<Key-Return>', self.set_weight)

        self.air_resistance_label = tk.Label(self, text='Air resistance:')
        self.air_resistance_label.grid(row=1, column=0, padx=15, pady=15, sticky='W')
        self.air_resistance_entry = tk.Entry(self, textvariable=self.str_air_resistance)
        self.air_resistance_entry.grid(row=1, column=1, padx=15, pady=15)
        self.air_resistance_entry.bind('<Key-Return>', self.set_air_resistance)

        self.shot_angle_label = tk.Label(self, text='Shot angle:')
        self.shot_angle_label.grid(row=2, column=0, padx=15, pady=15, sticky='W')
        self.shot_angle_entry = tk.Entry(self, textvariable=self.str_shot_angle)
        self.shot_angle_entry.grid(row=2, column=1, padx=15, pady=15)
        self.shot_angle_entry.bind('<Key-Return>', self.set_shot_angle)

        self.initial_speed_label = tk.Label(self, text='Initial speed:')
        self.initial_speed_label.grid(row=3, column=0, padx=15, pady=15, sticky='W')
        self.initial_speed_entry = tk.Entry(self, textvariable=self.str_initial_speed)
        self.initial_speed_entry.grid(row=3, column=1, padx=15, pady=15)
        self.initial_speed_entry.bind('<Key-Return>', self.set_initial_speed)

        self.go_back_button = ttk.Button(self, text='Print plot', command=self.rysuj)
        self.go_back_button.grid(row=4, column=0, padx=15, pady=15)

    def set_weight(self, event):
        temp = self.str_weight.get()
        try:
            temp = int(temp)
        except:
            tk.messagebox.showinfo('Bad data input.', 'Give me numbers, not letters!')
        else:
            if self.temp_positive(temp):
                self.weight = temp
                tk.Label(self, text='{} kg'.format(self.weight), fg='green').grid(row=0, column=3, sticky='W')

    def set_air_resistance(self, event):
        temp = self.str_air_resistance.get()

        try:
            temp = int(temp)
        except:
            tk.messagebox.showinfo('Bad data input.', 'Give me numbers, not letters!')
        else:
            if self.temp_positive(temp):
                self.air_resistance = temp
                tk.Label(self, text='{} N'.format(self.air_resistance), fg='green').grid(row=1, column=3, sticky='W')

    def set_shot_angle(self, event):
        temp = self.str_shot_angle.get()
        try:
            temp = int(temp)
        except:
            tk.messagebox.showinfo('Bad data input.', 'Give me numbers, not letters!')
        else:
            if self.temp_positive(temp):
                self.shot_angle = temp
                tk.Label(self, text='{} °'.format(self.shot_angle), fg='green').grid(row=2, column=3)

    def set_initial_speed(self, event):
        temp = self.str_initial_speed.get()

        try:
            temp = int(temp)
        except:
            tk.messagebox.showinfo('Bad data input.', 'Give me numbers, not letters!')
        else:
            if self.temp_positive(temp):
                self.initial_speed = temp
                tk.Label(self, text='{} m/s'.format(self.initial_speed), fg='green').grid(row=3, column=3, sticky='W')

    def temp_positive(self, temp):
        if temp > 0:
            return True
        else:
            tk.messagebox.showinfo('Small error', 'Value must be positive !')
            return False

    def rysuj(self):
        #print_plot()
        pass


app = CannonSimulator()
app.mainloop()
