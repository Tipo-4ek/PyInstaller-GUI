'''
------------------------------

PyInstaller GUI

Made by: Jason Li

------------------------------
'''



# print message while GUI loads
print('\n\n\nWelcome to PyInstaller GUI! Please do not close this terminal window.\n\n\n')

from tkinter import *
from tkinter import ttk as ttk
from tkinter.filedialog import askopenfilename, askdirectory
from ttkthemes import ThemedTk
import os
import subprocess
from webbrowser import open_new_tab as browser_open
import requests
import platform



'''
Initializing
------------------------------
'''

# initialize window and program
root = ThemedTk(theme='equilux')
root.configure(bg='#464646')
s = ttk.Style()
root.geometry('600x630')
root.title('PyInstaller GUI')
currentVersion = '1.8'

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
Installing PyInstaller section
------------------------------
'''

def installPyInstaller():
    '''
    Function to install PyInstaller, opens window with installing options
    '''

    def installPyInstallerDo(method):
        if method == 'pip':
            if str(pipVar.get()) == '1' and str(pip3Var.get()) == '1':
                newWin(
                    title='Error:',
                    content1='pip and pip3 are both selected'
                )
            elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '0':
                newWin(
                    title='Error:',
                    content1='Neither pip nor pip3 are selected'
                )
            elif str(pipVar.get()) == '1' and str(pip3Var.get()) == '0':
                os.system('pip install pyinstaller')
                newWin(
                    title='Successfully installed PyInstaller',
                    content1='You can close this window'
                )
            elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '1':
                os.system('pip3 install pyinstaller')
                newWin(
                    title='Successfully installed PyInstaller',
                    content1='You can close this window'
                )
        
        elif method == 'custom':
            os.system(str(customPyInstallerEntry.get()))
            newWin(
                    title='Ran your command in terminal',
                    content1='You can close this window'
                )

    installPyInstallerWin = Toplevel()
    installPyInstallerWin.geometry('450x210')
    installPyInstallerWin.configure(bg='#464646')
    installPyInstallerTitle = ttk.Label(installPyInstallerWin, text='Install PyInstaller', style="Title.TLabel")
    installPyInstallerTitle.pack()

    pipFrame = ttk.Frame(installPyInstallerWin, padding=10)
    pipFrame.pack()
    pipVar = IntVar()
    pip3Var = IntVar()
    pipCheck = ttk.Checkbutton(pipFrame, text='pip', variable=pipVar)
    pipCheck.pack(side=LEFT)
    pipCheck3 = ttk.Checkbutton(pipFrame, text='pip3', variable=pip3Var)
    pipCheck3.pack(side=LEFT)
    pipInstallBtn = ttk.Button(pipFrame, text='Install PyInstaller', command=lambda: installPyInstallerDo('pip'))
    pipInstallBtn.pack(side=LEFT)

    installPyInstallerOrLab = ttk.Label(installPyInstallerWin, text='or', style='NewWin.TLabel')
    installPyInstallerOrLab.pack()

    customPyInstallerFrame = ttk.Frame(installPyInstallerWin, padding=10)
    customPyInstallerFrame.pack()
    customPyInstallerEntry = ttk.Entry(customPyInstallerFrame)
    customPyInstallerEntry.pack(side=LEFT)
    customInstallBtn = ttk.Button(customPyInstallerFrame, text='Custom Install PyInstaller', command=lambda: installPyInstallerDo('custom'))
    customInstallBtn.pack(side=LEFT)


installBtnRoot = ttk.Button(root, text='Install PyInstaller', command=installPyInstaller)
installBtnRoot.pack()

'''
------------------------------
'''



'''
Old Installing PyInstaller section
------------------------------


# creates div for pip/pip3 install pyinstaller
pipFrame = ttk.Frame(root, padding=15)
pipFrame.pack()

