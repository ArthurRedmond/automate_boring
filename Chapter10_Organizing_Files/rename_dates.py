"""Renames filenames with American MM-DD-YYYY format to European DD-MM-YYYY"""

import shutil, os, re

# Create a regex that matches the files with the American date format (MM-DD-YYYY).
datePattern = re.compile(r"""^(.*?)         # all text before the date
                         ((0|1)?\d) -       # one or two digits for the month
                         ((0|1|2|3)?\d) -   # one or two digits for the day
                         ((19|20)\d\d)      # four digits for the year
                         (.*?)$             # all text after the date
                         """, re.VERBOSE)

# Loop over teh files in the working directory.
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName) # 'mo' match object
    
    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFileName}" to "{euroFilename}"...')
    #shutil.move(amerFileName, euroFilename) # uncomment after testing