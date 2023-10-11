""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("493x179")

# my attempt at collecting variables in one place
padx = 8
pady = 4
btn_padx = 8
btn_pady = 6

# function(s)
def clear_all_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)


# container
frame_label = tk.LabelFrame(main_window, text="Container")
frame_label.grid(row=0, column=0, padx=5, pady=5)

# separate entries and buttons
inside_frame = tk.Frame(frame_label)
inside_frame.grid(row=0, column=0, padx=10, pady=8, sticky=tk.N)
btns_frame = tk.Frame(frame_label)
btns_frame.grid(row=1, column=0, padx=10, pady=8, sticky=tk.S)

# label-entry pairs
label1 = tk.Label(inside_frame, text="Id", justify=tk.CENTER)
label1.grid(row=0, column=0, padx=padx, pady=pady)
entry1 = tk.Entry(inside_frame, width=4, justify=tk.CENTER)
entry1.grid(row=1, column=0, padx=padx, pady=pady)

label2 = tk.Label(inside_frame, text="Weight", justify=tk.CENTER)
label2.grid(row=0, column=1, padx=padx, pady=pady)
entry2 = tk.Entry(inside_frame, width=8, justify=tk.CENTER)
entry2.grid(row=1, column=1, padx=padx, pady=pady)

label3 = tk.Label(inside_frame, text="Destination", justify=tk.CENTER)
label3.grid(row=0, column=2, padx=padx, pady=pady)
entry3 = tk.Entry(inside_frame, width=20, justify=tk.CENTER)
entry3.grid(row=1, column=2, padx=padx, pady=pady)

label4 = tk.Label(inside_frame, text="Weather", justify=tk.CENTER)
label4.grid(row=0, column=3, padx=padx, pady=pady)
entry4 = tk.Entry(inside_frame, width=14, justify=tk.CENTER)
entry4.grid(row=1, column=3, padx=padx, pady=pady)

# buttons
btn_create = tk.Button(btns_frame, text="Create", justify=tk.CENTER)
btn_create.grid(row=0, column=0, padx=btn_padx, pady=btn_pady)

btn_update = tk.Button(btns_frame, text="Update", justify=tk.CENTER)
btn_update.grid(row=0, column=1, padx=btn_padx, pady=btn_pady)

btn_delete = tk.Button(btns_frame, text="Delete", justify=tk.CENTER)
btn_delete.grid(row=0, column=2, padx=btn_padx, pady=btn_pady)

btn_clear = tk.Button(btns_frame, text="Clear Entry Boxes", justify=tk.CENTER, command=clear_all_entries)
btn_clear.grid(row=0, column=3, padx=btn_padx, pady=btn_pady)


# run program
if __name__ == "__main__":
    main_window.mainloop()
