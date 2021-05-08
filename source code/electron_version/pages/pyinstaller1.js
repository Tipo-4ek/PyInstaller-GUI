const { ipcRenderer } = require('electron');
const { exec } = require('child_process');
const { platform } = require('os');

const choosePyFileBtn = document.getElementById('choose-py-file-btn');
var pyFile = '';
var pyDir = '';
var customIconPath = '';
var customPathDir = '';
var customExeBool = false;
var customIconBool = false;
var customPathBool = false;



/*
Get Python file
------------------------------
*/

choosePyFileBtn.addEventListener('click', function() {
    // ipcRenderer frontend js communicate with mainjs
    ipcRenderer.send('choose-py-file-dialog');
});

// mainjs returns python file
ipcRenderer.on('return-py-file-dialog', (event, pyFileIn, pyDirIn) => {
    if (pyFileIn != 'CANCELLED' && pyDirIn != 'CANCELLED') {getReturnedPyFile(pyFileIn, pyDirIn);}
    else {ipcRenderer.send('error-msg', 'Python file not selected')}
});

// Store python file in var
function getReturnedPyFile(pyFileIn, pyDirIn) {
    pyFile = pyFileIn;
    pyDir = pyDirIn;
    showCustomize();
}

//------------------------------



/*
File selections
------------------------------
*/

// Show selections
function showCustomize() {

    document.getElementById('title').innerHTML = 'Customize your program';
    document.getElementById('choose-py-file-btn').style.visibility = 'hidden';

    const showList = [
        'checks',

        'custom-exe-name-check', 'custom-exe-name-label',

        'custom-icon-check', 'custom-icon-check-label',

        'custom-path-check', 'custom-path-check-label',

        'one-file-check', 'one-file-check-label',

        'no-console-check', 'no-console-check-label',

        'clear-cache-check', 'clear-cache-check-label',
    ]

    for (const item in showList) {
        var id = showList[item];
        document.getElementById(id).style.visibility = 'visible';
    }

}

//------------------------------



/*
Make visible on check
------------------------------
*/

// Make custom exe input visible
document.getElementById('custom-exe-name-check').addEventListener('change', function() {
    if (!customExeBool) {
        customExeBool = true;
        document.getElementById('custom-exe-name-input').style.visibility = 'visible';
        document.getElementById('custom-exe-name-label').innerHTML = 'Custom .exe program name:';
    } else {
        customExeBool = false;
        document.getElementById('custom-exe-name-input').style.visibility = 'hidden';
        document.getElementById('custom-exe-name-label').innerHTML = 'Custom .exe program name';
    }
});

// Make custom icon button visible
document.getElementById('custom-icon-check').addEventListener('change', function() {
    if (!customIconBool) {
        customIconBool = true;
        document.getElementById('custom-icon-check-btn').style.visibility = 'visible';
        document.getElementById('custom-icon-check-label').innerHTML = 'Custom icon:';
    } else {
        customIconBool = false;
        document.getElementById('custom-icon-check-btn').style.visibility = 'hidden';
        document.getElementById('custom-icon-check-label').innerHTML = 'Custom icon';
    }
});

// Make custom path button visible
document.getElementById('custom-path-check').addEventListener('change', function() {
    if (!customPathBool) {
        customPathBool = true;
        document.getElementById('custom-path-check-btn').style.visibility = 'visible';
        document.getElementById('custom-path-check-label').innerHTML = 'Custom bundled app path:';
    } else {
        customPathBool = false;
        document.getElementById('custom-path-check-btn').style.visibility = 'hidden';
        document.getElementById('custom-path-check-label').innerHTML = 'Custom bundled app path';
    }
});

//------------------------------



/*
Icon, path, button functions
------------------------------
*/

document.getElementById('custom-icon-check-btn').addEventListener('click', function() {
    ipcRenderer.send('customize-program', 'custom-icon');
});

document.getElementById('custom-path-check-btn').addEventListener('click', function() {
    ipcRenderer.send('customize-program', 'custom-path');
})

