Requires winshell:  pip3 install winshell

Creates shortcuts for your SecureCRT sessions so you can launch from Windows search, Everything or similar:
![image](https://i.imgur.com/OwTnnCP.png)


To use, change sessions_path to your SecureCRT sessions path, scrt to your SecureCRT.exe path and outpath to where you want the shortcuts to live and then run

To keep sessions and shortcuts in sync, if your outpath dir contains **ONLY** the SecureCRT session shortcuts, uncomment the line `shutil.rmtree(outpath, ignore_errors=True)`.  It's important that your chosen directory does not contain anything else as this line will wipe it on each run.
