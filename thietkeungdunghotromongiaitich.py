import sympy as sym
import tkinter as tk
from tkinter import Label, Entry, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def calculate_limit():
    expression = input_expression.get()
    limit_x = float(input_limit.get())  # Lấy giá trị x cho giới hạn
    x = sym.symbols('x')
    f = sym.sympify(expression)

    limit = sym.limit(f, x, limit_x)  # Tính giới hạn tại giá trị limit_x

    result_label.config(text=f"Giới hạn tại x = {limit_x}: {limit}")

def plot_and_calculate():
    expression = input_expression.get()
    x = sym.symbols('x')
    f = sym.sympify(expression)

    x_vals = np.linspace(-10, 10, 400)
    f_lambda = sym.lambdify(x, f, "numpy")
    y_vals = f_lambda(x_vals)

    integral = sym.integrate(f, x)
    derivative = sym.diff(f, x)

    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.title('Đồ thị hàm số f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    result_label.config(text=f"Tích phân của f(x): {integral}\nĐạo hàm của f(x): {derivative}")

# Create the main window
window = tk.Tk()
window.title("Symbolic Computation Tool")

# Create input field for expression
expression_label = Label(window, text="Nhập biểu thức hàm f(x):")
expression_label.pack()

input_expression = Entry(window)
input_expression.pack()

# Create input field for limit
limit_label = Label(window, text="Nhập giá trị x cho giới hạn:")
limit_label.pack()

input_limit = Entry(window)
input_limit.pack()

# Create buttons to calculate limit and plot
calculate_limit_button = Button(window, text="Tính giới hạn", command=calculate_limit)
calculate_limit_button.pack()

calculate_and_plot_button = Button(window, text="Tích phân, Đạo hàm và Vẽ", command=plot_and_calculate)
calculate_and_plot_button.pack()

# Create a label to display results
result_label = Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop()

#
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def calculate_limit(expression, limit_x):
    x = sym.symbols('x')
    f = sym.sympify(expression)
    limit = sym.limit(f, x, limit_x)
    return limit

def plot_and_calculate(expression):
    x = sym.symbols('x')
    f = sym.sympify(expression)

    x_vals = np.linspace(-10, 10, 400)
    f_lambda = sym.lambdify(x, f, "numpy")
    y_vals = f_lambda(x_vals)

    integral = sym.integrate(f, x)
    derivative = sym.diff(f, x)

    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.title('Đồ thị hàm số f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

    print(f"Tích phân của f(x): {integral}")
    print(f"Đạo hàm của f(x): {derivative}")

# Example usage:
expression = input("Nhập biểu thức hàm f(x): ")
limit_x = float(input("Nhập giá trị x cho giới hạn: "))

limit_result = calculate_limit(expression, limit_x)
print(f"Giới hạn tại x = {limit_x}: {limit_result}")

plot_and_calculate(expression)