// Get returned path
ipcRenderer.on('customize-program-return', (event, type, path) => {
    if (type == 'custom-icon') {
        if (path == 'CANCELLED') {ipcRenderer.send('error-msg', 'Custom icon not selected')}
        else {customIconPath = path}
    }
    else if (type == 'custom-path') {
        if (path == 'CANCELLED') {ipcRenderer.send('error-msg', 'Custom bundled app path not selected')}
        else {customPathDir = path}
    }
})

//------------------------------



/*
Main run function
------------------------------
*/

function mainRunFunction() {
    let customExeChecked = document.getElementById('custom-exe-name-check').checked;
    let customExeInput = document.getElementById('custom-exe-name-input').value
    let customIconChecked = document.getElementById('custom-icon-check').checked;
    let customPathChecked = document.getElementById('custom-path-check').checked;
    let oneFileChecked = document.getElementById('one-file-check').checked;
    let noConsoleChecked = document.getElementById('no-console-check').checked;
    let clearCacheChecked = document.getElementById('clear-cache-check').checked;
    let noRun = false;

    let execRunStr = `pyinstaller ${pyFile}`;
    let appPath = '';

    // Replace spaces
    if (pyFile.indexOf(' ') >= 0) {
        if (process.platform == 'darwin') {
            pyFile = pyFile.replace(' ', '\\ ');
        } else if (process.platform == 'win32') {
            pyFile = `"${pyFile}"`
        }
        execRunStr = `pyinstaller ${pyFile}`;
    }

    // One file
    if (oneFileChecked) {execRunStr = `${execRunStr} --onefile`}

    // No console
    if (noConsoleChecked) {execRunStr = `${execRunStr} --noconsole`}

    // Custom name
    if (customExeChecked) {
        if (customExeInput == '') {
            ipcRenderer.send('error-msg', 'Custom .exe program name checked but name not entered.');
            noRun = true;
        } else {
            if (customExeInput.indexOf(' ') >= 0) {
                if (process.platform == 'darwin') {
                    customExeInput = customExeInput.replace(' ', '\\ ')
                } else if (process.platform == 'win32') {
                    customExeInput = `"${customExeInput}"`
                }
            }
            execRunStr = `${execRunStr} --name=${customExeInput}`;
        }
    }

    // Custom icon
    if (customIconChecked) {
        if (customIconPath == 'CANCELLED' || customIconPath == '') {
            ipcRenderer.send('error-msg', 'Custom icon checked but not selected.');
            noRun = true;
        } else {
            if (customIconPath.indexOf(' ') >= 0) {
                if (process.platform == 'darwin') {
                    customIconPath = customIconPath.replace(' ', '\\ ')
                } else if (process.platform == 'win32') {
                    customIconPath = `"${customIconPath}"`
                }
            }
            execRunStr = `${execRunStr} --icon=${customIconPath}`;
        }
    }

    // Custom path
    if (customPathChecked) {
        if (customPathDir == '' || customPathDir == 'CANCELLED') {
            ipcRenderer.send('error-msg', 'Custom bundled app path checked but not selected.');
            noRun = true;
        } else {
            if (customPathDir.indexOf(' ') >= 0) {
                if (process.platform == 'darwin') {
                    customPathDir = customPathDir.replace(' ', '\\ ')
                } else if (process.platform == 'win32') {
                    customPathDir = `"${customPathDir}"`
                }
            }
            execRunStr = `${execRunStr} --distpath=${customPathDir}`;
        }
    }

    // Clear cache
    if (clearCacheChecked) {execRunStr = `${execRunStr} --clean`;}

    if (!noRun) {
        exec(execRunStr, {'cwd': pyDir});
        if (customPathChecked) {appPath = customPathDir}
        else {appPath = pyDir + '/dist'}

        let fileManager = 'Show in file manager'
        if (process.platform == 'darwin') {fileManager = ' Show in Finder'}
        else if (process.platform == 'win32') {fileManager = 'Show in File Explorer'}
        ipcRenderer.send('run-pyinstaller-success', appPath, fileManager)
        window.location.href = 'index.html'
    }
    
}

//------------------------------