const { ipcRenderer } = require('electron');
const { exec } = require('child_process');

const installBtn = document.getElementById('install-btn');
const customInstallBtn = document.getElementById('run-terminal-btn');

// Get pip/pip3 selection
function pipInstall() {
    let pipChecked = document.getElementById('pipCheck').checked;
    let pip3Checked = document.getElementById('pip3Check').checked;
    
    // Error catching, if both/none are selected
    if (pipChecked && pip3Checked) {
        // ipcRenderer = frontend js communicate with mainjs
        ipcRenderer.send('pip-install-error', 'pip and pip3 are both selected.');
    } else if (pipChecked == false && pip3Checked == false) {
        // ipcRenderer = frontend js communicate with mainjs
        ipcRenderer.send('pip-install-error', 'Neither pip nor pip3 are selected.');
    } else if (pipChecked) {
        // Run in terminal
        exec('pip install pyinstaller');
        // ipcRenderer = frontend js communicate with mainjs
        ipcRenderer.send('pip-install-success', 'pip install pyinstaller');
    } else if (pip3Checked) {
        // Run in terminal
        exec('pip3 install pyinstaller');
        // ipcRenderer = frontend js communicate with mainjs
        ipcRenderer.send('pip-install-success', 'pip3 install pyinstaller');
    }
}

// OR

// Run custom install pyinstaller
function customInstall() {
    let customInstallInput = document.getElementById('custom-install').value;
    if (customInstallInput != '') {
        // Run in terminal
        exec(customInstallInput);
        // ipcRenderer = frontend js communicate with mainjs
        ipcRenderer.send('pip-custom-install');
    } else {ipcRenderer.send('pip-install-error', 'Custom install cannot be blank.')}
}


installBtn.addEventListener('click', function() {
    pipInstall();
})
customInstallBtn.addEventListener('click', function() {
    customInstall();
})