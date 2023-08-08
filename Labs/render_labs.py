
import jinja2
import gates_data
import dataflow_data
import arithmetic_data
import seven_segment_data
import stopwatch_data
import state_machine_data

notebooks = [(gates_data, "gates_lab"), (dataflow_data, "dataflow_lab"), (arithmetic_data, "arithmetic_lab"), 
    (seven_segment_data, "seven_segment_lab"), (stopwatch_data, "stopwatch_lab"), (state_machine_data, "state_machine_lab")]


for notebook in notebooks:
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "lab_template.txt"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(notebook[0].get_data())

    text_file = open("{}.ipynb".format(notebook[1]), "w")
    text_file.write(outputText)
    text_file.close()