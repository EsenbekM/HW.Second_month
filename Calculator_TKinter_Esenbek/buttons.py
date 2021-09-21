from calc import *

make_digit_button("1").grid(row=1, column=0, sticky='wens', padx=3, pady=3)
make_digit_button("2").grid(row=1, column=1, sticky='wens', padx=3, pady=3)
make_digit_button("3").grid(row=1, column=2, sticky='wens', padx=3, pady=3)
make_digit_button("4").grid(row=2, column=0, sticky='wens', padx=3, pady=3)
make_digit_button("5").grid(row=2, column=1, sticky='wens', padx=3, pady=3)
make_digit_button("6").grid(row=2, column=2, sticky='wens', padx=3, pady=3)
make_digit_button("7").grid(row=3, column=0, sticky='wens', padx=3, pady=3)
make_digit_button("8").grid(row=3, column=1, sticky='wens', padx=3, pady=3)
make_digit_button("9").grid(row=3, column=2, sticky='wens', padx=3, pady=3)
make_digit_button("0").grid(row=4, column=0, sticky='wens', padx=3, pady=3)

make_operation_button("+").grid(row=2, column=4, sticky='wens', padx=3, pady=3)
make_operation_button("-").grid(row=2, column=3, sticky='wens', padx=3, pady=3)
make_operation_button("*").grid(row=3, column=3, sticky='wens', padx=3, pady=3)
make_operation_button("/").grid(row=4, column=3, sticky='wens', padx=3, pady=3)
make_operation_button("**2").grid(row=4, column=2, sticky='wens', padx=3, pady=3)
make_operation_button("**(1/2)").grid(row=4, column=1, sticky='wens', padx=3, pady=3)
make_operation_button("%").grid(row=3, column=4, sticky='wens', padx=3, pady=3)

make_calc_button("=").grid(row=4, column=4, sticky='wens', padx=3, pady=3)
make_clear_button("C").grid(row=1, column=3, sticky='wens', padx=3, pady=3)
delete_button("DEL").grid(row=1, column=4, sticky='wens', padx=3, pady=3)


win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)
win.grid_columnconfigure(4,minsize=60)


win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
