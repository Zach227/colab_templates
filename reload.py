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
            # construct the full path to the file
            file_path = os.path.join(root, file_name)
            # read the json data from the file into a string
            with open(file_path, "r") as f:
                try:
                    json_str = f.read()
                    # parse the json string into a Python object
                    python_dict = json.loads(json_str)
                    # do something with the json data
                    # print(json_data)
                    i = 0
                    source_list = []
                    for key in python_dict["cells"]:
                        
                        if(not i or i == 1 ):
                            #Set up the setup block
                            #Add the setups every notebook uses
                            #Make it one block
                            #Add in template to close the first setup block
                        # Errors to catch/Things to change
                        # Everything needs a title, if it doesn't have a title, add one. (Code block)
                        # Resize the first  to have consistent sizing (Markdown )
                        # 
                        else if python_dict["cells"][i]["source"].find("import ") is not -1:
                                raise Exception("Invalid Import found in " +str(i+1) + " cell.\n Imports are only valid in the first and second cell\n")    
                        else:
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
                        cell_type = '"' + cell[0] + '"'
                        cell_string = ""
                        for line in cell[1]:
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
                    environment = Environment(loader=FileSystemLoader("templates/"))
                    template = environment.get_template("cell.txt")
                    content = template.render(cells=cells)
                    filename = "/home/wms29/testing/notebook/" + file_name
                    directory = "/home/wms29/testing/notebook"
                    filename = file_name
                    filepath = os.path.join(directory, filename)
                    print(filename)

                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    with open(filepath, mode="w") as f:
                        f.write(content)
                        print(f"... wrote {filename}")
                except:
                    print("Invalid Notebook format for exercise")
