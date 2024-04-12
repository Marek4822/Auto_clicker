import ttkbootstrap as ttk

class App():
    def __init__(self) -> None:
        super().__init__
        self = ttk.Window(
            title='Auto clicker',
            size=(400, 600),
            themename='darkly',
        )
        self.auto_clikcer = Auto_clicker(self)
        self.mainloop()

class Auto_clicker(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(10, 10))
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.widgets()
    
    def widgets(self):
        self.columnconfigure((0, 1), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.tab_interval()
        self.tab_position()
        self.tab_click_option()
        self.tab_click_repeat()
        bttn_start = ttk.Button(self, text='Start', bootstyle='success')
        bttn_stop = ttk.Button(self, text='Stop', bootstyle='danger')

        bttn_start.grid(row=3, column=0, sticky='we')
        bttn_stop.grid(row=3, column=1, sticky='we')


    def tab_interval(self):
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

        self.notebook = ttk.Notebook(self, bootstyle="info")
        self.notebook.grid(row=0, column=0, sticky='wesn', columnspan=2)

        tab_interval = ttk.Frame(self.notebook)
        self.notebook.add(tab_interval, text='Click Interval')

        entry_milli = ttk.Entry(tab_interval, ) # entry
        entry_sec = ttk.Entry(tab_interval, ) # entry
        entry_min = ttk.Entry(tab_interval, ) # entry
        entry_hr = ttk.Entry(tab_interval, ) # entry


        label_milli = ttk.Label(tab_interval, text='Millis') # label
        label_sec = ttk.Label(tab_interval, text='Sec') # label
        label_min = ttk.Label(tab_interval, text='Min') # label
        label_hr = ttk.Label(tab_interval, text='Hr') # label


        entry_milli.grid(row=0, column=0, sticky='', padx=10, pady=10) # grid entry
        entry_sec.grid(row=0, column=1, sticky='', padx=10, pady=10) # grid entry
        entry_min.grid(row=0, column=2, sticky='', padx=10, pady=10) # grid entry
        entry_hr.grid(row=0, column=3, sticky='', padx=10, pady=10) # grid entry


        label_milli.grid(row=1, column=0, sticky='', padx=10, pady=10) # grid label
        label_sec.grid(row=1, column=1, sticky='', padx=10, pady=10) # grid label
        label_min.grid(row=1, column=2, sticky='', padx=10, pady=10) # grid label
        label_hr.grid(row=1, column=3, sticky='', padx=10, pady=10) # grid label


    def tab_position(self):
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a', )

        self.notebook = ttk.Notebook(self, bootstyle="info")
        self.notebook.grid(row=1, column=0, sticky='wesn', columnspan=2)

        tab_position = ttk.Frame(self.notebook)
        self.notebook.add(tab_position, text='Cursor Position')


        self.checkbox_current_var = ttk.IntVar()

        self.checkbox_current = ttk.Checkbutton(tab_position, text='Current Location',
                                                bootstyle="success-round-toggle",
                                                state='selected',
                                                variable=self.checkbox_current_var, 
                                                onvalue=True, offvalue=False, 
                                                command=self.checker_position) # checkbox

        self.checkbox_current.grid(row=0, column=0, sticky='w', padx=10, pady=10) # grid checkbox

    def checker_position(self):
        if self.checkbox_current_var.get():
            self.is_checked_position = True
            print(f'Current Location {self.is_checked_position} ')
        else:
            self.is_checked_position = False
            print(f'Current Location {self.is_checked_position}')


    def tab_click_option(self):
        self.columnconfigure((0, 1,), weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

        self.notebook = ttk.Notebook(self, bootstyle="info")
        self.notebook.grid(row=2, column=0, sticky='wesn',)

        tab_click_option = ttk.Frame(self.notebook)
        self.notebook.add(tab_click_option, text='Click Options')

        mouse_bttn = ttk.Label(tab_click_option, text='Mouse Button')
        click_type = ttk.Label(tab_click_option, text='Click Type')
        self.mouse_bttn_menu = ttk.Menubutton(tab_click_option, text='option 1a')
        self.click_type_menu = ttk.Menubutton(tab_click_option, text='option 1b')


        mouse_bttn_inmenu = ttk.Menu(tab_click_option)
        option_mouse_var = ttk.StringVar()
        for option_mouse in ['option 1a', 'option 2a', 'option 3a']:
            mouse_bttn_inmenu.add_radiobutton(label=option_mouse, variable=option_mouse_var, value=option_mouse, 
                                              command=lambda option_mouse = option_mouse: self.change_mouse(option_mouse))
        self.mouse_bttn_menu['menu'] = mouse_bttn_inmenu

        click_type_inmenu = ttk.Menu(tab_click_option)
        option_click_var = ttk.StringVar()
        for option_click in ['option 1b', 'option 2b', 'option 3b']:
            click_type_inmenu.add_radiobutton(label=option_click, variable=option_click_var, value=option_click, 
                                              command=lambda option_click = option_click: self.change_click(option_click))
            self.click_type_menu['menu'] = click_type_inmenu


        mouse_bttn.grid(row=0, column=0, sticky='', padx=10, pady=10)
        click_type.grid(row=1, column=0, sticky='', padx=10, pady=10)
        self.mouse_bttn_menu.grid(row=0, column=1, sticky='', padx=10, pady=10)
        self.click_type_menu.grid(row=1, column=1, sticky='', padx=10, pady=10)


    def change_mouse(self, option_mouse):
        self.mouse_bttn_menu.config(text=option_mouse)
        print(f'You selected: {option_mouse}!')

    def change_click(self, option_click):
        self.click_type_menu.config(text=option_click)
        print(f'You selected: {option_click}!')


    def tab_click_repeat(self):
        self.columnconfigure((0, 1,), weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

        self.notebook = ttk.Notebook(self, bootstyle="info")
        self.notebook.grid(row=2, column=1, sticky='wesn',)

        tab_click_repeat = ttk.Frame(self.notebook)
        self.notebook.add(tab_click_repeat, text='Click Repeat')

        self.checkbox_repeat_var = ttk.IntVar()
        self.checkbox_repeat = ttk.Checkbutton(tab_click_repeat, text='Infinite',
                                                bootstyle="success-round-toggle",
                                                state='selected',
                                                variable=self.checkbox_repeat_var, 
                                                onvalue=True, offvalue=False, 
                                                command=self.checker_repeat) # checkbox
        
        label_repetition = ttk.Label(tab_click_repeat, text='Repetition')
        entry_repetition = ttk.Entry(tab_click_repeat, width=10)

        self.checkbox_repeat.grid(row=0, column=0, sticky='w', padx=10, pady=10) # grid checkbox
        label_repetition.grid(row=1, column=0,  padx=10, pady=10)
        entry_repetition.grid(row=1, column=1,  padx=10, pady=10)

    def checker_repeat(self):
        if self.checkbox_repeat_var.get():
            self.is_checked_repeat = True
            print(f'Click repeat infinite: {self.is_checked_repeat} ')
        else:
            self.is_checked_repeat = False
            print(f'Click repeat infinite: {self.is_checked_repeat}')

App()

# Todo: 
# 1. fix ui
# 2. change to ttkbootstrap Radiobutton
# 3. add logic