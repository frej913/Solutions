"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("250x200")  # 125x200 men det gør at man ikke kan se andet end minimer-, full-screen- eller luk-vindue knapperne

padx_input_sets = 4
pady_input_sets = 4
# container
frame_label = tk.LabelFrame(main_window, text="Container")
frame_label.grid(row=0, column=0, padx=5, pady=5)
inside_frame = tk.Frame(frame_label)  # currently useless, but also good to play around
inside_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NS)
# label
label1 = tk.Label(inside_frame, text="Id", width=30, justify=tk.CENTER)  # the width is weird but what can you do
label1.grid(row=0, column=0, padx=padx_input_sets, pady=pady_input_sets)
# input -ish
entry1 = tk.Entry(inside_frame, width=5, justify=tk.CENTER)  # .        PADDING FOR ALL
entry1.grid(row=1, column=0, padx=padx_input_sets, pady=pady_input_sets)
# button
btn_create = tk.Button(inside_frame, text="Create", justify=tk.CENTER)
btn_create.grid(row=2, column=0, padx=10, pady=10)
# run program
if __name__ == "__main__":
    main_window.mainloop()
