import tkinter as tk
import math

def on_button_click(char):
    current_entry = entry.get()

    if char == 'C':
        entry.delete(0, tk.END)
    elif char == '±':
        try:
            if current_entry:
                number = float(current_entry)
                number *= -1
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(number))
        except ValueError:
            pass
    elif char == '%':
        try:
            result = eval(current_entry) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == '√':
        try:
            result = math.sqrt(float(current_entry))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == 'π':
        entry.insert(tk.END, str(math.pi))
    elif char == '=':
        try:
            expression = current_entry.replace('²', '**2').replace('÷', '/')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, char)

app = tk.Tk()
app.title("Advanced Calculator")
app.configure(bg='black')

entry_font = ('Arial', 24)
button_font = ('Arial', 18)

entry = tk.Entry(app, width=20, font=entry_font, bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

number_button_color = {'bg': '#2e2e2e', 'fg': 'white'}
top_button_color = {'bg': 'light gray', 'fg': 'black'}
right_side_button_color = {'bg': '#FF4500', 'fg': 'white'}

buttons = [
    ('C', 1, 0, top_button_color), ('±', 1, 1, top_button_color), ('%', 1, 2, top_button_color), ('÷', 1, 3, right_side_button_color),
    ('7', 2, 0, number_button_color), ('8', 2, 1, number_button_color), ('9', 2, 2, number_button_color), ('*', 2, 3, right_side_button_color),
    ('4', 3, 0, number_button_color), ('5', 3, 1, number_button_color), ('6', 3, 2, number_button_color), ('-', 3, 3, right_side_button_color),
    ('1', 4, 0, number_button_color), ('2', 4, 1, number_button_color), ('3', 4, 2, number_button_color), ('+', 4, 3, right_side_button_color),
    ('0', 5, 0, number_button_color), ('.', 5, 1, number_button_color), ('²', 5, 2, number_button_color), ('=', 5, 3, right_side_button_color),
    ('√', 6, 0, top_button_color), ('π', 6, 1, top_button_color)
]

for (text, row, col, color) in buttons:
    button = tk.Button(app, text=text, command=lambda char=text: on_button_click(char), bg=color['bg'], fg=color['fg'], font=button_font)
    button.grid(row=row, column=col, sticky="nsew")

for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(1, 7):
    app.grid_rowconfigure(i, weight=1)

app.geometry("300x450")

app.mainloop()
