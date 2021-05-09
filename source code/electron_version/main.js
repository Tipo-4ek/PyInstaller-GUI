/*
------------------------------

PyInstaller GUI
Electron JS Rewrite

Author: Jason Li

------------------------------
*/



const { app, BrowserWindow, Menu, dialog, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');
require('electron-reload')(__dirname);

var pyFile = ''
var fileDirPath = ''



/*
Menubar
------------------------------
*/

const menu = Menu.buildFromTemplate([
    {role: 'appMenu'},
    {
        label: 'File',
        submenu: [
            {
                label: 'New window',
                click: () => {createWindow()}
            },
            {
                label: 'Open source code',
                click: () => {createWindow(loadFile='', loadURL='https://github.com/HDSB-GWS-ProgrammingClub/PyInstaller-GUI/tree/main/source%20code')}
            },
            {type: 'separator'},
            {role: 'quit'}
        ]
    },
    {
        label: 'Install',
        submenu: [
            {
                label: 'Open installation page',
                click: () => {createWindow('pages/install.html')}
            },
            {type: 'separator'},
            {
                label: 'pip install pyinstaller',
                click: () => {
                    exec('pip install pyinstaller');
                    dialog.showMessageBox({
                        message: 'Successfully installed PyInstaller',
                        detail: `Ran 'pip install pyinstaller' in terminal, PyInstaller GUI cannot guarantee installation of pip or Python.`
                    })
                }
            },
            {
                label: 'pip3 install pyinstaller',
                click: () => {
                    exec('pip3 install pyinstaller');
                    dialog.showMessageBox({
                        message: 'Successfully installed PyInstaller',
                        detail: `Ran 'pip3 install pyinstaller' in terminal, PyInstaller GUI cannot guarantee installation of pip or Python.`
                    })
                }
            },
        ]
    },
    {
        label: 'Run',
        submenu: [
            {
                label: 'Open PyInstaller page',
                click: () => {createWindow('pages/pyinstaller1.html')}
            }
        ]
    },
    {role: 'viewMenu'},
    {role: 'windowMenu'}
])

Menu.setApplicationMenu(menu)

//------------------------------



/*
Electron boilerplate
------------------------------
*/

function createWindow(loadFile='pages/index.html', loadURL='') {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })

    if (loadFile != '') {win.loadFile(loadFile)}
    if (loadURL != '') {win.loadURL(loadURL)}
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        };
    });
});

//------------------------------



/*
pages/install.js
pages/install.html

ipcMain/ipcRenderer mainjs and frontend interaction
Error/success popup messages on pip install
------------------------------
*/

ipcMain.on("pip-install-error", (event, msg) => {
    dialog.showErrorBox('PyInstaller installation error', msg)
})

ipcMain.on("pip-install-success", (event, msg) => {
    dialog.showMessageBox({
        message: 'Successfully installed PyInstaller',
        detail: `Ran '${msg}' in terminal, PyInstaller GUI cannot guarantee installation of pip or Python.`
    })
})

ipcMain.on("pip-custom-install", (event) => {
    dialog.showMessageBox({
        message: 'Ran command in terminal',
        detail: 'PyInstaller GUI cannot guarantee correct installation of Python, or PyInstaller through custom installation.'
    })
})

//------------------------------



/*
pages/pyinstaller1.js
pages/pyinstaller1.html

ipcMain/ipcRenderer mainjs and frontend interaction
Get pyinstaller info
------------------------------
*/

// Get file path on frontend js button click event
ipcMain.on("choose-py-file-dialog", (event) => {

    // Opens file dialog
    dialog.showOpenDialog({
        title: 'Choose Python file',
        defaultPath: '/',
        buttonLabel: 'Select .py file',
        properties: ['openFile'],
        filters: [
            {name: 'Python file', extensions: ['py']}
        ],
        properties: ['openFile']
    }).then(result => {
        if (result.canceled) {event.reply('return-py-file-dialog', 'CANCELLED', 'CANCELLED')}
        else {
            pyFile = path.parse(result.filePaths[0]).name + '.py';
            fileDirPath = path.parse(result.filePaths[0]).dir;
            // Returns python file to frontend js
            event.reply('return-py-file-dialog', pyFile, fileDirPath);
        }
    })
})

// Icon, path, button function file dialogs
ipcMain.on('custom-icon', (event) => {
    dialog.showOpenDialog({
        title: 'Choose icon file',
        defaultPath: fileDirPath,
        buttonLabel: 'Select .ico file',
        properties: ['openFile'],
        filters: [
            {name: 'Icon file', extensions: ['ico']}
        ]
    }).then(result => {
        if (result.canceled) {event.reply('custom-icon-return', 'CANCELLED')}
        else {
            let iconFile = path.parse(result.filePaths[0]).name + '.ico';
            // Returns icon file to frontend js
            event.reply('custom-icon-return', iconFile)
        }
    })
})

// Display error message on event
ipcMain.on('error-msg', (event, msg) => {
    dialog.showErrorBox('Error', msg)
})

// Show message after run PyInstaller
ipcMain.on('run-pyinstaller-success', (event, appPath, fileManagerMsg) => {
    dialog.showMessageBox({
        'message': 'Running PyInstaller',
        'detail': 'PyInstaller may take a few more seconds or up to a minute to finish.',
        'buttons': ['Ok', fileManagerMsg]
    }).then(result => {
        let successResponse = (result.response);
        if (successResponse == 1) {
            if (process.platform == 'win32') {exec(`start ${appPath}`, {cwd: '/'})}
            else {exec(`open ${appPath}`, {cwd: '/'})}
        }
    })
})

//------------------------------