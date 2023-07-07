import pygetwindow as window

data = window.getAllTitles()
for i in data:
    print(i, end="\n")
print(data)