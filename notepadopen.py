from pywinauto import application
import time

app = application.Application()
app.start("Notepad.exe")
time.sleep(3)
app.Notepad.edit.TypeKeys("Hello World")
time.sleep(2)
app.Notepad.MenuSelect("File ->SaveAs")
app.SaveAs.edit.SetText("pywinautodemo.txt")
app.SaveAs.Save.Click()