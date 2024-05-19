import json
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x600")
root.title("CHATBOT")

file_path = "intents.json"
with open(file_path, "r") as file:
    intents = json.load(file)

for i in range(100):
    root.grid_rowconfigure(i, weight=1)
for j in range(100):
    root.grid_columnconfigure(j, weight=1)

import random

def send_message(event=None):
    message = entry1.get()
    
    bot_response = ""
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in message.lower():
                bot_response = random.choice(intent["responses"])
                break  
    
    if bot_response:
        user_label = customtkinter.CTkLabel(frame2, text="USER: " + message, font=("Helvetica", 21), bg_color="#191919", text_color="white")
        user_label.grid(sticky="w", padx=(10, 0), pady=10)  
        bot_label = customtkinter.CTkLabel(frame2, text="BOT: " + bot_response, font=("Helvetica", 21), bg_color="#191919", text_color="white", anchor="e")
        bot_label.grid(sticky="w", padx=(10, 0), pady=10)

    else:
        bot_response = "Sorry, I didn't understand that."
        user_label = customtkinter.CTkLabel(frame2, text="USER: " + message, font=("Helvetica", 21), bg_color="#191919", text_color="white")
        user_label.grid(sticky="w", padx=(10, 0), pady=10)
        bot_label = customtkinter.CTkLabel(frame2, text="BOT: " + bot_response, font=("Helvetica", 21), bg_color="#191919", text_color="white", anchor="e")
        bot_label.grid(sticky="w", padx=(10, 0), pady=10)
    
    entry1.delete(0, "end") 


def start():
    button1.destroy()
    label1.destroy()

    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew",rowspan=70,columnspan=100)
    frame2.grid(row=1000, column=0, padx=0, pady=25, sticky="nsew")
    
    entry1.grid(row=70, column=0, padx=0, pady=0, sticky="ew")
    button2.grid(row=70, column=1, padx=0, pady=0, sticky="ew") 
    
    label2.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    

frame1 = customtkinter.CTkScrollableFrame(root, height=500, width=1000, fg_color="#191919")
frame2 = customtkinter.CTkFrame(frame1, height=1000, width=1500, fg_color="#191919")
label1 = customtkinter.CTkLabel(root, text="WELCOME TO NEXTALK-AI", font=("Helvetica", 25))
button1 = customtkinter.CTkButton(root, text="PRESS TO START", height=50, width=140, font=("Helvetica", 12), text_color="black", fg_color="white", hover_color="grey", corner_radius=50, border_width=2,command=start)
entry1 = customtkinter.CTkEntry(root, placeholder_text="Write something to start the chat", height=50, width=1350, font=("Helvetica", 25), text_color="white", corner_radius=50)
button2 = customtkinter.CTkButton(root, text="SEND", height=50, width=100, font=("Helvetica", 25), text_color="black", fg_color="dark grey", hover_color="grey", border_width=2, command=send_message,corner_radius=50)
label2 = customtkinter.CTkLabel(root, text="NEXTALK-AI", font=("Roboto", 25))



root.grid_rowconfigure(0, weight=1)  
root.grid_columnconfigure(0, weight=1)  

label1.grid(row=50, column=50, padx=0, pady=10)
button1.grid(row=60,column=50)

entry1.bind("<Return>", send_message)
root.mainloop()