import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "seven_segment_lab",
    "intro_title": "The Lab",
    "intro_body": """
In this lab, given a binary value, display the equivalent Hexadecimal character.
So if we input `0000` we want to output `0` and if we input `1100` we want to output `A`.
        """,

    "part1_exists": True,
    "part1_title": "Seven Segment Module",
    "part1_body": """
| Module Name: |seven_segment|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
| data	|Input 	|4| data to display|
|segment 	|Output 	|7 | Cathode signals to the display|
        """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "seven_segment",

    "part2_exists": False,
    "part2_title": "",
    "part2_body": """
part 2 text goes here
        """,
    "part2_wavedrom": True,
    "part2_testbench": True,
    "part2_sim_file": "",


    "part3_exists": False,
    "part3_title": "",
    "part3_body": """
part 3 text goes here
    """,
    "part3_wavedrom": True,
    "part3_testbench": True,
    "part3_sim_file": "",

    "part4_exists": False,
    "part4_title": "",
    "part4_body": """
part 4 text goes here
        """,
    "part4_wavedrom": True,
    "part4_testbench": True,
    "part4_sim_file": "",

    "top_module_title": "The Top Module",
    "top_module_body": """
| Module Name: |seven_segment_top|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
| sw	|Input 	|4| Input to drive seven-segment decoder |
| btnc	|Input 	|1| Will turn on digit point |
| segment	|Output 	|8 | Cathode signals to the display including the point|
| anode	|Output 	|4 | Anode signals for each of the four digits on the display|  

<br>  
This figure shows what is happening in the module. 
<br>  <br>

![picture](https://raw.githubusercontent.com/anon36424/digital_design_colab/main/SevenSegment/media/seven_top.jpg)
        """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "seven_segment_top",

    "xdc_exists": True,
    "xdc_title": "XDC File",
    "xdc_body":
    """
In the xdc file below, uncomment the lines corresponding to the FPGA I/O that you are using. Then run the code block to create your xdc file.
        """,

    "f4pga_exists": True,
    "download_exists": True,
    "download_body": 
    """
You can use this configuration file and the program openOCD to download the bitstream to your board. 
You will need to download this file and the bitstream to your local machine.
        """,

    "top": "seven_segment_top",
    "folder": "Seven_Segment",
    "files": "Makefile xdc.xdc seven_segment.sv seven_segment_top.sv",

    "next_lesson": "sequential_logic",
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].replace('\\s', '\\\\s')
            data[key]=data[key].replace('\n', '\\n')
            data[key]=data[key].replace('\t', '\\t')
            data[key]=data[key].replace('\frac', '\\\\frac')
            data[key]=data[key].splitlines()
    return data