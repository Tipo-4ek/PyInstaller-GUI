'''
------------------------------

PyInstaller GUI

Author: Jason Li

------------------------------
'''



from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
import os
import subprocess
import webbrowser
import requests
from Custom_Dialog import InstallPyInstallerDialog, HelpDialog



class App(ThemedTk):


    def __init__(self):

        '''
        Initializing
        ------------------------------
        '''

        super().__init__(theme='equilux')
        # initialize window and program
        self.configure(bg='#464646')
        s = ttk.Style()
        self.geometry('600x630')
        self.title('PyInstaller GUI')
        self.currentVersion = '1.9'

        # configure styles
        s.configure("Title.TLabel", font=('*', 25), padding=15)
        s.configure("NewWin.TLabel", font=('*', 17), padding=5)

        # creates a page title
        title = ttk.Label(self, text='PyInstaller GUI', style='Title.TLabel')
        title.pack()

        self.filepath = ''

        '''
        ------------------------------
        '''



        '''
        User input for pyinstaller parameters
        ------------------------------
        '''

        # install PyInstaller
        self.installBtnRoot = ttk.Button(self, text='Install PyInstaller', command=self.installPyInstaller)
        self.installBtnRoot.pack()

        # creates div for checkboxes/entries
        self.checksFrame = ttk.Frame(self, padding=20)
        self.checksFrame.pack()

        # user input py file
        self.filePathFrame = ttk.Frame(self.checksFrame, padding=5)
        self.filePathFrame.pack()
        self.filePathLab = ttk.Label(self.filePathFrame, text='.py File')
        self.filePathLab.pack(side=LEFT)
        self.filePathBtn = ttk.Button(self.filePathFrame, text='Choose .py file', command=self.filePathGet)
        self.filePathBtn.pack(side=LEFT)
        self.filePathQuestion = ttk.Button(self.filePathFrame, text='?', command=self.filePathQuestionFunc, width=1)
        self.filePathQuestion.pack()

        # user input .exe name
        self.nameFrame = ttk.Frame(self.checksFrame, padding=5)
        self.nameFrame.pack()
        self.nameVar = IntVar()
        self.nameCheck = ttk.Checkbutton(self.nameFrame, text='Custom .exe Program Name:', variable=self.nameVar)
        self.nameCheck.pack(side=LEFT)
        self.nameIn = ttk.Entry(self.nameFrame, width=10)
        self.nameIn.pack(side=LEFT)
        self.nameInExeLab = ttk.Label(self.nameFrame, text='.exe')
        self.nameInExeLab.pack(side=LEFT)
        self.nameQuestion = ttk.Button(self.nameFrame, text='?', command=self.nameQuestionFunc, width=1)
        self.nameQuestion.pack(side=LEFT)

        # user check onefile
        self.oneFileFrame = ttk.Frame(self.checksFrame, padding=5)
        self.oneFileFrame.pack()
        self.oneFileVar = IntVar()
        self.oneFileCheck = ttk.Checkbutton(self.oneFileFrame, text='One file', variable=self.oneFileVar)
        self.oneFileCheck.pack(side=LEFT)
        self.oneFileQuestion = ttk.Button(self.oneFileFrame, text='?', command=self.oneFileQuestionFunc, width=1)
        self.oneFileQuestion.pack(side=LEFT)

        # user check noconsole
        self.noConsoleFrame = ttk.Frame(self.checksFrame, padding=5)
        self.noConsoleFrame.pack()
        self.noConsoleVar = IntVar()
        self.noConsoleCheck = ttk.Checkbutton(self.noConsoleFrame, text='No console', variable=self.noConsoleVar)
        self.noConsoleCheck.pack(side=LEFT)
        self.noConsoleQuestion = ttk.Button(self.noConsoleFrame, text='?', command=self.noConsoleQuestionFunc, width=1)
        self.noConsoleQuestion.pack(side=LEFT)

        # user check clean
        self.cleanFrame = ttk.Frame(self.checksFrame, padding=5)
        self.cleanFrame.pack()
        self.cleanVar = IntVar()
        self.cleanCheck = ttk.Checkbutton(self.cleanFrame, text='Clear cache and temporary files', variable=self.cleanVar)
        self.cleanCheck.pack(side=LEFT)
        self.cleanQuestion = ttk.Button(self.cleanFrame, text='?', command=self.cleanQuestionFunc, width=1)
        self.cleanQuestion.pack(side=LEFT)

        # user check custom icon + user input icon file
        self.iconFrame = ttk.Frame(self.checksFrame, padding=5)
        self.iconFrame.pack()
        self.iconVar = IntVar()
        self.iconCheck = ttk.Checkbutton(self.iconFrame, text='Custom icon', variable=self.iconVar)
        self.iconCheck.pack(side=LEFT)
        self.iconPath = ttk.Button(self.iconFrame, text='Choose icon file', command=self.iconFileGet)
        self.iconPath.pack(side=LEFT)
        self.iconQuestion = ttk.Button(self.iconFrame, text='?', command=self.iconQuestionFunc, width=1)
        self.iconQuestion.pack(side=LEFT)

        # user check add data + user input data files
        self.dataFrame = ttk.Frame(self.checksFrame, padding=5)
        self.dataFrame.pack()
        self.dataVar = IntVar()
        self.dataCheck = ttk.Checkbutton(self.dataFrame, text='Add data files   ', variable=self.dataVar)
        self.dataCheck.pack(side=LEFT)
        self.dataLab = ttk.Label(self.dataFrame, text='Data files:')
        self.dataLab.pack(side=LEFT)
        self.dataIn = ttk.Entry(self.dataFrame, width=10)
        self.dataIn.pack(side=LEFT)
        self.dataQuestion = ttk.Button(self.dataFrame, text='?', command=self.dataQuestionFunc, width=1)
        self.dataQuestion.pack(side=LEFT)

        # user check custom bundle path + user input custom bundle path input
        self.distpathFrame = ttk.Frame(self.checksFrame, padding=5)
        self.distpathFrame.pack()
        self.distpathVar = IntVar()
        self.distpathCheck = ttk.Checkbutton(self.distpathFrame, text='Custom bundled app path', variable=self.distpathVar)
        self.distpathCheck.pack(side=LEFT)
        self.distpathIn = ttk.Button(self.distpathFrame, text='Choose path', command=self.distPathGet)
        self.distpathIn.pack(side=LEFT)
        self.distQuestion = ttk.Button(self.distpathFrame, text='?', command=self.distQuestionFunc, width=1)
        self.distQuestion.pack(side=LEFT)

        # run pyinstaller button
        self.runPyInstaller = ttk.Button(self.checksFrame, text='Run PyInstaller', command=self.runPyInstaller)
        self.runPyInstaller.pack()

        '''
        ------------------------------
        '''



        '''
        Menubar
        ------------------------------
        '''

        # Mac about submenu
        self.createcommand('tkAboutDialog', lambda: webbrowser.open_new_tab('https://github.com/jasonli0616/PyInstaller-GUI'))

        menubar = Menu(self)
        self.config(menu=menubar)

        # File submenu
        file_menu = Menu(menubar)
        file_menu.add_command(label='New window', command=lambda: App())
        file_menu.add_command(label='Check for update', command=self.checkUpdate)
        menubar.add_cascade(label='File', menu=file_menu)

        # PyInstaller submenu
        pyinstaller_menu = Menu(menubar)
        pyinstaller_menu.add_command(label='Install PyInstaller', command=self.installPyInstaller)
        pyinstaller_menu.add_separator()
        pyinstaller_menu.add_command(label='Select Python file', command=self.filePathGet)
        pyinstaller_menu.add_command(label='Run PyInstaller', command=self.runPyInstaller)
        menubar.add_cascade(label='PyInstaller', menu=pyinstaller_menu)

        '''
        ------------------------------
        '''



        '''
        Credits (on GUI)
        ------------------------------
        '''

        # credits at bottom
        self.creditFrame = ttk.Frame(self, padding=10)
        self.creditFrame.pack()
        self.creditLab1 = ttk.Label(self.creditFrame, text='PyInstaller GUI for Windows')
        self.creditLab2 = ttk.Label(self.creditFrame, text=f'Version {self.currentVersion}')
        self.creditLab3 = ttk.Label(self.creditFrame, text='Made by: Jason')
        self.creditLab4 = ttk.Label(self.creditFrame, text='This app is not associated with PyInstaller')
        self.creditBtnFrame = ttk.Frame(self.creditFrame)
        self.sourcecodeButton = ttk.Button(self.creditBtnFrame, text='Source code', command=self.sourcecodeFunc)
        self.checkupdateButton = ttk.Button(self.creditBtnFrame, text='Check for update', command=self.checkUpdate)
        self.helpButton = ttk.Button(self.creditBtnFrame, text='Help', command=self.helpFunc)
        self.creditLab1.pack()
        self.creditLab2.pack()
        self.creditLab3.pack()
        self.creditLab4.pack()
        self.creditBtnFrame.pack()
        self.sourcecodeButton.pack(side=LEFT)
        self.checkupdateButton.pack(side=LEFT)
        self.helpButton.pack(side=LEFT)

        '''
        ------------------------------
        '''


    
    '''
    Functions
    ------------------------------
    '''


    def installPyInstaller(self):
        InstallPyInstallerDialog()


    def updateApp(self, version):
        '''
        If an update is found (in lines 131-174), will open new window requesting update
        '''
        update = messagebox.askyesno(title='Update available', message=f'Version {version} available. Update?')
        if update:
            webbrowser.open_new_tab('https://github.com/jasonli0616/PyInstaller-GUI/releases')


    def checkUpdate(self, method='Button'):
        try:
            # checks for latest version available on GitHub README file
            github_page = requests.get('https://raw.githubusercontent.com/jasonli0616/PyInstaller-GUI/main/README.md')
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
            if float(version) > float(self.currentVersion):
                self.updateApp(version)
            else:
                if method == 'Button':
                    messagebox.showinfo(title='No update found', message=f'No update found.\nLatest version: {version}')

        # do not check for update if offline
        except requests.exceptions.ConnectionError:
            if method == 'Button':
                messagebox.showwarning(title='You are offline', message='You are offline.\nPlease connect to the internet to check for update.')
            elif method == 'Button':
                pass


    def filePathGet(self):
        '''
        Get file path from user
        '''
        filePathDialog = filedialog.askopenfilename(title='Select .py file', initialdir='/', filetypes=[('Python file', '*.py')])
        self.dirpath = str(os.path.split(filePathDialog)[0])
        self.filepath = str(os.path.split(filePathDialog)[1])


    def filePathQuestionFunc(self):
        '''
        Question mark for file path
        Opens new window with explanation
        '''
        messagebox.showinfo(title='Python file', message='Select your Python file.')


    def nameQuestionFunc(self):
        '''
        Question mark for name
        Opens new window with explanation
        '''
        messagebox.showinfo(title='Application name', message='Enter custom app name.\nIf nothing is inputted, it will use the same name as your Python file.')


    def oneFileQuestionFunc(self):
        '''
        Question mark for one file
        Opens new window with explanation
        '''
        messagebox.showinfo(title='One file', message='This will bundle your program into one .exe file.')


    def noConsoleQuestionFunc(self):
        '''
        Question mark for no console
        Opens new window with explanation
        '''
        messagebox.showinfo(title='No console', message='This will not launch the command line for your program.\nLeave this unchecked if you\'re making a command line app.')


    def cleanQuestionFunc(self):
        '''
        Question mark for clear cache and temporary files
        Opens new window with explanation
        '''
        messagebox.showinfo(title='Clear cache and temporary files.', message='Clear cache and temporary files.')


    def iconFileGet(self):
        '''
        Get icon file from user
        '''
        try:
            iconPathDialog = filedialog.askopenfilename(title='Select icon file', initialdir=self.dirpath, filetypes=[('Icon file', '*.ico')])
            self.iconfile = str(os.path.split(iconPathDialog)[1])
        except NameError:
            messagebox.showerror(title='Error', message='Please do all the steps in order')


    def iconQuestionFunc(self):
        '''
        Question mark for custom icon
        Opens new window with explanation
        '''
        messagebox.showinfo(title='Custom icon', message='Use a custom icon.\nMake sure this file is in the same directory as your Python file.')


    def dataQuestionFunc(self):
        '''
        Question mark for add data files
        Opens new window with explanation
        '''
        if messagebox.askokcancel(title='Data files', message='See more info in browser?'):
            webbrowser.open_new_tab('https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-data-files')


    def distPathGet(self):
        '''
        Get dist path from user
        '''
        try:
            distPathDialog = filedialog.askdirectory(title='Choose dist path', initialdir=self.dirpath)
            self.distpath = str(distPathDialog)
        except NameError:
            messagebox.showerror(title='Error', message='Please do all the steps in order')


    def distQuestionFunc(self):
        '''
        Question mark for custom bundled app folder
        Opens new window with explanation
        '''
        messagebox.showinfo(title='Custom bundled app folder', message='Folder where your app will appear')


    def sourcecodeFunc(self):
        '''
        Opens source code on GitHub in browser
        '''
        if messagebox.askokcancel(title='Source code', message='Open in browser?'):
            webbrowser.open_new_tab('https://github.com/jasonli0616/PyInstaller-GUI/tree/main/src')


    def helpFunc(self):
        '''
        Opens window with multiple options to help user
        '''
        HelpDialog()


    def runPyInstaller(self):
        '''
        Main PyInstaller GUI function
        Runs PyInstaller in cmd prompt with parameters taken from GUI
        '''

        # gets user defined self, parameters into strings
        filePathStr = self.filepath
        nameCheck = str(self.nameVar.get())
        nameStr = str(self.nameIn.get())
        oneFile = str(self.oneFileVar.get())
        noConsole = str(self.noConsoleVar.get())
        cleanCache = str(self.cleanVar.get())
        iconPathCheck = str(self.iconVar.get())
        addDataCheck = str(self.dataVar.get())
        addDataFilesStr = str(self.dataIn.get())
        distPathCheck = str(self.distpathVar.get())
        noRun = False

        # list to run with subprocess.run()
        runList = ['pyinstaller']

        # checks user parameters (checkboxes), appends to list
        if filePathStr:
            runList.append(filePathStr)
        else:
            messagebox.showerror(title='Error', message='No Python file selected')
            noRun = True
        if nameCheck == "1":
            if nameStr:
                runList.append(f'--name={nameStr}')
            else:
                noRun = True
                messagebox.showerror(title='Error', message='No .exe name entered')
        if oneFile == '1':
            runList.append('--onefile')
        if noConsole == '1':
            runList.append('--noconsole')
        if cleanCache == '1':
            runList.append('--clean')
        if iconPathCheck == '1':
            if self.iconfile:
                runList.append(f'--icon={self.iconfile}')
            else:
                noRun = True
                messagebox.showerror(title='Error', message='No icon file selected')
        if addDataCheck == '1':
            if addDataFilesStr:
                runList.append(f'--add-data={addDataFilesStr}')
            else:
                noRun = True
                messagebox.showerror(title='Error', message='No data files entered')
        if distPathCheck == '1':
            if self.distpath:
                runList.append(f'--distpath={self.distpath}')
            else:
                noRun = True
                messagebox.showerror(title='Error', message='No bundled app folder selected')

        # run pyinstaller in terminal if no errors and opens window with terminal command
        runListStr = ''
        for i in runList:
            runListStr = runListStr + ' ' + i
        runListStr.strip()
        if noRun == False:
            try:
                runCmd = subprocess.run(runList, cwd=self.dirpath, capture_output=True)
                if runCmd.stderr.decode('utf-8') != '':
                    raise subprocess.SubprocessError(runCmd.stderr.decode('utf-8'))
                messagebox.showinfo(title='Ran PyInstaller', message=f'Running PyInstaller. Command:\n{runListStr}')
            except subprocess.SubprocessError as e:
                if messagebox.askyesno(title='Ran PyInstaller', message=f'Ran PyInstaller. Command:\n{runListStr}\nSee output?'):
                    messagebox.showerror(title='Error', message=str(e))
            except FileNotFoundError:
                if messagebox.askyesno(title='Ran PyInstaller', message=f'An error has occured. Command:\n{runListStr}\nSee more info?'):
                    messagebox.showerror(title='Command', message='Command not found')


    '''
    ------------------------------
    '''



'''
Run
------------------------------
'''

if __name__ == '__main__':
    app = App()

'''
------------------------------
'''
