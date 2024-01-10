# alias-echo
Python program that echos the aliases of a .zshrc file. Using add or remove arguments will add or remove aliases from the .zshrc file.

## Requirements
python3: [Download](https://www.python.org/downloads/)

## Usage
Copy the contents of the main.py file into a file somewhere reliable on your computer.

Use your terminal to find your terminal's configuration file. For example, if you use zsh, you can find your configuration file by typing `nano ~/.zshrc` into your terminal.

Add an alias to your configuration file that points to the main.py file. For example, if you copied the main.py file to your home directory, you can add the following line to your configuration file: `alias shortcuts="python3 ~/main.py"`. 

Reload your configuration file by typing `source ~/.zshrc` into your terminal.

You can now type `shortcuts` into your terminal to see a list of your aliases.

