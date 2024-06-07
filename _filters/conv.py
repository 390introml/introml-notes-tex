import subprocess
import os

# Get the current working directory (current folder)
BASE = os.getcwd()


def add_macro(name):
    if name == "top":
        return f"{BASE}/tex/top"

    with open(f"{BASE}/tex/{name}.tex", "r") as main_file:
        main_content = main_file.read()
        # main_content = main_content.replace("Eq.~\\ref", "eeqref")
    with open(f"{BASE}/tex/macros.tex", "r") as macro_file:
        macro_content = macro_file.read()

    with open(f"{BASE}/tex/combined.tex", "w") as output_file:
        output_file.write(macro_content + main_content)
    return f"{BASE}/tex/combined"


# Function to run a command-line command
def run_command(filename):
    # if not in_file:
    # in_file = "lecture" + str(in_seq)
    # pandoc input.tex -o output.md --filter=myfilter.py
    outfile = f"{BASE}/notes/{filename}.md"

    command = f"cd {BASE}/tex; pandoc -f latex -t markdown -s {add_macro(filename)}.tex -o {outfile} --extract-media {BASE}/static/img/"
    if filename != "top":
        command += f"; rm {BASE}/tex/combined.tex"
    try:
        # Run the command and capture the output
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(output)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during command execution
        print(f"Command execution failed with error code {e.returncode}:")
        print(e.output)

    # Read the file
    with open(f"{outfile}", "r") as file:
        content = file.read()

    # Replace double dollar signs with your desired text (e.g., <replacement>)
    content = content.replace("$$", "\n$$\n")
    content = content.replace(f"{BASE}/static", "")
    content = content.replace("aligned", "align")
    content = content.replace(r"\_zero_new:N \_\_prg_map_int", "")
    # Write the modified content back to the file
    with open(f"{outfile}", "w") as file:
        file.write(content)


# replacement = f"sed -e 's/\$\$/+++___DOUBLE_DOLLAR___+++/g' {outfile} > temp.md"
# try:
#     subprocess.check_output(replacement, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
# except subprocess.CalledProcessError as e:
#     # Handle any errors that occurred during command execution
#     print(f"Replacement execution failed with error code {e.returncode}:")
#     print(e.output)

# replacement = f"sed -e 's/___DOUBLE_DOLLAR___/\n\$\$\n/g' temp.md > {outfile}"
# try:
#     subprocess.check_output(replacement, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
# except subprocess.CalledProcessError as e:
#     # Handle any errors that occurred during command execution
#     print(f"Replacement execution failed with error code {e.returncode}:")
#     print(e.output)

# Example usage
name = "intro"

run_command(name)
