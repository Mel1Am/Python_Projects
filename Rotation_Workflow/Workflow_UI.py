import tkinter as tk

# default answers
default_answers = [
    "This is a default answer 1 template. Customize as necessary.",
    "This is a default answer 2 template. Customize as necessary.",
    "This is a default answer 3 template. Customize as necessary."
]

# dialog prompts
dialog_prompts = [
    "24 hours have past since the post was made?",
    "Has a resolution been provided?",
    "Have you replied to the post?",
    "Is a reply required for the post owner?"
]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.step = 0  # Move this line before create_widgets() call
        self.pack()
        self.create_widgets()
        
    # the rest of the class

    def create_widgets(self):
        self.label = tk.Label(self, text=dialog_prompts[self.step])
        self.label.pack(side="top")
        self.entry = tk.Entry(self)
        self.entry.pack(side="top")
        self.ok_button = tk.Button(self)
        self.ok_button["text"] = "OK"
        self.ok_button["command"] = self.next_step
        self.ok_button.pack(side="top")

    def next_step(self):
        response = self.entry.get()
        if self.step == len(dialog_prompts):  # Add this check
            self.label["text"] = "End of Process. Close the application or start over."
            self.entry.delete(0, 'end')
            return

    # The rest of your next_step() function

        if self.step == 0:
            if response == "Yes":
                self.step = 1
            else:
                self.label["text"] = "Wait for at least 24 hrs before reaching out with a response."
                return
        elif self.step == 1:
            if response == "Yes":
                self.label["text"] = default_answers[0]
                self.step = 2
            else:
                self.step = 3
        elif self.step == 2:
            if response == "Yes":
                self.step = 4
            else:
                self.label["text"] = "Research for any possible solution you might find."
                return
        elif self.step == 3:
            if response == "Yes":
                self.label["text"] = default_answers[1]
                self.step = 2
            else:
                self.label["text"] = default_answers[2]
                return
        elif self.step == 4:
            if response == "Yes":
                self.label["text"] = "Reply with best solution found."
            else:
                self.label["text"] = "Document the Problem/Solution in the Wiki Spreadsheet. Update Issue Tracker spreadsheet."
                return
        self.label["text"] = dialog_prompts[self.step]
        self.entry.delete(0, 'end')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
