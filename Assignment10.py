import tkinter as tk
import webbrowser

def nav():
    url = entry.get()
    print("Navigate to website = ", url)
    webbrowser.open(url)

main_page = tk.Tk()
main_page.title("* Navigate Into Websites *")

# Creating a label and an field to enter data
label = tk.Label(main_page, text="Enter a website URL:")
label.pack()
entry = tk.Entry(main_page)
entry.pack()

# Creating a button to navigate to the entered website
button = tk.Button(main_page, text="SEARCH", command=nav)
button.pack()

main_page.mainloop()