import os, subprocess, sys, requests
def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
for x in os.listdir(os.path.expanduser('~')+'\\Documents'):
    if x != 'WindowsPowerShell':
        createFolder(os.path.expanduser('~')+'\\Documents\\WindowsPowerShell')
        File = open(os.path.expanduser('~')+'\\Documents\\WindowsPowerShell\\'+'Microsoft.PowerShell_profile.ps1','w+')
        File.write(requests.get('https://raw.githubusercontent.com/lptstr/winfetch/master/src/posh-winfetch.ps1').text)
        File.close()
        subprocess.Popen(["powershell.exe", ""], stdout=sys.stdout).communicate()
    elif x == 'WindowsPowerShell':
        File = open(os.path.expanduser('~')+'\\Documents\\WindowsPowerShell\\'+'Microsoft.PowerShell_profile.ps1','w+')
        File.write(requests.get('https://raw.githubusercontent.com/lptstr/winfetch/master/src/posh-winfetch.ps1').text)
        File.close()
        subprocess.Popen(["powershell.exe", ""], stdout=sys.stdout).communicate()
