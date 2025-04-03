To work with python, we first need to install a couple of programs. For the purposes of this course, we will use VS Code as our code editor.

# Setup

## Install python

Download python from [https://www.python.org/downloads/](https://www.python.org/downloads/). After the installer is done, you can verify your installation using the following command in the command prompt:

```bash
python --version
```

Python by default comes with a package manager called `pip`. To verify this has been installed, use the following command:
```bash
pip --version
```

Once this has been done, your python environment is set up.

## Install VS Code

The IDE or code editor we'll be using for this course is Visual Studio Code. (Visual studio code is a lightweight code editor. For more heavy usage it's recommended to use something like [Pycharm](https://www.jetbrains.com/pycharm/download/))

To start, download VS Code from the following link: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

To be able to use python, we have to install a few extensions.
- Open VS Code and navigate to the extensions tab.
- Search for Python in the search bar
    - Install the Python Extension
    - Install the Python Debugger Extension

# Writing and running your first python script

We will now write our first python script. To do this, follow the next steps:

- Create a file called `HelloWorld.py`
- Write the following code
```py
print("Hello world! My name is <insert your name>")
```
- Save the file

Now that we have a python script, it is time to execute it. To run a python script, there are two ways of running the program.

We can run it from the terminal. We do this by entering the python command followed by the name of the file.
```bash
python ./01-Introduction-to-python/example/MyFirstScript.py
```

We can also run it from VS Code itself. To do this, locate the `Run python file` button when the python script is open. This will open a terminal and run the script.

# Congratulations
You have taken your first steps into becoming a python programmer. Follow the next chapter [Basics of python syntax](../02-Basics-of-python-syntax/02%20-%20Basics%20of%20python%20syntax.md) to continue your journey!