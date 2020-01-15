Creates shortcuts for your SecureCRT sessions so you can launch from Windows search, Everything or similar:
![image](https://i.imgur.com/OwTnnCP.png)

**IMPORTANT: DO NOT RUN UNTIL YOU ENSURE THAT outpath IS A NEW, UNUSED DIRECTORY BECAUSE THE SCRIPT WIPES IT ON EACH RUN!**  Alternatively, remove this line: `shutil.rmtree(outpath, ignore_errors=True)`


To use, change sessions_path to your SecureCRT sessions path, scrt to your SecureCRT.exe path and outpath to where you want the shortcuts to live and then run

Requires winshell:  pip3 install winshell

