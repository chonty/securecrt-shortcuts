import os
import winshell
from pathlib import Path
import glob
import shutil

sessions_path = "C:\\Users\\lee\\OneDrive\\Documents\\SecureCRT\\Config.personal\\Sessions\\"
scrt = "C:\\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.exe"
desktop = Path(winshell.desktop())
outpath = str(desktop / "scrt")
sessions = glob.glob(sessions_path + r"\**", recursive=True)
sessions = [x for x in sessions if x.endswith(".ini")]
directories = []

shutil.rmtree(outpath, ignore_errors=True)

for i in range(len(sessions)):
    sessions[i] = sessions[i].replace(sessions_path, "")
    sessions[i] = sessions[i].replace(".ini", "")
    filepath = os.path.dirname(sessions[i])
    directories.append(outpath + "\\" + filepath)

directories = list(set(directories))

for d in directories:
    Path(d).mkdir(parents=True, exist_ok=True)

for session in sessions:
    args = '/T /S "' + session + '"'
    link_filepath = outpath + "\\" + session + ".lnk"
    with winshell.shortcut(link_filepath) as link:
        link.path = scrt
        link.arguments = args
