from chat import bot_response, bot_name
from tkinter import *
from chat_styles import chatStyles




class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap("favicon.ico")
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window_configure()
        self.head_lable()
        self.tiny_divider()
        self.textwidget()
        self.scroll_bar()
        self.message_entry_box()

    def window_configure(self):
        self.window.title("Hanna is online")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=500, height=550, bg=chatStyles.BG_COLOR)

    def head_lable(self):
        head_lable = Label(self.window, bg=chatStyles.BG_COLOR, fg=chatStyles.TEXT_COLOR,
                                text="Welcome", font=chatStyles.FONT_BOLD, pady=chatStyles.PADY)
        head_lable.place(relwidth=1)

    def tiny_divider(self):
        line = Label(self.window, width=450, bg=chatStyles.BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

    def textwidget(self):
        self.text_widget = Text(self.window, width=20, height=2, bg=chatStyles.BG_COLOR,
                        fg=chatStyles.TEXT_COLOR , font=chatStyles.FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
    
    def scroll_bar(self):
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)



    def message_entry_box(self):
        bottom_label = Label(self.window, bg=chatStyles.BG_GRAY,
        height=80)
        bottom_label.place(relwidth=1, rely=0.82)
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=chatStyles.TEXT_COLOR, font=chatStyles.FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        send_button = Button(bottom_label, text="Send", font=chatStyles.FONT_BOLD,
                                width=20, bg=chatStyles.BT_COLOR,
                                command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)
        msg2 = f"{bot_name}: {bot_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    



if __name__ == "__main__":
    ChatApplication().run()