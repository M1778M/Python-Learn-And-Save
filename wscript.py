import win32com.client as W

ws = W.Dispatch('wscript.shell')

#ws.MsgBox("Hello")

ws.SendKeys('Hello')

ws.run('notepad.exe')


