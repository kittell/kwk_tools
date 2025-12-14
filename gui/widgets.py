import tkinter as tk
from tkinter import ttk

class LabelEntry(ttk.Frame):
    '''Combines Label and Entry in a single widget
    '''
    def __init__(self, parent, label_text, entry_var, orient='horizontal'):
        super().__init__(parent)  # Initialize superclass

        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self, textvariable=entry_var)

        if orient == 'vertical':
            rows = [0, 1]
            columns = [0, 0]
            row_weights = [1, 0]
            column_weights = [1, 1]
        else:
            rows = [0, 0]
            columns = [0, 1]
            row_weights = [1, 1]
            column_weights = [0, 1]
        
        i = 0
        self.label.grid(row=rows[i], column=columns[i], sticky='NESW')
        self.rowconfigure(rows[i], weight=row_weights[i])
        self.columnconfigure(columns[i], weight=column_weights[i])
        i += 1
        self.entry.grid(row=rows[i], column=columns[i], sticky='NESW')
        self.rowconfigure(rows[i], weight=row_weights[i])
        self.columnconfigure(columns[i], weight=column_weights[i])

        return

class LabelEntryButton(ttk.Frame):
    '''Combines Label, Entry, Button in a single widget
    '''
    def __init__(self, parent, label_text, entry_var, button_text, button_callback, orient='horizontal'):
        super().__init__(parent)  # Initialize superclass

        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self, textvariable=entry_var)
        self.button = ttk.Button(self, text=button_text, command=button_callback)

        rows = list()
        columns = list()
        if orient == 'vertical':
            rows = [0, 1, 2]
            columns = [0, 0, 0]
            row_weights = [1, 0, 1]
            column_weights = [1, 1, 1]
        else:
            rows = [0, 0, 0]
            columns = [0, 1, 2]
            row_weights = [1, 1, 1]
            column_weights = [0, 1, 0]
        
        for i in range(len(rows)):
            self.label.grid(row=rows[i], column=columns[i], sticky='NESW')
            self.rowconfigure(rows[i], weight=row_weights[i])
            self.columnconfigure(columns[i], weight=column_weights[i])

        return
    

class FrameScrollbar(ttk.Frame):
    '''Frame with Scrollbar on right edge
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky='NESW')
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='NES')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)   # Resize content area, not scrollbar
        self.columnconfigure(1, weight=0)
        
        self.frame_content = ttk.Frame(self.canvas)  # Frame to hold scrollable content
        self.frame_content.bind('<Configure>', self._update_canvas_size)

        self.canvas.create_window((0, 0), window=self.frame_content, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        return
    
    def _update_canvas_size(self, e=None):
        self.canvas['scrollregion'] = self.canvas.bbox('all')
        return

class LabelStack(ttk.Frame):
    '''Stacks a number of Label widgets in a Frame
    '''

    def __init__(self, parent, scrollbar=False):
        '''
        Args:
            parent: parent widget for frame
            scrollbar: bool, switch to add scrollbar to frame
        '''
        super().__init__(parent)
        self.scrollbar = scrollbar
        if scrollbar == True:
            self.frame = FrameScrollbar(self)
        else:
            self.frame = ttk.Frame(self)
        
        self.frame.grid(row=0, column=0, sticky='NESW')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.labels = dict()
        
        return
    
    def add_labels(self, labels, insert_at=None):
        '''Add a label to the frame. Defaults to bottom of list.

        Args:
            labels: dict:
                key: name of label for reference
                value: tk.StringVar() that holds label text
        '''
        # Different content frame depending if using FrameScrollbar or Frame
        if self.scrollbar == True:
            frame_content = self.frame.frame_content
        else:
            frame_content = self.frame

        # TODO: currently can just append to end; try to insert later
        if insert_at is None:
            # Append to end
            r_frame = -1
            c_frame = 0
            for k in labels:
                # Create label and add to frame (self)
                r_frame += 1
                self.labels[k] = ttk.Label(frame_content, textvariable=labels[k])
                self.labels[k].grid(row=r_frame, column=c_frame, sticky='NESW')
                frame_content.rowconfigure(r_frame, weight=1)
                frame_content.columnconfigure(c_frame, weight=1)

        return
    

class ListboxScrollbar(ttk.Frame):
    '''Combines a Listbox and Scrollbar in a single widget
    '''
    def __init__(self, parent, height, list_var, list_items, return_var):
        super().__init__(parent)  # Initialize superclass

        self.list_var = list_var
        self.return_var = return_var

        self.listbox = tk.Listbox(self, height=height, listvariable=self.list_var)
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.listbox.yview)

        # Add items to be included in Listbox list
        for item in list_items:
            self.listbox.insert(tk.END, item)

        self.listbox.grid(row=0, column=0, sticky='NSEW')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=0, column=1, sticky='NSW')
        self.columnconfigure(1, weight=0)

        self.listbox.bind('<<ListboxSelect>>', self._callback_listbox_select_value)

        return
    
    def _callback_listbox_select_value(self, event):
        w = event.widget
        i = self.listbox.curselection()[0]  # Index of selected item in list
        v = event.widget.get(i)

        self.return_var.set(v)

        return