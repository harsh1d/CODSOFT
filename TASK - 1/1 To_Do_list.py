"""A To-Do List application is a useful project that helps users manage
 and organize their tasks efficiently. This project aims to create a
 command-line or GUI-based application using Python, allowing
 users to create, update, and track their to-do lists
"""
import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        
        # Creating a frame to hold the widgets of our application
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.create_widgets()
        self.tasks = []
        self.load_tasks()
        self.update_listbox()
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.master.bind("<Return>", self.add_task)
        self.master.bind("<Delete>", self.delete_task)
        self.master.bind("<F5>", self.refresh_tasks)
        self.master.bind("<F6>", self.save_tasks)
        self.master.bind("<F7>", self.load_tasks)
        self.master.bind("<F8>", self.sort_tasks)
        self.master.bind("<F9>", self.toggle_completed)
        self.master.bind("<F10>", self.mark_as_done)
        self.master.bind("<F11>", self.mark_as_undone)
        self.master.bind("<F12>", self.edit_task)
        
    def create_widgets(self):
        # Creating a label widget
        self.label = tk.Label(self.frame, text="Enter a task:")
        self.label.grid(row=0, column=0)
        
        # Creating an entry widget
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=0, column=1)
        
        # Creating a button widget
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2)
        
        # Creating a listbox widget
        self.listbox = tk.Listbox(self.frame, height=10, width=50)
        self.listbox.grid(row=1, column=0, columnspan=3)
        
        # Creating a scrollbar widget
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.grid(row=1, column=3, sticky='ns')
        
        # Connecting the listbox to the scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self, event=None):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)
    
    def load_tasks(self, event=None):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = file.read().splitlines()
        except FileNotFoundError:
            self.tasks = []
    
    def save_tasks(self, event=None):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    
    def refresh_tasks(self, event=None):
        self.load_tasks()
        self.update_listbox()
    
    def sort_tasks(self, event=None):
        self.tasks.sort()
        self.update_listbox()
    
    def toggle_completed(self, event=None):
        pass
    
    def mark_as_done(self, event=None):
        pass
    
    def mark_as_undone(self, event=None):
        pass
    
    def edit_task(self, event=None):
        pass
    
    def on_close(self):
        self.save_tasks()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()