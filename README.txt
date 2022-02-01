Version: 1.01
This project is under the MIT open source license. Do what you will with it.
This project is for the benefit of one of my classes. If you are stumbling upon this program randomly and are not from the class it may not work as you expect.

WARNING: Use at your own risk, I am not responsible if this overwrites or corrupts work. It shouldn't harm work, due to the way it works and from what I've tested, but if you 
are concerned duplicate your work before running the program.

WARNING 2: The output file this program creates will overwrite an existing copy if one exists. *This is fine in most use cases* but please keep this in mind in case you change the output file afterwards, if you need to run the exporter again.

This program exports a .py file (or alternatively a .R file) comtaining all of the code cells, as well as all of the markdown cells from a given Jupyter notebook, in a (somewhat) 
neatly ordered manner. This program will only work when ran in the terminal/command line. It is not set up to be ran as a stand alone program since you need to pass arguments to it through the command line.

The output will be in the same folder as the project file. 

The exported file's name will be the same as the given file's name, except with "_py" added to the end (or "_r" if it's an R file), as well as the file type changed to ".py" (or,
again, ".R" depending on the option you choose).

Try to avoid using funky folder names (e.g. nontypical characters, spaces) since this program likely will not work with them.

There are two arguments for the program:
argument 1: this is the file path for the project file you're trying to export
argument 2 (optional): this is the type of file export you want to do. The options are py-mode (default if left blank) to exporgt a .py file, and r-mode for a .R file

You can run this program by opening the terminal and typing in:
python <full file path to where this program is saved> <argument 1: full file path of your project file> <argument 2 (optional): py-mode or r-mode>

Example usage:
python spring-2022/project_exporter/project_exporter_v1.01.py spring-2022/project_exporter/demo_v1.01.ipynb

- This would create a file in spring-2022/project_exporter/ named "demo_py.py"

Pages I used to piece this code together
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://stackoverflow.com/questions/17544307/how-do-i-run-python-script-using-arguments-in-windows-command-line
- https://www.geeksforgeeks.org/read-json-file-using-python/
- https://nbformat.readthedocs.io/en/latest/format_description.html
- https://www.geeksforgeeks.org/reading-writing-text-files-python/
- https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
- https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python
- https://stackoverflow.com/questions/42798967/how-to-subtract-strings-in-python/42799034