def installPyInstaller():
    \'''
    Function for button, installs pyinstaller in cmd prompt
    \'''
    if str(pipVar.get()) == '1' and str(pip3Var.get()) == '1':
        newWin(
            title='Error:',
            content1='pip and pip3 are both selected'
        )
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '0':
        newWin(
            title='Error:',
            content1='Neither pip nor pip3 are selected'
        )
    elif str(pipVar.get()) == '1' and str(pip3Var.get()) == '0':
        os.system('pip install pyinstaller')
        newWin(
            title='Successfully installed PyInstaller'
        )
    elif str(pipVar.get()) == '0' and str(pip3Var.get()) == '1':
        os.system('pip3 install pyinstaller')
        newWin(
            title='Successfully installed PyInstaller'
        )


# install pyinstaller button
pipVar = IntVar()
pip3Var = IntVar()
pipCheck = ttk.Checkbutton(pipFrame, text='pip', variable=pipVar)
pipCheck.pack(side=LEFT)
pipCheck3 = ttk.Checkbutton(pipFrame, text='pip3', variable=pip3Var)
pipCheck3.pack(side=LEFT)
installBtn = ttk.Button(pipFrame, text='Install PyInstaller', command=installPyInstaller)
installBtn.pack(side=LEFT)


------------------------------
'''



'''
Functions
------------------------------
'''

def newWin(
        winSize='350x200',
        title='', content1='', content2='', content3='', content4='',
        button1txt='', button1cmd='',
        button2txt='', button2cmd=''
    ):
    '''
    Creates popup window with error/success message
    This takes arguments for window size + title + content (text) + buttons
    '''
    newWin = Toplevel()
    newWin.geometry(winSize)
    newWin.configure(bg='#464646')
    if title != '':
        winTitleLab = ttk.Label(newWin, text=title, style="NewWin.TLabel")
        winTitleLab.pack()
    if content1 != '':
        winLab1 = ttk.Label(newWin, text=content1, padding=5)
        winLab1.pack()
    if content2 != '':
        winLab2 = ttk.Label(newWin, text=content2, padding=5)
        winLab2.pack()
    if content3 != '':
        winLab3 = ttk.Label(newWin, text=content3, padding=5)
        winLab3.pack()
    if content4 != '':
        winLab4 = ttk.Label(newWin, text=content4, padding=5)
        winLab4.pack()
    if button1txt != '' and button1cmd != '':
        winBtn1 = ttk.Button(newWin, text=button1txt, command=button1cmd)
        winBtn1.pack()
    if button2txt != '' and button1cmd != '':
        winBtn2 = ttk.Button(newWin, text=button2txt, command=button2cmd)
        winBtn2.pack()


def updateApp(version):
    '''
    If an update is found (in lines 131-174), will open new window requesting update
    '''
    def updateFunc():
        browser_open('https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/raw/main/PyInstaller%20GUI%20(windows).zip')
    newWin(
        winSize='400x150',
        title='Update available',
        content1=f'Version {version} available',
        button1txt='Update now', button1cmd=updateFunc,
    )


def checkUpdate(method='Button'):
    try:
        # checks for latest version available on GitHub README file
        github_page = requests.get('https://raw.githubusercontent.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/main/README.md')
        github_page_html = str(github_page.content).split()
        for i in range(0, 21):
            # checks for 1.x versions
            try:
                index = github_page_html.index(('1.' + str(i)))
                version = github_page_html[index]
            except ValueError:
                v1NotFound = True
        if v1NotFound:
            # checks for 2.x versions
            for i in range(0, 21):
                try:
                    index = github_page_html.index(('2.' + str(i)))
                    version = github_page_html[index]
                except ValueError:
                    v2NotFound = True
        if v2NotFound:
            # checks for 3.x versions
            for i in range(0, 21):
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
                newWin(
                    title='No update found',
                    content1=f'Latest version: {version}'
                )

    # do not check for update if offline
    except requests.exceptions.ConnectionError:
        if method == 'Button':
            newWin(
                title='You are offline',
                content1='Please connect to the internet to check for update'
            )
        elif method == 'Button':
            pass


def filePathGet():
    '''
    Get file path from user
    '''
    global dirpath, filepath
    filePathDialog = askopenfilename(title='Select .py file', initialdir='/', filetypes=[('Python file', '*.py')])
    dirpath = str(os.path.split(filePathDialog)[0])
    filepath = str(os.path.split(filePathDialog)[1])


def filePathQuestionFunc():
    '''
    Question mark for file path
    Opens new window with explanation
    '''
    newWin(
        title='Python File:',
        content1='Select your Python file',
        winSize='400x200'
    )


