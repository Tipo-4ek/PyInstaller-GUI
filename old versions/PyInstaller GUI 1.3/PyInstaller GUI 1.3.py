from tkinter import *
from tkinter import ttk as ttk
import os
import subprocess
import webbrowser
import requests



'''
GUI Initializing
------------------------------
'''

# initialize windoww
root = Tk()
s = ttk.Style()
root.geometry('600x650')
root.title('PyInstaller GUI')

# configure styles
s.configure("Title.TLabel", font=('*', 25), padding=15)
s.configure("NewWin.TLabel", font=('*', 17), padding=5)

# creates a page title
title = ttk.Label(root, text='PyInstaller GUI', style='Title.TLabel')
title.pack()

'''
------------------------------
'''



'''
------------------------------
Installing PyInstaller section
'''

# creates div for pip/pip3 install pyinstaller
pipFrame = ttk.Frame(root, padding=15)
pipFrame.pack()

def installPyInstaller():
    '''
    Function for button, installs pyinstaller in cmd prompt
    '''
    if str(pipVar.get()) == '1' and str(pip3Var.get()) == '1':
        newWin(title='Error:', content1='pip and pip3 are both selected')
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '0':
        newWin(title='Error:', content1='Neither pip nor pip3 are selected')
    elif str(pipVar.get()) == '1' and str(pip3Var.get()) == '0':
        os.system('pip install pyinstaller')
        newWin(title='Successfully installed PyInstaller')
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '1':
        os.system('pip3 install pyinstaller')
        newWin(title='Successfully installed PyInstaller')


# install pyinstaller button
pipVar = IntVar()
pip3Var = IntVar()
pipCheck = ttk.Checkbutton(pipFrame, text='pip', variable=pipVar)
pipCheck.pack(side=LEFT)
pipCheck3 = ttk.Checkbutton(pipFrame, text='pip3', variable=pip3Var)
pipCheck3.pack(side=LEFT)
installBtn = ttk.Button(pipFrame, text='Install PyInstaller', command=installPyInstaller)
installBtn.pack(side=LEFT)

'''
------------------------------
'''



'''
Functions
------------------------------
'''

def newWin(winSize='350x200', title='', content1='', content2=''):
    '''
    Creates popup window with error/success message
    This takes arguments for window size + text in window
    '''
    newWin = Toplevel()
    newWin.geometry(winSize)
    winTitleLab = ttk.Label(newWin, text=title, style="NewWin.TLabel")
    winTitleLab.pack()
    winLab1 = ttk.Label(newWin, text=content1, padding=5)
    winLab1.pack()
    winLab2 = ttk.Label(newWin, text=content2, padding=5)
    winLab2.pack()


def updateApp(version):
    '''
    If an update is found (in lines 336-354), will open new window requesting update
    '''
    update = Toplevel()
    def updateFunc():
        webbrowser.open_new_tab('https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/raw/main/PyInstaller%20GUI%20(windows).zip')
    def remindFunc():
        update.destroy()
    update.geometry('400x200')
    updateTitle = ttk.Label(update, text='Update available', style="NewWin.TLabel")
    updateTitle.pack()
    updateLab = ttk.Label(update, text=f'Version {version} available')
    updateLab.pack()
    updateBtn = ttk.Button(update, text='Update now', command=updateFunc)
    updateBtn.pack()
    remind = ttk.Button(update, text='Remind me later', command=remindFunc)
    remind.pack()


def checkUpdate(method='Button'):
    try:
        # checks for latest version available on GitHub README file
        github_page = requests.get('https://raw.githubusercontent.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/main/README.md')
        github_page_html = str(github_page.content).split()
        for i in range(1, 21):
            # checks for 1.x versions
            try:
                index = github_page_html.index(('1.' + str(i)))
                version = github_page_html[index]
            except ValueError:
                v1NotFound = True
        if v1NotFound:
            # checks for 2.x versions
            for i in range(1, 21):
                try:
                    index = github_page_html.index(('2.' + str(i)))
                    version = github_page_html[index]
                except ValueError:
                    v2NotFound = True
        if v2NotFound:
            # checks for 3.x versions
            for i in range(1, 21):
                try:
                    index = github_page_html.index(('3.' + str(i)))
                    version = github_page_html[index]
                except ValueError:
                    pass
        
        # display popup window if update found
        if float(version) > float(currentVersion):
            updateApp(version)
        else:
            if method == 'Auto':
                pass
            elif method == 'Button':
                newWin(title='No update found', content1=f'Latest version: {version}')

    # do not check for update if offline
    except requests.exceptions.ConnectionError:
        if method == 'Button':
            newWin(title='You are offline', content1='Please connect to the internet to check for update')
        elif method == 'Button':
            pass


