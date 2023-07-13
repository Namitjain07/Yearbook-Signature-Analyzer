# Yearbook Signature Analyzer
    This program determines the students with the most and least signatures in a yearbook, based on the input data provided in a file. The program reads the file, creates a dictionary representing the yearbook, and then calculates the students with the most and least signatures.

## Input Format

The input file should follow this format:
```python

name1:
name2, 1
name3, 0
name4, 1
...
name2:
name1, 0
name3, 0
name4, 0
...

```

Each student's entry starts with their name followed by a colon (":"). After that, each line contains another student's name and their signature status. The status is represented by "1" for signed and "0" for not signed. The data is provided for all graduating students.


## Program Execution


    1. initially, manually create a dictionary yearbook in the program code. The dictionary should have the following structure: yearbook = {name1: {...}, name2: {...}, ...}. The nested dictionaries represent each student's signatures.
    2. The program reads the input file and populates the yearbook dictionary accordingly.
    3. It calculates the students with the most and least signatures by iterating over the yearbook dictionary and counting the number of signed entries for each student.
    4. If there are multiple students with the most or least signatures, the program will print all of them.
    5. The program writes the results to an output file named output.txt. The file will contain the students with the most signatures on one line and the students with the least signatures on the next line.

## Example Output
    The program writes the results to an output file named output.txt. The file will contain the students with the most signatures on one line and the students with the least signatures on the next line.
```python

Most signatures: name1, name3
Least signatures: name2

```

In this example, 
- name1
 and 
- name3
 have the most signatures, while name2 has the least.

Please make sure to provide the input data in the correct format and update the program's code to include the yearbook dictionary before executing it.