def nameQuestionFunc():
    '''
    Question mark for name
    Opens new window with explanation
    '''
    newWin(
        title='Application Name',
        content1='Enter custom .exe file name',
        content2='If no input, will use same name as .py file',
        winSize='400x200'
    )


def oneFileQuestionFunc():
    '''
    Question mark for one file
    Opens new window with explanation
    '''
    newWin(
        title='What is \"One file\"?',
        content1='This will bundle your program into one .exe file',
        winSize='400x200'
    )


def noConsoleQuestionFunc():
    '''
    Question mark for no console
    Opens new window with explanation
    '''
    newWin(
        title='What is \"No console\"?',
        content1='This will not launch the command line for your program\nLeave this unchecked if you\'re making a command line app',
        winSize='400x200'
    )


def cleanQuestionFunc():
    '''
    Question mark for clear cache and temporary files
    Opens new window with explanation
    '''
    newWin(
        title='Clear cache and temporary files',
        content1="That\'s it",
        winSize='400x200'
    )


def iconFileGet():
    '''
    Get icon file from user
    '''
    try:
        global iconfile, dirpath
        iconPathDialog = askopenfilename(title='Select icon file', initialdir=dirpath, filetypes=[('Icon file', '*.ico')])
        iconfile = str(os.path.split(iconPathDialog)[1])
    except NameError:
        newWin(
            winSize='350x200',
            title='Error:',
            content1='Please do all the steps in order'
        )


def iconQuestionFunc():
    '''
    Question mark for custom icon
    Opens new window with explanation
    '''
    newWin(
        title='Custom icon',
        winSize='500x150',
        content1='Use a custom icon',
    )


def dataQuestionFunc():
    '''
    Question mark for add data files
    Opens new window with explanation
    '''
    def whatIsData():
        # opens browser tab with explanation for add data files
        browser_open('https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-data-files')
    newWin(
        winSize='400x200',
        title='Add data format:',
        content1='source.file;dest',
        button1txt='What is adding data?', button1cmd=whatIsData,
    )


def distPathGet():
    '''
    Get dist path from user
    '''
    try:
        global distpath
        distPathDialog = askdirectory(title='Choose dist path', initialdir=dirpath)
        distpath = str(distPathDialog)
    except NameError:
        newWin(
            winSize='350x200',
            title='Error:',
            content1='Please do all the steps in order'
        )


def distQuestionFunc():
    '''
    Question mark for custom bundled app folder
    Opens new window with explanation
    '''
    newWin(
        title='Custom bundled app folder',
        content1='Folder where your app will appear',
        winSize='500x200'
    )


def sourcecodeFunc():
    '''
    Opens source code on GitHub in browser
    '''
    browser_open('https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/tree/main/source%20code')


def helpFunc():
    '''
    Opens window with multiple options to help user
    '''
    def pyInstallerWebsite():
        browser_open('https://www.pyinstaller.org')
    def createIssue():
        browser_open('https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/issues')
    newWin(
        winSize='600x225',
        title='Help',
        content1='PyInstaller GUI is based off of but not associated with PyInstaller,',
        content2='therefore we cannot provide help on PyInstaller.',
        content3='For help on PyInstaller, please head to their website.',
        content4='For help with this GUI or to report a bug/issue, please create an issue on GitHub.',
        button1txt='PyInstaller website', button1cmd=pyInstallerWebsite,
        button2txt='Create an issue', button2cmd=createIssue,
    )


def openPy2App():
    '''
    Recommends py2app to macOS users
    '''
    browser_open('https://pypi.org/project/py2app/')


