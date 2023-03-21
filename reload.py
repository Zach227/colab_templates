import os
import json
from jinja2 import Environment, FileSystemLoader

# define the directory to search for json files
dir_path = "/home/wms29/digital_design_colab2/Exercises"
print(dir_path)
# loop through all subdirectories and files in the directory
for root, dirs, files in os.walk(dir_path):
    print(root, dirs, files)
    for file_name in files:
        # check if the file is a json file
        if file_name.endswith(".ipynb"):
            notebook_name = file_name[0:-6]
            # construct the full path to the file
            file_path = os.path.join(root, file_name)
            # read the json data from the file into a string
            with open(file_path, "r") as f:
                try:
                    json_str = f.read()
                    # parse the json string into a Python object
                    python_dict = json.loads(json_str)
                    # do something with the json data
                    i = 0  # position in array of cells
                    import_list = set()  # Set of packages to import using import_text()
                    source_list = []  # List of the contents of the relevant blocks
                    skip = []  # Lines to skip?
                    for key in python_dict["cells"]:
                        skipping = False  # If there is an import in a block of code, we don't want to duplicate it
                        # Check for import_text(
                        for line in python_dict["cells"][i]["source"]:
                            # If the current object isn't a string, skip it
                            if type(line) != str:
                                continue
                            if (
                                len(line) > 15 and line.find("import_text") != -1
                            ):  # Only check it if its long enough to contain an import text
                                x = line.find("(")
                                y = line.find(")")
                                if line[x + 1] == '"' and line[y - 1] == '"':
                                    import_list.add(line[x + 2 : y - 4])
                                    print(import_list)
                                    skip.append(i)
                                    skipping = True
                                print("Import exists ", line)
                            if line.find("**Setup**") != -1:
                                print("SKIPPING " + line)
                                skipping = True
                            if line.find("from ipywidgets") != -1:
                                print("SKIPPING " + line)
                                skipping = True
                        if skipping is True:
                            skipping = False
                            pass
                        else:
                            # Skip the setup
                            # First block in array will be a Intro block
                            # Title then followed by Markdown
                            source_list.append(
                                (
                                    python_dict["cells"][i]["cell_type"],
                                    python_dict["cells"][i]["source"],
                                )
                            )
                        i += 1
                    cells = source_list
                    i = 0
                    for cell in cells:
                        #     if i in skip:
                        #         continue
                        if type(cell[0]) == dict:
                            print("NOT A CELL")
                            continue
                        # If the cell is empty, skip
                        # print(cell)
                        cell_type = '"' + cell[0] + '"'
                        cell_string = ""
                        for line in cell[1]:
                            if len(line) == 0:
                                continue
                            if line[-1] == "\n":
                                tempLine = line[0:-1]
                            else:
                                tempLine = line
                            cell_string += (
                                '"'
                                + tempLine.replace("\\", "\\\\").replace('"', '\\"')
                                + '",'
                            )
                        if cell_string and cell_string[-1] == ",":
                            cell_string = cell_string[:-1]
                        cells[i] = (cell_type, cell_string)
                        i += 1
                    import_list = list(import_list)
                    environment = Environment(loader=FileSystemLoader("templates/"))
                    template = environment.get_template("cell.txt")
                    content = template.render(
                        cells=cells,
                        import_list=import_list,
                        notebook_name=notebook_name,
                    )
                    filename = "/home/wms29/testing/notebook/" + file_name
                    directory = "/home/wms29/testing/notebook"
                    filename = file_name
                    filepath = os.path.join(directory, filename)
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    with open(filepath, mode="w") as f:
                        f.write(content)
                        print(f"... wrote {filename}")
                    print(import_list)
                except Exception as e:
                    print("Invalid Notebook format for exercise", e)
