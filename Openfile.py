#create input.txt file with some content
with open('input.txt', 'w') as file:
    file.write("I love coding.\n")
    file.write("python is fun.\n")
    file.write("Plp is the best.\n")
    file.write("I enjoy learning new programming languages.\n")

def process_file(input_file , output_file):
    try:
        #read input file
        with open(input_file, 'r') as infile:
            content = infile.read()

            #count words 
            word_count = len(content.split())

            #convert to uppercase
            content_upper = content.upper()

            #write output
            with open(output_file, 'w') as outfile:
                outfile.write("PROCESSED TEXT:\n")
            outfile.write(content_upper + "\n")
            outfile.write(f"\nWORD COUNT: {word_count}\n")
               
        print(f"File processed successfully. Output written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"unexpected Error: {e}")

        #run the function
process_file('input.txt', 'output.txt')