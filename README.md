Parse Maplestory Map.wz files to extract important information about all elements (objects, npcs, background etc...)

# Limbs' XML Parser:
This is a Python script that parses XML files and extracts specific information from them. Specifically, it looks for string elements in the XML file and outputs information based on the element's name and attributes.

# Features:
- XML File Parser
- XML File Comparer
---
Diff: (XML File Comparer)

    In this script, the file compare button is used generate a unified diff of the two files and display it in the output text box of the GUI. 
    The diff is displayed with the filename at the top of the output, followed by the differences between the two files. 
    The added and deleted lines are indicated with a + and - respectively, and the modified lines are indicated with both symbols. 
    The context lines are displayed with a space at the beginning of the line.

# How to Use:
---
    (Use the packed executable located in the dist folder)
    or
    - Clone this repository to your local machine
    - Install the required Python packages by running pip install -r requirements.txt in your terminal
    - Run the script by running python main.py in your terminal
    - Select the XML file you want to parse using the file dialog that appears
    - The script will output the parsed information in the text box on the GUI

# Dependencies:
This script requires the following Python packages:

- tkinter for the GUI
- xml.etree.ElementTree for parsing the XML files

# Future Improvements:
Some possible improvements to this script include:

Adding more options for output formatting (e.g. JSON, CSV)
Allowing the user to specify which elements they want to extract
Adding error handling for invalid XML files
# License:
This script is licensed under the MIT License. See LICENSE for more information.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# Credits:
This script was created by Limbs. If you have any questions or feedback, feel free to contact me on discord @Limbs#1915