def dirQuestionFunc():
    '''
    Question mark for file path
    Opens new window with explanation
    '''
    newWin(title='Python File Path:', content1='/directory/file.py', content2='(Starts from where this app is located)', winSize='400x200')


def nameQuestionFunc():
    '''
    Question mark for name
    Opens new window with explanation
    '''
    newWin(title='Application Name', content1='Enter custom .exe file name', content2='If no input, will use same name as py file', winSize='400x200')


def oneFileQuestionFunc():
    '''
    Question mark for one file
    Opens new window with explanation
    '''
    newWin(title='What is \"One file\"?', content1='This will compile your program into one .exe file', winSize='400x200')


def noConsoleQuestionFunc():
    '''
    Question mark for no console
    Opens new window with explanation
    '''
    newWin(title='What is \"No console\"?', content1='This will not launch the command line for your program\nLeave this unchecked if you\'re making a command line app', winSize='400x200')


def cleanQuestionFunc():
    '''
    Question mark for clear cache and temporary files
    Opens new window with explanation
    '''
    newWin(title='Clear cache and tempoary files', content1="That\'s it", winSize='400x200')


def iconQuestionFunc():
    '''
    Question mark for custom icon
    Opens new window with explanation
    '''
    newWin(title='Custom icon format:', content1='iconfile.ico', winSize='400x200')


def dataQuestionFunc():
    '''
    Question mark for add data files
    Opens new window with explanation
    '''
    def whatIsData():
        # opens browser tab with explanation for add data files
        webbrowser.open_new_tab('https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-data-files')

    data = Toplevel()
    data.geometry('400x200')
    dataTitle = ttk.Label(data, text='Add data format:', style="NewWin.TLabel")
    dataTitle.pack()
    dataExample = ttk.Label(data, text='source.file;dest', padding=5)
    dataExample.pack()
    dataWhatis = ttk.Button(data, text='What is adding data?', command=whatIsData)
    dataWhatis.pack()

def distQuestionFunc():
    '''
    Question mark for custom bundled app folder
    Opens new window with explanation
    '''
    newWin(title='Custom bundled app folder', content1='Folder where your app will appear', winSize='400x200')


def sourcecodeFunc():
    '''
    Opens source code on GitHub in browser
    '''
    webbrowser.open_new_tab('https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/tree/main/source%20code')


def runPyInstaller():
    '''
    Runs PyInstaller in cmd prompt with parameters taken from GUI
    '''

    # gets user defined parameters into strings
    filePathStr = str(dirPath.get())
    nameStr = str(nameIn.get())
    oneFile = str(oneFileVar.get())
    noConsole = str(noConsoleVar.get())
    cleanCache = str(cleanVar.get())
    iconPathCheck = str(iconVar.get())
    iconPathStr = str(iconPath.get())
    addDataCheck = str(dataVar.get())
    addDataFilesStr = str(dataIn.get())
    distPathCheck = str(distpathVar.get())
    distPathStr = str(distpathIn.get())
    noRun = False
    if " " in filePathStr:
        filePathStr = '"' + filePathStr + '"'
    if " " in nameStr:
        nameStr = '"' + nameStr + '"'
    if " " in iconPathStr:
        iconPathStr = '"' + iconPathStr + '"'
    if " " in distPathStr:
        distPathStr = '"' + distPathStr + '"'

    # list to run with subprocess.call()
    runStr = 'pyinstaller '

    # checks user parameters (checkboxes), appends to list
    if filePathStr:
        runStr = runStr + (filePathStr + ' ')
    else:
        newWin(title='Error', content1='No .py file entered')
        noRun = True
    if nameStr != "":
        runStr = runStr + ('--name ')
        runStr = runStr + (nameStr + ' ')
    if oneFile == '1':
        runStr = runStr + ('--onefile ')
    if noConsole == '1':
        runStr = runStr +('--noconsole ')
    if cleanCache == '1':
        runStr = runStr +('--clean ')
    if iconPathCheck == '1':
        if iconPathStr:
            runStr = runStr + ('--icon=' + iconPathStr + ' ')
        else:
            noRun = True
            newWin(title='Error:', content1='No icon file entered')
    if addDataCheck == '1':
        if addDataFilesStr:
            runStr = runStr + ('--add-data ')
            runStr = runStr +(addDataFilesStr + ' ')
        else:
            noRun = True
            newWin(title='Error:', content1='No data files entered')
    if distPathCheck == '1':
        if distPathStr:
            runStr = runStr + ('--distpath ')
            runStr = runStr + (distPathStr)
        else:
            noRun = True
            newWin(title='Error:', content1='No bundled app folder selected')


    # run pyinstaller in terminal if no errors and opens window with terminal command
    if noRun == False:
        newWin(title='Running in terminal:', content1=runStr, winSize='700x150')
        os.system(runStr)

