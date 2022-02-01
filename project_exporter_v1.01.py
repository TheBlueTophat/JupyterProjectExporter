# Version: 1.01
# This project is under the MIT open license. Do what you will with it.
#
# WARNING: Use at your own risk, I am not responsible if this overwrites or corrupts work. It shouldn't harm work, due to the way it works and from what I've tested, but if you 
# are concerned duplicate your work before running the program.
# 
# WARNING 2: The output file this program creates will overwrite an existing copy if one exists. *This is fine in most use cases* but please keep this in mind in case you change the # output file afterwards, if you need to run the exporter again.
#
# This program exports a .py file (or alternatively a .R file) comtaining all of the code cells, as well as all of the markdown cells from a given Jupyter notebook, in a (somewhat) 
# neatly ordered manner. This program will only work when ran in the terminal/command line. It is not set up to be ran as a stand alone program since you need to pass arguments to it # through the command line.
# 
# The output will be in the same folder as the project file. 
# 
# The exported file's name will be the same as the given file's name, except with "_py" added to the end (or "_r" if it's an R file), as well as the file type changed to ".py" (or,
# again, ".R" depending on the option you choose).
# 
# Try to avoid using funky folder names (e.g. nontypical characters, spaces) since this program likely will not work with them.
#
# There are two arguments for the program:
# argument 1: this is the file path for the project file you're trying to export
# argument 2 (optional): this is the type of file export you want to do. The options are py-mode (default if left blank) to exporgt a .py file, and r-mode for a .R file
#
# You can run this program by opening the terminal and typing in:
# python <full file path to where this program is saved> <argument 1: full file path of your project file> <argument 2 (optional): py-mode or r-mode>
#
# Example usage:
# python spring-2022/project_exporter/project_exporter_v1.01.py spring-2022/project_exporter/demo_v1.01.ipynb
# 
# - This would create a file in spring-2022/project_exporter/ named "demo_py.py"
#
# Pages I used to piece this code together
# - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# - https://stackoverflow.com/questions/17544307/how-do-i-run-python-script-using-arguments-in-windows-command-line
# - https://www.geeksforgeeks.org/read-json-file-using-python/
# - https://nbformat.readthedocs.io/en/latest/format_description.html
# - https://www.geeksforgeeks.org/reading-writing-text-files-python/
# - https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
# - https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python
# - https://stackoverflow.com/questions/42798967/how-to-subtract-strings-in-python/42799034

import sys # Used for accepting arguments from the command line.
import json # Used for parsing the Jupyter notebooks.
import os.path # Used to check if file paths exist
from os import path # Used to manupulate the file path

projectPath = ''

argNum = len(sys.argv) # Tracks the number of arguments passed

export_mode = 'py-mode'

# Error checking in case the project path given is incorrect or nonexistent
if(argNum >= 2):
    projectPath = sys.argv[1] # The file path for the project file to convert. The first argument ([0]) is the program's name so I need to use the second argument.

# Same idea, error checking to make sure there's enough arguments for detecting the mode to run in (or to default to python mode if option left blank)
if(argNum >= 3):
    if(sys.argv[2] == 'py-mode' or sys.argv[2] == 'r-mode' or sys.argv[2] == ''):
        export_mode = sys.argv[2]
    else:
        sys.exit("Improper export mode: " + export_mode + "\nPlease choose either r-mode, py-mode, or leave this argument blank (py-mode by default).")

# Exits the program if the path to the project does exist or is incorrect/not a proper file path.
if(not path.exists(projectPath)):
   sys.exit("The file path for your project: \"" + projectPath + "\" does not exist or is not accessible.")

file = open(projectPath) # Opens the project file and stores it as an object.

newPath = projectPath.replace('.ipynb', '_py.py') # Generates the new path/file name.

if(export_mode == 'r-mode'):
    newPath = projectPath.replace('.ipynb', '_r.R') # Generates an alternative path if r-mode is selected.

notebookData = json.load(file) # Loads the Jupyter notebook data. Apparently its the same as loading .json data, which makes this very easy.

buffer = [] # This is an array that stores every line of text (whether code or actual text) from each cell. At the end, all of its contents get written into a file.

prevType = '' # As the code loops through the notebook cells, this keeps track of the previous type of cell (either "code" or "markdown").

# This loops through every cell in the notebook and loads in each line of text into "buffer" (with some formatting for readibility).
# Apparently Jupyter notebooks store each cell's data as a list of dictionaries (one for each cell).
# "index" keeps track of the integer index corresponding to each cell, "cell" corresponds to the dictionary of each cell itself.
for index, cell in enumerate(notebookData["cells"]):
    if(cell["cell_type"] == "code"):
        for j in cell["source"]: # Source is the dictionary key for the actual cell content  
            buffer.append(j)
            
        buffer[-1] = buffer[-1] + '\n\n' # Postpends 2 newlines, since one does not come at the end of the blocks by default. Theres two so that theres a newline of blank space between the code and the text.
            
    elif(cell["cell_type"] == 'markdown'):
        for j in cell['source']:
            buffer.append(j)
            
            # Prepends a "#" to comment out markdown cells. This does not add a "#" at the start if the block already starts with one (such as in the markdown for headers).
            if(not j.startswith("#")):
                buffer[-1] = '# ' + buffer[-1] # Adds a hashtag and space to the very start of each line of text.
            elif(index > 2): # Checks index for formatting purposes.
                buffer[-2] = buffer[-2] + '\n\n' # Postpends newlines to previous cell between this block (a markdown block) and the previous one (also a markdown block).

        buffer[-1] = buffer[-1] + '\n\n' # Postpends a newline for readibility's sake. There is only one here because the markdown cells are formatted slightly differently by the code.

    prevType = cell["cell_type"]
        
newFile = open(newPath, "w") # Creates/opens the output file.

# Dumps every line of the buffer into the new file.
for line in buffer:
    newFile.writelines(line)

# CLoses up everything.
file.close() # Closes file
newFile.close()

# Lets user know the program worked and the new file's path.
print('File export complete. The new file is available at: ' + newPath)
