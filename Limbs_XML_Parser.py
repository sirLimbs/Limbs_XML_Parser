import xml.etree.ElementTree as ET
import urllib.request
import base64
from tkinter import filedialog
import tkinter as tk
from difflib import unified_diff
from io import StringIO

def parse_xml(file_path):
    # parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # find all string elements
    output_text.delete('1.0', tk.END) # Clear output text box
    output_text.insert(tk.END, f"\nParsing file:\n{file_path}\n\n")
    for imgdir in root.findall(".//imgdir[@name]"):
        imgdir_name = imgdir.attrib['name']
        values = []
        if imgdir_name in ["life"]:
            output_text.insert(tk.END, f"\r\n{imgdir_name}:\n")
            continue
        for string in imgdir.findall("./string[@name]"):
            string_name = string.attrib['name']
            if string_name in ["u", "pn", "tn", "script"]:
                continue
            string_value = string.attrib.get('value', '')
            if string_name == "oS":
                values.append(f"Map.wz/Obj/{string_value}")
            elif string_name == "bS":
                values.append(f"Map.wz/Back/{string_value}")
            elif string_name == "type":
                if string_value == "n":
                    values.append("Npc")
                elif string_value == "m":
                    values.append("Mob")
                elif string_value == "r":
                    values.append("Reactor")
            elif string_name == "id":
                values.append(f"ID={string_value}")
            else:
                values.append(string_value)

        if len(values) > 0:
            output_text.insert(tk.END, f"{imgdir_name} = {'/'.join(values)}\n")

def compare_files():
    # open file dialog to select the XML files
    root = tk.Tk()
    root.withdraw()
    file_path1 = filedialog.askopenfilename(title="Select XML File 1")
    file_path2 = filedialog.askopenfilename(title="Select XML File 2")

    # parse the files and get their strings
    output1 = StringIO()
    output2 = StringIO()
    parse_xml(file_path1)
    output1.write(output_text.get("1.0", tk.END))
    parse_xml(file_path2)
    output2.write(output_text.get("1.0", tk.END))

    # compare the files and display the differences
    diff = unified_diff(output1.getvalue().splitlines(keepends=True),
                        output2.getvalue().splitlines(keepends=True),
                        fromfile="Original file:\n" + file_path1,
                        tofile="File 2:\n" + file_path2)
    diff_output = ''.join(diff)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, diff_output)

# create the GUI
root = tk.Tk()
root.title("Limbs' Map.wz XML Parser")
root.geometry("800x850")

# create a button to select an XML file
select_button = tk.Button(root, text="Select an XML File", command=lambda: parse_xml(filedialog.askopenfilename()))
select_button.pack(pady=10)

# create a button to compare two XML files
compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.pack(pady=10)

# create a text box to display the output
output_text = tk.Text(root, font=("Courier New", 12))
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# set the icon
url = "https://i.imgur.com/9o4RxQ6.png"
icon_data = urllib.request.urlopen(url).read()
icon_base64 = base64.b64encode(icon_data)

icon = tk.PhotoImage(data=icon_base64)
root.iconphoto(True, icon)

# run the GUI
root.mainloop()
