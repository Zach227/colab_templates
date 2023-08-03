import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "",
    "intro_title": "",
    "intro_body": """
text goes here
        """,
    "part1_title": "",
    "part1_body": """
text goes here
        """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "",

    "part2_exists": True,
    "part2_title": "",
    "part2_body": """
text goes here
        """,
    "part2_wavedrom": True,
    "part2_testbench": True,
    "part2_sim_file": "",


    "part3_exists": True,
    "part3_title": "",
    "part3_body": """
text goes here
    """,
    "part3_wavedrom": True,
    "part3_testbench": True,
    "part3_sim_file": "",

    "part4_exists": True,
    "part4_title": "",
    "part4_body": """
text goes here
        """,
    "part4_wavedrom": True,
    "part4_testbench": True,
    "part4_sim_file": "",

    "top_module_title": "",
    "top_module_body": """
text goes here
        """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "",

    "xdc_exists": True,
    "xdc_title": "",
    "xdc_body":
    """
text goes here
        """,

    "f4pga_exists": True,
    "download_exists": True,
    "download_body": 
    """
text goes here
        """,

    "top": "",
    "folder": "",
    "files": "",

    "next_lesson": "",
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].replace('\\s', '\\\\s')
            data[key]=data[key].replace('\t', '\\t')
            data[key]=data[key].replace('\frac', '\\\\frac')
            data[key]=data[key].splitlines()
        if "questions" in key:
            for question in data[key]:
                i = 0
                for line in question.title:
                    line=line.replace('"', '\\"')
                    question.title[i] = line
                    i+=1
    return data

