'''
------------------------------

Custom dialogs
For: PyInstaller GUI

Author: Jason Li

------------------------------
'''



from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
import subprocess
import webbrowser



class InstallPyInstallerDialog(Toplevel):
    '''
    Dialog to install PyInstaller
    '''
    def __init__(self):
        super().__init__()
        self.geometry('450x210')
        self.configure(bg='#464646')
        self.installPyInstallerTitle = ttk.Label(self, text='Install PyInstaller', style="Title.TLabel")
        self.installPyInstallerTitle.pack()

        self.pipFrame = ttk.Frame(self, padding=10)
        self.pipFrame.pack()
        self.pipVar = IntVar()
        self.pip3Var = IntVar()
        self.pipCheck = ttk.Checkbutton(self.pipFrame, text='pip', variable=self.pipVar)
        self.pipCheck.pack(side=LEFT)
        self.pipCheck3 = ttk.Checkbutton(self.pipFrame, text='pip3', variable=self.pip3Var)
        self.pipCheck3.pack(side=LEFT)
        self.pipInstallBtn = ttk.Button(self.pipFrame, text='Install PyInstaller', command=lambda: self.installPyInstallerDo('pip'))
        self.pipInstallBtn.pack(side=LEFT)

        self.installPyInstallerOrLab = ttk.Label(self, text='or', style='NewWin.TLabel')
        self.installPyInstallerOrLab.pack()

        self.customPyInstallerFrame = ttk.Frame(self, padding=10)
        self.customPyInstallerFrame.pack()
        self.customPyInstallerEntry = ttk.Entry(self.customPyInstallerFrame)
        self.customPyInstallerEntry.pack(side=LEFT)
        self.customInstallBtn = ttk.Button(self.customPyInstallerFrame, text='Custom Install PyInstaller', command=lambda: self.installPyInstallerDo('custom'))
        self.customInstallBtn.pack(side=LEFT)

    def installPyInstallerDo(self, method):
        if method == 'pip':
            if str(self.pipVar.get()) == '1' and str(self.pip3Var.get()) == '1':
                messagebox.showerror(title='Error', message='pip and pip3 are both selected')
            elif str(self.pipVar.get()) == '0' and str(self.pip3Var.get()) == '0':
                messagebox.showerror(title='Error', message='Neither pip nor pip3 are selected')

            elif str(self.pipVar.get()) == '1' and str(self.pip3Var.get()) == '0':
                try:
                    runCmd = subprocess.run(['pip', 'install', 'pyinstaller'], capture_output=True)
                    if runCmd.stderr.decode('utf-8') != '':
                        raise subprocess.SubprocessError(runCmd.stderr.decode('utf-8'))
                    messagebox.showinfo(title='Success', message='Successfully installed PyInstaller')
                except subprocess.SubprocessError as e:
                    if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                        messagebox.showerror(title='Error', message=str(e))
                except FileNotFoundError:
                    if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                        messagebox.showerror(title='Error', message='Command not found')
            elif str(self.pipVar.get()) == '0' and str(self.pip3Var.get()) == '1':
                try:
                    runCmd = subprocess.run(['pip3', 'install', 'pyinstaller'], capture_output=True)
                    if runCmd.stderr.decode('utf-8') != '':
                        raise subprocess.SubprocessError(runCmd.stderr.decode('utf-8'))
                    messagebox.showinfo(title='Success', message='Successfully installed PyInstaller')
                except subprocess.SubprocessError as e:
                    if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                        messagebox.showerror(title='Error', message=str(e))
                except FileNotFoundError:
                    if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                        messagebox.showerror(title='Error', message='Command not found')
        
        elif method == 'custom':
            try:
                runCmd = subprocess.run(str(self.customPyInstallerEntry.get()).split(), capture_output=True)
                if runCmd.stderr.decode('utf-8') != '':
                    raise subprocess.SubprocessError(runCmd.stderr.decode('utf-8'))
                messagebox.showinfo(title='Success', message='Ran your command')
            except subprocess.SubprocessError as e:
                if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                    messagebox.showerror(title='Error', message=str(e))
            except FileNotFoundError:
                if messagebox.askyesno(title='Error', message='An error has occured. See more info?'):
                    messagebox.showerror(title='Error', message='Command not found')

class HelpDialog(Toplevel):
    '''
    Opens window with multiple options to help user
    '''
    def __init__(self):
        super().__init__()
        self.config(bg='#464646')
        ttk.Label(self, text='Help', style="NewWin.TLabel").pack()
        ttk.Label(self, text='PyInstaller is not associated with PyInstaller, therefore we cannot provide help with PyInstaller.').pack()
        ttk.Label(self, text='For help with this app for to report a bug, create an issue on GitHub.').pack()
        ttk.Label(self, text='For help with PyInstaller, visit their website.').pack()
        ttk.Button(self, text='PyInstaller website', command=lambda: webbrowser.open_new_tab('https://www.pyinstaller.org')).pack()
        ttk.Button(self, text='Create issue on GitHub', command=lambda: webbrowser.open_new_tab('https://github.com/jasonli0616/PyInstaller-GUI/issues')).pack()



'''
------------------------------
'''