def runPyInstaller():
    '''
    Main PyInstaller GUI function
    Runs PyInstaller in cmd prompt with parameters taken from GUI
    '''

    global filepath, dirpath, iconfile, distpath

    # gets user defined parameters into strings
    filePathStr = filepath
    nameCheck = str(nameVar.get())
    nameStr = str(nameIn.get())
    oneFile = str(oneFileVar.get())
    noConsole = str(noConsoleVar.get())
    cleanCache = str(cleanVar.get())
    iconPathCheck = str(iconVar.get())
    addDataCheck = str(dataVar.get())
    addDataFilesStr = str(dataIn.get())
    distPathCheck = str(distpathVar.get())
    noRun = False

    # list to run with subprocess.call()
    runList = ['pyinstaller']

    # checks user parameters (checkboxes), appends to list
    if filePathStr:
        runList.append(filePathStr)
    else:
        newWin(
            title='Error',
            content1='No .py file entered'
        )
        noRun = True
    if nameCheck == "1":
        if nameStr:
            runList.append(f'--name={nameStr}')
        else:
            noRun = True
            newWin(
                title='Error:',
                content1='No .exe name entered'
            )
    if oneFile == '1':
        runList.append('--onefile')
    if noConsole == '1':
        runList.append('--noconsole')
    if cleanCache == '1':
        runList.append('--clean')
    if iconPathCheck == '1':
        if iconfile:
            runList.append(f'--icon={iconfile}')
        else:
            noRun = True
            newWin(
                title='Error:',
                content1='No icon file entered'
            )
    if addDataCheck == '1':
        if addDataFilesStr:
            runList.append(f'--add-data={addDataFilesStr}')
        else:
            noRun = True
            newWin(
                title='Error:',
                content1='No data files entered'
            )
    if distPathCheck == '1':
        if distpath:
            runList.append(f'--distpath={distpath}')
        else:
            noRun = True
            newWin(
                title='Error:',
                content1='No bundled app folder selected'
            )

    # run pyinstaller in terminal if no errors and opens window with terminal command
    if noRun == False:
        newWin(
            title='Success',
            winSize='300x150',
        )
        subprocess.call(runList, cwd=dirpath)


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
filePathFrame = ttk.Frame(checksFrame, padding=5)
filePathFrame.pack()
filePathLab = ttk.Label(filePathFrame, text='.py File')
filePathLab.pack(side=LEFT)
filePath = ttk.Button(filePathFrame, text='Choose .py file', command=filePathGet)
filePath.pack(side=LEFT)
filePathQuestion = ttk.Button(filePathFrame, text='?', command=filePathQuestionFunc, width=1)
filePathQuestion.pack()

# user input .exe name
nameFrame = ttk.Frame(checksFrame, padding=5)
nameFrame.pack()
nameVar = IntVar()
nameCheck = ttk.Checkbutton(nameFrame, text='Custom .exe Program Name:', variable=nameVar)
nameCheck.pack(side=LEFT)
nameIn = ttk.Entry(nameFrame, width=10)
nameIn.pack(side=LEFT)
nameInExeLab = ttk.Label(nameFrame, text='.exe')
nameInExeLab.pack(side=LEFT)
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
iconCheck = ttk.Checkbutton(iconFrame, text='Custom icon', variable=iconVar)
iconCheck.pack(side=LEFT)
iconPath = ttk.Button(iconFrame, text='Choose icon file', command=iconFileGet)
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
distpathCheck = ttk.Checkbutton(distpathFrame, text='Custom bundled app path', variable=distpathVar)
distpathCheck.pack(side=LEFT)
distpathIn = ttk.Button(distpathFrame, text='Choose path', command=distPathGet)
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
creditFrame = ttk.Frame(root, padding=10)
creditFrame.pack()
creditLab1 = ttk.Label(creditFrame, text='PyInstaller GUI for Windows')
creditLab2 = ttk.Label(creditFrame, text=f'Version {currentVersion}')
creditLab3 = ttk.Label(creditFrame, text='Made by: Jason')
creditLab4 = ttk.Label(creditFrame, text='This app is not associated with PyInstaller')
creditBtnFrame = ttk.Frame(creditFrame)
sourcecodeButton = ttk.Button(creditBtnFrame, text='Source code', command=sourcecodeFunc)
checkupdateButton = ttk.Button(creditBtnFrame, text='Check for update', command=checkUpdate)
helpButton = ttk.Button(creditBtnFrame, text='Help', command=helpFunc)
creditLab1.pack()
creditLab2.pack()
creditLab3.pack()
creditLab4.pack()
creditBtnFrame.pack()
sourcecodeButton.pack(side=LEFT)
checkupdateButton.pack(side=LEFT)
helpButton.pack(side=LEFT)

# recommends py2app for macOS users
if str(platform.system()) == 'Darwin':
    newWin(
        winSize='400x150',
        title='We noticed you are on macOS',
        content1='py2app is better for macOS Python GUI programs!',
        content2='(py2app does not work for command line programs)',
        button1txt='Py2App', button1cmd=openPy2App,
    )

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
