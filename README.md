Files Included
1. # Openfile.py:
Creates input.txt and writes five lines of sample text into it.

2. # filemodifier.py:
Reads input.txt, converts its content to uppercase, counts the words, and writes the result into output.txt.

3. # input.txt:
The sample input file with five lines of text.

4. # output.txt:
Output from filemodifier.py — shows the uppercase content and word count.

5. # modified_input.txt:
Output from the user-interactive script that asks for a filename, reads its content, and writes a modified (uppercase) version with proper error handling.             

Key Concepts Used
with open() to safely read/write files.

file.read() and file.write() for content processing.

Error handling with try, except, FileNotFoundError, and PermissionError.

os.path.exists() to check file existence before reading.

Simple word counting using split().
