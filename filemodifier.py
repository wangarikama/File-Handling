def modify_file():
    filename= input("Enter the name of the file to read: ")
    try:
        #read input file
        with open(filename, 'r') as infile:
            content = infile.read()

           #modify the content
            modified_content = content.upper()

            #create a new output file
            output_file = 'modified_' + filename
            with open(output_file, 'w') as outfile:
                outfile.write(modified_content)
            print(f"File modified successfully. Output written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {filename}.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
#run the program
modify_file()