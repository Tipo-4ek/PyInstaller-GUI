from tkinter import *
from tkinter import ttk as ttk
import os
import subprocess
import webbrowser

root = Tk()
s = ttk.Style()
root.geometry('600x500')
root.title('PyInstaller GUI')

s.configure("Title.TLabel", font=('*', 25), padding=15)

title = ttk.Label(root, text='PyInstaller GUI', style='Title.TLabel')
title.pack()

pipFrame = ttk.Frame(root, padding=15)
pipFrame.pack()

pipVar = IntVar()
pip3Var = IntVar()
pipCheck = ttk.Checkbutton(pipFrame, text='pip', variable=pipVar)
pipCheck.pack(side=LEFT)
pipCheck3 = ttk.Checkbutton(pipFrame, text='pip3', variable=pip3Var)
pipCheck3.pack(side=LEFT)

def newWin(geoStr, showTitle, Lab1Str):
    newWin = Toplevel()
    newWin.geometry(geoStr)
    winTitleLab = ttk.Label(newWin, text=showTitle, padding=5)
    winTitleLab.pack()
    winLab1 = ttk.Label(newWin, text=Lab1Str, padding=5)
    winLab1.pack()

def installPyInstaller():
    if str(pipVar.get()) == '1' and str(pip3Var.get()) == '1':
        newWin('350x200', 'Error:', 'pip and pip3 are both selected')
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '0':
        newWin('350x200', 'Error:', 'Neither pip nor pip3 are selected')
    elif str(pipVar.get()) == '1' and str(pip3Var.get()) == '0':
        os.system('pip install pyinstaller')
        newWin('350x200', 'Successfully installed PyInstaller', '')
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '1':
        os.system('pip3 install pyinstaller')
        newWin('350x200', 'Successfully installed PyInstaller', '')

def dirQuestionFunc():
    dirPath = Toplevel()
    dirPath.geometry('350x200')
    dirPathTitle = ttk.Label(dirPath, text='Python File Path:', padding=5)
    dirPathTitle.pack()
    dirPathExample = ttk.Label(dirPath, text='/directory/file.py', padding=5)
    dirPathExample.pack()
    dirPathLab = ttk.Label(dirPath, text='(Starts from where this app is located)', padding=5, foreground='red')
    dirPathLab.pack()

def oneFileQuestionFunc():
    newWin('400x200', 'What is \"One file\"?', 'This will compile your program into one .exe file')
    
def noConsoleQuestionFunc():
    newWin('400x200', 'What is \"No console\"?', 'This will not launch the command line for your program\nLeave this unchecked if you\'re making a command line app')

def iconQuestionFunc():
    newWin('400x200', 'Custom icon format:', 'iconfile.ico')

def dataQuestionFunc():
    def whatIsData():
        webbrowser.open_new_tab('https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-data-files')
    data = Toplevel()
    data.geometry('400x200')
    dataTitle = ttk.Label(data, text='Add data format:', padding=5)
    dataTitle.pack()
    dataExample = ttk.Label(data, text='source.file;dest', padding=5)
    dataExample.pack()
    dataWhatis = ttk.Button(data, text='What is adding data?', command=whatIsData)
    dataWhatis.pack()


def runPyInstaller():
    noRun = False

    filePathStr = str(dirPath.get())

    oneFile = str(oneFileVar.get())

    noConsole = str(noConsoleVar.get())

    iconPathCheck = str(iconVar.get())
    iconPathStr = str(iconPath.get())

    addDataCheck = str(dataVar.get())
    addDataFilesStr = str(dataIn.get())

    '''
    print(f"File path: {filePathStr}")
    print(f"One file check: {oneFile}")
    print(f"No console check: {noConsole}")
    print(f"Icon path check: {iconPathCheck}")
    print(f"Icon path: {iconPathStr}")
    print(f"Add data check: {addDataCheck}")
    print(f"Data files: {addDataFilesStr}")
    '''

    runList = ['pyinstaller']
    if filePathStr:
        runList.append(filePathStr)
    else:
        newWin('350x200', 'Error', 'No .py file entered')
        noRun = True
    if oneFile == '1':
        runList.append('--onefile')
    if noConsole == '1':
        runList.append('--noconsole')
    if iconPathCheck == '1':
        if iconPathStr:
            runList.append('--icon=' + iconPathStr)
        else:
            noRun = True
            newWin('350x200', 'Error:', 'No icon file entered')

    if addDataCheck == '1':
        if addDataFilesStr:
            runList.append('--add-data')
            runList.append(addDataFilesStr)
        else:
            noRun = True
            newWin('350x200', 'Error:', 'No data files entered')

    if noRun == False:
        newWin('500x150', 'Running in terminal:', runList)

        subprocess.call(runList)

