import os
import json
import re
from jinja2 import *

file_name = "boolean_algebra.ipynb"
with open(file_name, "r") as f:
    try:
        json_str = f.read()
        # parse the json string into a Python object
        python_dict = json.loads(json_str)
        # do something with the json data
        # print(json_data)
        i = 0
        import_list = set()
        source_list = []
        import_exists = False
        skip = []
        for key in python_dict["cells"]:
            # Check for import(
            for line in python_dict["cells"][i]["source"]:
                # print(line)
                if type(line) != str:
                    continue
                # if line.find("import(") != -1 and (i > 2):
                #     import_exists = True
                # print("Import exists ", line)
                if len(line) > 15 and line.find("import_text") != -1:
                    x = line.find("(")
                    y = line.find(")")
                    # import_exists = True
                    print(line[x + 2 : y - 1])
                    if line[x + 1] == '"' and line[y - 1] == '"':
                        print(line[13:-4])
                        import_list.add(line[x + 2 : y - 1])
                        print(import_list)
                        skip.append(i)
                    print("Import exists ", line)

            if not i or i == 1:
                # Rewrite the setup block so that the first cell and setup cells are combined.
                # Set up the setup block
                # Add the setups every notebook uses
                # Make it one block
                # Add in template to close the first setup block
                # Errors to catch/Things to change
                # Everything needs a title, if it doesn't have a title, add one. (Code block)
                # Resize the first  to have consistent sizing (Markdown )
                #
                pass
            elif import_exists is True:
                raise Exception(
                    "Invalid Import found in "
                    + " cell.\n Imports are only valid in the first and second cell\n"
                )
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
                    '"' + tempLine.replace("\\", "\\\\").replace('"', '\\"') + '",'
                )
            if cell_string and cell_string[-1] == ",":
                cell_string = cell_string[:-1]
            cells[i] = (cell_type, cell_string)
            i += 1
        import_list = list(import_list)
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("cell.txt")
        content = template.render(cells=cells, import_list=import_list)
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
