from tkinter import *
from tkinter import messagebox as mb
import matplotlib.pyplot as plt

rt = Tk()
rt.title("Sheet Graph Maker")
rt.geometry("600x600")
DARK = "#595959"
rt.config(bg=DARK)


def text_size(size):
    return ("Arial", size)

title = Label(rt, text="Sheet Graph Maker", font=text_size(40), bg=DARK)
title.place(relx=0.375, rely=0.1)

Label(rt, text="Enter graph type:", font=text_size(15), bg=DARK).place(relx=0.2, rely=0.25)

graph_type = Entry(rt, font=text_size(15))
graph_type.place(relx=0.2, rely=0.3)


Label(rt, text="Enter labels (Seperate with ','):", font=text_size(15), bg=DARK).place(relx=0.5, rely=0.25)

graph_labels = Entry(rt, font=text_size(15))
graph_labels.place(relx=0.5, rely=0.3)


Label(rt, text="Enter values (Seperate with ','):", font=text_size(15), bg=DARK).place(relx=0.2, rely=0.55)

graph_values = Entry(rt, font=text_size(15))
graph_values.place(relx=0.2, rely=0.6)


Label(rt, text="X and Y label (Seperate with ','):", font=text_size(15), bg=DARK).place(relx=0.7, rely=0.55)

xy_label = Entry(rt, font=text_size(15))
xy_label.place(relx=0.7, rely=0.6)


Label(rt, text="Enter graph title:", font=text_size(15), bg=DARK).place(relx=0.7, rely=0.25)

graph_title = Entry(rt, font=text_size(15))
graph_title.place(relx=0.7, rely=0.3)

def graph():

    try:
        try:
            x_y_label = list(map(lambda x: x.strip(),xy_label.get().split(",")))
        except:
            ...

        g_title = graph_title.get()
        typ = graph_type.get().strip().lower()
        values = list(map(lambda x: int(x), graph_values.get().split(",")))
        labels = list(map(lambda x: x.strip(), graph_labels.get().split(",")))

        plt.title(g_title)

        if typ == "graph":
            plt.plot(labels, values)
            plt.xlabel(x_y_label[0])
            plt.ylabel(x_y_label[1])
        elif typ == "bar":
            plt.bar(labels, values)
            plt.xlabel(x_y_label[0])
            plt.ylabel(x_y_label[1])
        elif typ == "pie":
            plt.pie(values, labels=labels, autopct="%1.1f%%", shadow=1)

        else:
            mb.showwarning("Invalid graph type", "This graph type is invalid; please check your input.")
            return
        


        plt.show()
    except:
        mb.showerror("Invalid input", "One of your input is invalid; please check your input.")

Button(rt, text="Graph", font=text_size(15), command=graph).place(relx=0.5, rely=0.6)

rt.mainloop()