'''
------------------------------
'''



'''
User input for pyinstaller parameters
------------------------------
'''

# creates div for checkboxes/entries
checksFrame = ttk.Frame(root, padding=20)
checksFrame.pack()

# user input py file
dirPathFrame = ttk.Frame(checksFrame, padding=5)
dirPathFrame.pack()
dirPathLab = ttk.Label(dirPathFrame, text='.py File Path')
dirPathLab.pack(side=LEFT)
dirPath = ttk.Entry(dirPathFrame)
dirPath.pack(side=LEFT)
dirQuestion = ttk.Button(dirPathFrame, text='?', command=dirQuestionFunc, width=1)
dirQuestion.pack()

# user input .exe name
nameFrame = ttk.Frame(checksFrame, padding=5)
nameFrame.pack()
nameLab = ttk.Label(nameFrame, text='.exe Program Name:')
nameLab.pack(side=LEFT)
nameIn = ttk.Entry(nameFrame, width=10)
nameIn.pack(side=LEFT)
nameQuestion = ttk.Button(nameFrame, text='?', command=nameQuestionFunc, width=1)
nameQuestion.pack(side=LEFT)

# user check onefile
oneFileFrame = ttk.Frame(checksFrame, padding=5)
oneFileFrame.pack()
oneFileVar = IntVar()
oneFileCheck = ttk.Checkbutton(oneFileFrame, text='One file', variable=oneFileVar)
oneFileCheck.pack(side=LEFT)
oneFileQuestion = ttk.Button(oneFileFrame, text='?', command=oneFileQuestionFunc, width=1)
oneFileQuestion.pack(side=LEFT)

# user check noconsole
noConsoleFrame = ttk.Frame(checksFrame, padding=5)
noConsoleFrame.pack()
noConsoleVar = IntVar()
noConsoleCheck = ttk.Checkbutton(noConsoleFrame, text='No console', variable=noConsoleVar)
noConsoleCheck.pack(side=LEFT)
noConsoleQuestion = ttk.Button(noConsoleFrame, text='?', command=noConsoleQuestionFunc, width=1)
noConsoleQuestion.pack(side=LEFT)

# user check clean
cleanFrame = ttk.Frame(checksFrame, padding=5)
cleanFrame.pack()
cleanVar = IntVar()
cleanCheck = ttk.Checkbutton(cleanFrame, text='Clear cache and temporary files', variable=cleanVar)
cleanCheck.pack(side=LEFT)
cleanQuestion = ttk.Button(cleanFrame, text='?', command=cleanQuestionFunc, width=1)
cleanQuestion.pack(side=LEFT)

# user check custom icon + user input icon file
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

# user check add data + user input data files
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

# user check custom bundle path + user input custom bundle path input
distpathFrame = ttk.Frame(checksFrame, padding=5)
distpathFrame.pack()
distpathVar = IntVar()
distpathCheck = ttk.Checkbutton(distpathFrame, text='Custom bundled app path   ', variable=distpathVar)
distpathCheck.pack(side=LEFT)
distpathLab = ttk.Label(distpathFrame, text='Path:')
distpathLab.pack(side=LEFT)
distpathIn = ttk.Entry(distpathFrame, width=10)
distpathIn.pack(side=LEFT)
distQuestion = ttk.Button(distpathFrame, text='?', command=distQuestionFunc, width=1)
distQuestion.pack(side=LEFT)

# run pyinstaller button
runPyInstaller = ttk.Button(checksFrame, text='Run PyInstaller', command=runPyInstaller)
runPyInstaller.pack()

'''
------------------------------
'''



'''
Credits (on GUI)
------------------------------
'''

# credits at bottom
currentVersion = '1.3'
creditFrame = ttk.Frame(root, padding=10)
creditFrame.pack()
creditLab1 = ttk.Label(creditFrame, text='PyInstaller GUI for Windows')
creditLab2 = ttk.Label(creditFrame, text=f'Version {currentVersion}')
creditLab3 = ttk.Label(creditFrame, text='Made by: Jason')
creditLab4 = ttk.Label(creditFrame, text='This app is not associated with PyInstaller')
creditBtnFrame = ttk.Frame(creditFrame)
sourcecodeButton = ttk.Button(creditBtnFrame, text='Source code', command=sourcecodeFunc)
checkupdateButton = ttk.Button(creditBtnFrame, text='Check for update', command=checkUpdate)
creditLab1.pack()
creditLab2.pack()
creditLab3.pack()
creditLab4.pack()
creditBtnFrame.pack()
sourcecodeButton.pack(side=LEFT)
checkupdateButton.pack(side=LEFT)

'''
------------------------------
'''



'''
Run
------------------------------
'''

if __name__ == '__main__':
    checkUpdate('Auto')
    root.mainloop()

'''
------------------------------
'''