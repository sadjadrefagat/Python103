import json
from openpyxl import Workbook
import tkinter as tk
from tkinter import filedialog, messagebox


def read_data(filename):
    with open(file=filename, mode='r', encoding='utf-8') as fIn:
        data = json.load(fp=fIn)
    return [tuple(item.items()) for item in data]


def export_data(data, fields, filename):
    excel_workbook = Workbook()
    excel_sheet = excel_workbook.active
    excel_sheet.title = 'شماره مشتریان'
    excel_sheet.append(fields)
    for item in data:
        excel_sheet.append([(dict(item).get(field, '')) for field in fields])
    excel_workbook.save(filename=filename)


def main():
    def select_data_file():
        filename = filedialog.askopenfilename(
            title='فایل حاوی اطلاعات مشتریان را انتخاب کنید',
            filetypes=(
                ('JSON Files', '*.json'),
                ('All Files', '*.*')
            )
        )
        if filename:
            json_path.set(filename)
            data = read_data(filename=filename)
            populate_fields(data=data)

    def populate_fields(data):
        fields = set()
        for item in data:
            fields.update(dict(item).keys())
        fields_list.clear()
        fields_list.extend(fields)
        for chk in chk_frame.winfo_children():
            chk.destroy()
        for field in fields_list:
            boolVar = tk.BooleanVar()
            chkField = tk.Checkbutton(chk_frame, text=field, variable=boolVar)
            chkField.pack(anchor='e')
            fields_var[field] = boolVar

    def export_to_excel():
        fields = [field for field,
                  var in fields_var.items() if var.get()]
        if not fields:
            messagebox.showerror(
                title='خطا', message='.هیچ فیلدی انتخاب نشده است')
            return
        filename = filedialog.asksaveasfilename(
            title='فایل اکسل', defaultextension='.xlsx',
            filetypes=(
                ('Excel Files', '*.xlsx'),
                ('All Files', '*.*')
            )
        )
        if filename:
            data = read_data(filename=json_path.get())
            export_data(data=data, fields=fields, filename=filename)
            messagebox.showinfo(
                title='توجه', message=f'داده‌ها با موفقت به اکسل ارسال شدند:\n{filename}')

    root = tk.Tk()
    root.title('پروژه 3 - دانشجو: آیسان دهقان‌زاده')
    root.geometry('600x450')
    json_path = tk.StringVar()
    fields_list = []
    fields_var = {}

    lbl1 = tk.Label(root, text=':فایل داده')
    lbl1.pack(anchor='e', padx=10, pady=10)

    txtFile = tk.Entry(root, textvariable=json_path,
                       state='readonly', width=50)
    txtFile.pack(anchor='e', padx=10)

    btnImport = tk.Button(root, text='انتخاب فایل داده',
                          command=select_data_file)
    btnImport.pack(anchor='e', padx=10, pady=5)

    lbl2 = tk.Label(root, text=':فیلدها')
    lbl2.pack(anchor='e', padx=10, pady=5)

    chk_frame = tk.Frame(root)
    chk_frame.pack(anchor='e', padx=10, pady=5, fill='x')

    btnExport = tk.Button(root, text='ارسال به اکسل', command=export_to_excel)
    btnExport.pack(anchor='e', padx=10, pady=20)
    root.mainloop()


if __name__ == '__main__':
    main()