checksFrame = ttk.Frame(root, padding=20)
checksFrame.pack()

dirPathFrame = ttk.Frame(checksFrame, padding=5)
dirPathFrame.pack()
dirPathLab = ttk.Label(dirPathFrame, text='.py File Path')
dirPathLab.pack(side=LEFT)
dirPath = ttk.Entry(dirPathFrame)
dirPath.pack(side=LEFT)
dirQuestion = ttk.Button(dirPathFrame, text='?', command=dirQuestionFunc, width=1)
dirQuestion.pack()

oneFileFrame = ttk.Frame(checksFrame, padding=5)
oneFileFrame.pack()
oneFileVar = IntVar()
oneFileCheck = ttk.Checkbutton(oneFileFrame, text='One file', variable=oneFileVar)
oneFileCheck.pack(side=LEFT)
oneFileQuestion = ttk.Button(oneFileFrame, text='?', command=oneFileQuestionFunc, width=1)
oneFileQuestion.pack(side=LEFT)

noConsoleFrame = ttk.Frame(checksFrame, padding=5)
noConsoleFrame.pack()
noConsoleVar = IntVar()
noConsoleCheck = ttk.Checkbutton(noConsoleFrame, text='No console', variable=noConsoleVar)
noConsoleCheck.pack(side=LEFT)
noConsoleQuestion = ttk.Button(noConsoleFrame, text='?', command=noConsoleQuestionFunc, width=1)
noConsoleQuestion.pack(side=LEFT)

iconFrame = ttk.Frame(checksFrame, padding=5)
iconFrame.pack()
iconVar = IntVar()
iconCheck = ttk.Checkbutton(iconFrame, text='Custom icon   ', variable=iconVar)
iconCheck.pack(side=LEFT)
iconLab = ttk.Label(iconFrame, text='Icon path:\n(from directory)')
iconLab.pack(side=LEFT)
iconPath = ttk.Entry(iconFrame, width=10)
iconPath.pack(side=LEFT)
iconQuestion = ttk.Button(iconFrame, text='?', command=iconQuestionFunc, width=1)
iconQuestion.pack(side=LEFT)

dataFrame = ttk.Frame(checksFrame, padding=5)
dataFrame.pack()
dataVar = IntVar()
dataCheck = ttk.Checkbutton(dataFrame, text='Add data files   ', variable=dataVar)
dataCheck.pack(side=LEFT)
dataLab = ttk.Label(dataFrame, text='Data files:')
dataLab.pack(side=LEFT)
dataIn = ttk.Entry(dataFrame, width=10)
dataIn.pack(side=LEFT)
dataQuestion = ttk.Button(dataFrame, text='?', command=dataQuestionFunc, width=1)
dataQuestion.pack(side=LEFT)

runPyInstaller = ttk.Button(checksFrame, text='Run PyInstaller', command=runPyInstaller)
runPyInstaller.pack()


installBtn = ttk.Button(pipFrame, text='Install PyInstaller', command=installPyInstaller)
installBtn.pack(side=LEFT)

creditFrame = ttk.Frame(root, padding=10)
creditFrame.pack()

creditLab1 = ttk.Label(creditFrame, text='PyInstaller GUI for Windows')
creditLab2 = ttk.Label(creditFrame, text='Made by: Jason')
creditLab3 = ttk.Label(creditFrame, text='This app is not associated with PyInstaller')
creditLab1.pack()
creditLab2.pack()
creditLab3.pack()

root.mainloop()