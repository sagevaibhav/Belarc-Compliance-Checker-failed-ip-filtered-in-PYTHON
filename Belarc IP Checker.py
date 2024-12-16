import os
import re
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Text
from bs4 import BeautifulSoup

def check_belarc_compliance_with_images():
    root_directory = filedialog.askdirectory(title="Select Root Directory")
    if not root_directory:
        messagebox.showerror("Error", "No directory selected.")
        return

    search_sentence = search_entry.get().strip()
    if not search_sentence:
        messagebox.showerror("Error", "Search sentence cannot be empty.")
        return

    compliance_images = {
        "yes.gif": "Compliance Pass",
        "no.gif": "Compliance Fail"
    }

    results = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for file in filenames:
            if file.endswith(".html"):
                file_path = os.path.join(dirpath, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    soup = BeautifulSoup(f, "html.parser")
                    status = "No Compliance Image Found"

                    for tag in soup.find_all(text=search_sentence):
                        parent = tag.parent

                        prev_sibling = parent.find_previous("img")
                        if prev_sibling:
                            img_src = prev_sibling.get("src", "").split("/")[-1]
                            if img_src in compliance_images:
                                status = compliance_images[img_src]
                                break

                        next_sibling = parent.find_next("img")
                        if next_sibling:
                            img_src = next_sibling.get("src", "").split("/")[-1]
                            if img_src in compliance_images:
                                status = compliance_images[img_src]
                                break

                    relative_path = os.path.relpath(file_path, root_directory)
                    results[relative_path] = status

    output_text.delete(1.0, "end")
    output_text.insert("end", "Search Results (Filtered IPv4 Addresses Only):\n")
    ipv4_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    for file, status in results.items():
        if status == "Compliance Fail":
            match = ipv4_pattern.search(file)
            if match:
                output_text.insert("end", f"{match.group()}\n")
    
    # Add the "Made with ❤️ by Vaibhav Mishra ✨" message to the output text
    output_text.insert("end", "\n\n✨ Made with ❤️ by Vaibhav Mishra ✨")

def restart_program():
    search_entry.delete(0, "end")
    output_text.delete(1.0, "end")

root = Tk()
root.title("Belarc Compliance Checker - Made by Vaibhav Mishra")

Label(root, text="Search Sentence:").grid(row=0, column=0, padx=10, pady=10)
search_entry = Entry(root, width=50)
search_entry.grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Select Directory and Start", command=check_belarc_compliance_with_images).grid(row=1, column=0, columnspan=2, pady=10)

Button(root, text="Restart Program", command=restart_program).grid(row=2, column=0, columnspan=2, pady=10)

output_text = Text(root, width=80, height=20)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
