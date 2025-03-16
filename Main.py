from pymem import Pymem
import pymem.process as proc
import tkinter.messagebox as msgbox
from time import sleep
import os
def GetProcess(process_name : str):
    try:
        return Pymem("{}.exe".format(process_name))
    except:
        msgbox.showerror(title="Unity3DInjector", message="Not Founded Process... Please Run This Process: " + process_name)
        os._exit(1554)

def Main():
    processname = input("Write You're Process Name(Without .exe): ")
    bkk = GetProcess(process_name=processname)
    dll_inject = input("Please Write You're DLL Filename: ")
    for x in bkk.list_modules():
        if x.name == "GameAssembly.dll":
            print("Founded in Unity3D Module(IL2Cpp)!!! Injecting...")
            converted_utf8 = bytes(dll_inject, "utf-8")
            proc.inject_dll(bkk.process_handle, converted_utf8)
            sleep(3400)
            print("Injecting Done!!! Created by RimisiusDev!!!")
            os._exit(344)
        elif x.name == "mono-2.0-bdwgc.dll":
            print("Founded Module in Unity3D(mono-library!!!)... \nP.S: This Library Is FREE-TO-USE(WITH OPEN SOURCE CODE!!!)... \nYou Can Try Create Cheeto with C++ Library(MonoLibrary from UnityTechnologies)")
            converted_utf8 = bytes(dll_inject, "utf-8")
            proc.inject_dll_from_path(bkk.process_handle, converted_utf8)
            sleep(3400)
            print("Injecting Done!!! Created by RimisiusDev!!!")
            os._exit(344)
        else:
            msgbox.showerror(title="Unity3DInjector", message="Not Founded Any of Modules(MonoLibrary or IL2CppLibrary)... Try to Write Another Process Name!!!")
            os._exit(344)

if __name__ == "__main__":
    Main()