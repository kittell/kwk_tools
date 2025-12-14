import tkinter as tk
from tkinter import ttk

from kwk_tools.gui.widgets import *

class Application:
    '''Main class to run application
    '''
    def __init__(self):
        gui = GUI(self)
        return
    
class GUI(tk.Tk):
    '''Handles GUI functions that interface with underlying app functions
    '''
    def __init__(self, app):
        super().__init__()

        # Basic GUI objects
        self.app = app
        self.notebook = ttk.Notebook(self)
        self.tabs = dict()
        self.var = dict()

        # Display basic items
        self.title('APP TITLE')
        self.geometry('800x600')
        self.notebook.grid(row=0, column=0, sticky='NESW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.notebook.columnconfigure(0, weight=1)
        self.notebook.rowconfigure(0, weight=1)

        # TAB START: TAB_1
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'TAB_1'
        self.tabs[tab_name] = ttk.Frame(self.notebook)
        this_tab = self.tabs[tab_name]
        self.notebook.add(this_tab, text=tab_name)
        # Note: Do not add tab to .grid()
        
        # T1 FRAME START: FRAME_1
        r_grid_0 += 1; c_grid_0 += 1
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_FRAMENAME = ttk.LabelFrame(this_tab, text='frame_1')
        this_frame_1 = self.frame_FRAMENAME    # tier 1 frame
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        this_tab.columnconfigure(c_grid_0, weight=1)
        

        self.var['var_1'] = tk.StringVar(value='')
        r_grid_1 += 1; c_grid_1 += 1
        self.labelentrybutton_1 = LabelEntryButton(
            parent=this_frame_1,
            label_text = 'label_text',
            entry_var = self.var['var_1'],
            button_text = 'button_text',
            button_callback = self._callback_labelentrybutton_BUTTONNAME,
            orient='horizontal'
        )
        this_frame_2 = self.labelentrybutton_1  # tier 2 frame
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T1 FRAME END: FRAME_1

        # T1 FRAME START: FRAME_2
        self.var['var_2'] = tk.StringVar(value=list())  # List of items for listbox
        self.var['var_3'] = tk.StringVar(value='')      # Selected item in listbox
        r_grid_0 += 1; c_grid_0 += 0
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_2 = ttk.LabelFrame(this_tab, text='frame_2')
        this_frame_1 = self.frame_2
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        this_tab.columnconfigure(c_grid_0, weight=1)

        # Replace with items to add to list
        list_items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        r_grid_1 += 1; c_grid_1 += 1
        self.listbox = ListboxScrollbar(
            parent=this_frame_1,
            height=5,
            list_var=self.var['var_2'],
            list_items=list_items,
            return_var=self.var['var_3']
        )
        this_frame_2 = self.listbox  # tier 2 frame
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T2 FRAME END: FRAME_2
        
        # TAB END: TAB_1


        # Go
        self.mainloop()
        return
    
    def _callback_labelentrybutton_BUTTONNAME(self):
        return
    
    def _update_vars(self):
        return
    
app = Application()
