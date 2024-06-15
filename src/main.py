import customtkinter as ctk
from tasks.notepad_task import open_notepad_and_write
from tasks.search_task import search
from tasks.ping_test_task import ping_test
import threading

class TaskApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("VidLex")
        self.geometry("600x400")

        ctk.set_appearance_mode("system") 
        ctk.set_default_color_theme("green")  

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.main_label = ctk.CTkLabel(self.main_frame, text="Welcome to VidLex", font=ctk.CTkFont(size=30))
        self.main_label.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.notepad_button = ctk.CTkButton(self.button_frame, text="Notepad", command=open_notepad_and_write)
        self.notepad_button.grid(row=0, column=0, padx=10)

        self.google_button = ctk.CTkButton(self.button_frame, text="Google Search", command=search)
        self.google_button.grid(row=0, column=1, padx=10)

        self.ping_button = ctk.CTkButton(self.button_frame, text="Ping Test", command=ping_test)
        self.ping_button.grid(row=0, column=2, padx=10)

        self.all_tasks_button = ctk.CTkButton(self.main_frame, text="Run All Tasks", command=self.run_all_tasks)
        self.all_tasks_button.pack(pady=10)

        self.footer_label = ctk.CTkLabel(self, text="Powered by VidLex", font=ctk.CTkFont(size=12))
        self.footer_label.pack(side="bottom", pady=10)

    def run_all_tasks(self):
        threading.Thread(target=open_notepad_and_write).start()
        threading.Thread(target=search).start()
        threading.Thread(target=ping_test).start()

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()
