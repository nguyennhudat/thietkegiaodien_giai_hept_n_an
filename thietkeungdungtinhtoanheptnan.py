import tkinter as tk
from tkinter import ttk
import numpy as np
from numpy.linalg import LinAlgError

def solve_linear_equation():
    num_equations_str = num_equations_entry.get()
    if num_equations_str:
        num_equations = int(num_equations_str)
        A = np.zeros((num_equations, num_equations))
        b = np.zeros(num_equations)

        for i in range(num_equations):
            for j in range(num_equations):
                A[i, j] = float(coeff_entries[i][j].get())
            b[i] = float(const_entries[i].get())

        try:
            X = np.linalg.solve(A, b)
            result_label.config(text=f"Nghiệm của hệ phương trình: {X}")
        except LinAlgError:
            result_label.config(text="Hệ phương trình không có nghiệm.")
    else:
        result_label.config(text="Vui lòng nhập số phương trình.")

def find_matrix_inverse():
    num_equations_str = num_equations_entry.get()
    if num_equations_str:
        num_equations = int(num_equations_str)
        A = np.zeros((num_equations, num_equations))

        for i in range(num_equations):
            for j in range(num_equations):
                A[i, j] = float(coeff_entries[i][j].get())

        try:
            A_inv = np.linalg.inv(A)
            result_label.config(text=f"Ma trận nghịch đảo của A:\n{A_inv}")
        except LinAlgError:
            result_label.config(text="Không thể tìm ma trận nghịch đảo của A.")
    else:
        result_label.config(text="Vui lòng nhập số phương trình.")

def find_matrix_rank():
    num_equations_str = num_equations_entry.get()
    if num_equations_str:
        num_equations = int(num_equations_str)
        A = np.zeros((num_equations, num_equations))

        for i in range(num_equations):
            for j in range(num_equations):
                A[i, j] = float(coeff_entries[i][j].get())

        rank_A = np.linalg.matrix_rank(A)
        result_label.config(text=f"Hạng của ma trận A: {rank_A}")
    else:
        result_label.config(text="Vui lòng nhập số phương trình.")

def update_ui():
    num_equations_str = num_equations_entry.get()
    if num_equations_str:
        num_equations = int(num_equations_str)
        for entry_row in coeff_entries:
            for entry in entry_row:
                entry.destroy()
        for entry in const_entries:
            entry.destroy()

        coeff_entries.clear()
        const_entries.clear()

        for i in range(num_equations):
            coeff_row = []
            for j in range(num_equations):
                coeff_label = ttk.Label(frame, text=f"A[{i + 1},{j + 1}]:")
                coeff_label.grid(row=i + 5, column=j * 2, padx=5, pady=5)
                coeff_entry = ttk.Entry(frame, width=10)
                coeff_entry.grid(row=i + 5, column=j * 2 + 1, padx=5, pady=5)
                coeff_row.append(coeff_entry)
            coeff_entries.append(coeff_row)

            const_label = ttk.Label(frame, text=f"b[{i + 1}]:")
            const_label.grid(row=i + 5, column=num_equations * 2, padx=5, pady=5)
            const_entry = ttk.Entry(frame, width=10)
            const_entry.grid(row=i + 5, column=num_equations * 2 + 1, padx=5, pady=5)
            const_entries.append(const_entry)

        result_label.config(text="Kết quả sẽ được hiển thị ở đây.")
        solve_button.grid(row=num_equations + 5, column=0, columnspan=num_equations * 2, padx=5, pady=5)
        inverse_button.grid(row=num_equations + 6, column=0, columnspan=num_equations * 2, padx=5, pady=5)
        rank_button.grid(row=num_equations + 7, column=0, columnspan=num_equations * 2, padx=5, pady=5)

root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")
root.geometry("800x800")  # Đặt kích thước cửa sổ gốc

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

num_equations_label = ttk.Label(frame, text="Số phương trình:")
num_equations_label.grid(row=0, column=0, padx=5, pady=5)

num_equations_entry = ttk.Entry(frame)
num_equations_entry.grid(row=0, column=1, padx=5, pady=5)

update_button = ttk.Button(frame, text="Cập nhật", command=update_ui)
update_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

coeff_entries = []
const_entries = []

solve_button = ttk.Button(frame, text="Giải", command=solve_linear_equation)
inverse_button = ttk.Button(frame, text="Tìm Ma trận Nghịch Đảo", command=find_matrix_inverse)
rank_button = ttk.Button(frame, text="Tìm Hạng Ma trận A", command=find_matrix_rank)

for i in range(2):
    ttk.Label(frame, text="").grid(row=4 + i, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(frame, text="Kết quả sẽ được hiển thị ở đây.")
result_label.grid(row=10, column=10, columnspan=2, padx=5, pady=5)

root.mainloop()

#
import numpy as np
from numpy.linalg import LinAlgError

def solve_linear_equation(num_equations, coefficients, constants):
    A = np.array(coefficients)
    b = np.array(constants)

    try:
        X = np.linalg.solve(A, b)
        return f"Nghiệm của hệ phương trình: {X}"
    except LinAlgError:
        return "Hệ phương trình không có nghiệm."

def find_matrix_inverse(coefficients):
    A = np.array(coefficients)

    try:
        A_inv = np.linalg.inv(A)
        return f"Ma trận nghịch đảo của A:\n{A_inv}"
    except LinAlgError:
        return "Không thể tìm ma trận nghịch đảo của A."

def find_matrix_rank(coefficients):
    A = np.array(coefficients)
    rank_A = np.linalg.matrix_rank(A)
    return f"Hạng của ma trận A: {rank_A}"

# Example usage:
num_equations = int(input("Nhập số phương trình: "))

coefficients = []
constants = []

for i in range(num_equations):
    row = []
    for j in range(num_equations):
        coeff = float(input(f"Nhập A[{i + 1},{j + 1}]: "))
        row.append(coeff)
    coefficients.append(row)

    constant = float(input(f"Nhập b[{i + 1}]: "))
    constants.append(constant)

result_solve = solve_linear_equation(num_equations, coefficients, constants)
print(result_solve)

result_inverse = find_matrix_inverse(coefficients)
print(result_inverse)

result_rank = find_matrix_rank(coefficients)
print(result_rank)
