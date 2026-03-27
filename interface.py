import customtkinter as ctk
from reader import read_logs_warnings, read_logs_ok
from writter import write_logs


if __name__ == "__main__":
    ctk.set_appearance_mode("light")

    app = ctk.CTk()
    app.title("Sys")
    app.geometry("700x600")
    app.resizable(True,True)

    logs_box = ctk.CTkTextbox(app, width=350, height=200,text_color="green")
    logs_box.pack(pady=10)

    warnings_box = ctk.CTkTextbox(app, width=350, height=200,text_color="red")
    warnings_box.pack(pady=10)

    show_quantities_logs = 5
    show_quantities_warnings = 5

    def show_5_logs():
        global show_quantities_logs

        content = read_logs_ok(show_quantities_logs)

        logs_box.delete("0.0", "end")
        logs_box.insert("0.0", content)
        show_quantities_logs += 5

    def show_5_warnings():
        global show_quantities_warnings

        content = read_logs_warnings(show_quantities_warnings)

        warnings_box.delete("0.0", "end")
        warnings_box.insert("0.0", content)
        show_quantities_warnings += 5

    def write_2_logs():
        logs_box.delete("0.0", "end")
        warnings_box.delete("0.0", "end")
        write_logs(2,5)
        logs_box.insert("0.0", "Logs written successfully")
        warnings_box.insert("0.0", "Logs written successfully")

    def switch_event():
        if switch_var.get() == "on":
            btn_create_logs.pack_forget()
            btn_show_logs.pack(pady=10)
            btn_show_warnings.pack(pady=10)

        else:
            btn_show_logs.pack_forget()
            btn_show_warnings.pack_forget()
            btn_create_logs.pack(pady=10)



    switch_var = ctk.StringVar(value="on")
    switch = ctk.CTkSwitch(app, text="Read/Write", command=switch_event,
                                     variable=switch_var, onvalue="on", offvalue="off")

    switch.pack(pady=10)

    btn_show_logs = ctk.CTkButton(app,text="Show 5 logs",command=show_5_logs)
    btn_show_warnings = ctk.CTkButton(app, text="Show 5 warnings",command=show_5_warnings)
    btn_create_logs = ctk.CTkButton(app, text="Write 2 logs in 5 seconds", command=write_2_logs)

    btn_show_logs.pack(pady=10)
    btn_show_warnings.pack(pady=10)
    btn_create_logs.pack(pady=10)

    app.mainloop()