import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "stopwatch_lab",
    "intro_title": "Stopwatch",
    "intro_body": """
### Frequency Vs Period\n
Frequency is the number of times something occurs in a given time frame, while period is the amount of time it takes for something to occur. They are inverses of one another. 
        """
        r"""
$Period = \\frac{1}{Frequency}$ and $Frequency = \\frac{1}{Period}$.\n
        """
        """
This is important when dealing with Clocks in circuits.\n
Example:  \n
You are running around a pillar while playing tag.\n
You run around it 3 times every minute. That is your frequency.\n
The period would be 
        """
r"$\\frac{1}{Frequency}$"
        """
        , so every 1/3 of a minute or 20 seconds you would complete a circle. This is the period.\n
So why does Frequency and Period matter?\n
Timing is very important because of the FPGAs built in clock. The clock keeps all elements in the circuit working together and prevents conflicts.
In this lab, inorder to create a stopwatch, you will need to know how many clock cycles occur in a given time frame, then after counting that many, increment the stopwatch.
        """,
    "part1_title": "The Counter Module",
    "part1_body": r"""
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/stopwatch_lab/media/mod_counter.png"\n
width="400" height="150" style="display: block; margin: 0 auto " />\n
<br>
| Module Name: | mod_counter|||\n
| -- --------- | ----------- |--|--|\n
| Port Name      | Direction       |Width|Function|\n
|reset \t|Input \t|1| Active high reset|\n
|clk \t|Input \t|1| Clock used for timing|\n
|increment \t|Input \t|1 | should only increment when enable if its high|\n
| MOD_VALUE|\tParameter| \tN/A| Value at which counter should reset, default of 10 \t|\n
| rollover\t|Output \t|1| \tHigh for one cycle when counter rolls over|\n
|count| \tOutput \t|4| \tCurrent value of the counter|\n\n\n
<br>
        """
        """
"When increment is high, the counter should begin increasing. 
When it reaches the MOD_VALUE, it should reset to zero and rollover should be high for that clock cycle.
        """,
    "part1_wavedrom": False,
    "part1_testbench": False,
    "part1_sim_file": "mod_counter",

    "part2_exists": True,
    "part2_title": "The Stopwatch Module",
    "part2_body": r"""
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/stopwatch_lab/media/stopwatch_module.jpg"\n
width="500" style="display: block; margin: 0 auto " />\n<br><br>\n\n
| Module Name: | stopwatch |||\n
| -- --------- | ----------- |--|--|\n
| Port Name      | Direction       |Width|Function|\n
|clk \t|Input \t|1| The Clock Signal|\n
|reset \t|Input \t|1| Active high reset|  \n
|run \t|Input \t|1 | High when timer should be running|\n
| digit0\t|Output \t|4| The value of the hundredths of a second digit|\n
| digit1\t|Output \t|4| The value of the tenths of a second digit|\n
| digit2\t|Output \t|4| The value of the seconds digit|\n
| digit3\t|Output \t|4| The value of the tens of seconds digit|\n\n<br>\n\n
        """
        """
You will  have to create a separate counter. This one will reset and give a rollover value every .01s. 
This cannot be an instantiation of `mod_counter` because its `count` value will be wider than 4 bits. 
This `rollover` will be fed into `digit0` as the `increment`.\n
You will also have to instantiate 4 different instances of `mod_counter`, `digit0` through `digit3`.\n
When `digit0` reaches 9 it should increment `digit1` and go back to `0`. So on for all 4 digits. `digit3` should rollver at `5` (60 seconds in a minute after all)
        """,
    "part2_wavedrom": False,
    "part2_testbench": False,
    "part2_sim_file": "stopwatch",


    "part3_exists": False,
    "part3_title": "",
    "part3_body": """
text goes here
    """,
    "part3_wavedrom": True,
    "part3_testbench": True,
    "part3_sim_file": "",

    "part4_exists": False,
    "part4_title": "",
    "part4_body": """
text goes here
        """,
    "part4_wavedrom": True,
    "part4_testbench": True,
    "part4_sim_file": "",

    "top_module_title": "Tope Level Module",
    "top_module_body": r"""
# Top Level Module\n
| Module Name: | stopwatch_top|||\n
| -- --------- | ----------- |--|--|\n
| Port Name      | Direction       |Width|Function|\n
|clk \t|Input \t|1| The Clock Signal |\n
| btnc \t|Input \t|1 | Active High Reset|\n
| sw\t|Input \t|1| High when stopwatch should be running |\n
| anode\t|Output \t|4| Seven-segment anode values, from Seven-Segment Controller|\n
| segment\t|Output \t|8| Seven-segment segment values,  from Seven-Segment Controller|  \n\n
        """
        """
The `clk` signal is defined in the XDC.\n
When `btnc` is pressed, the stopwatch should go to `0` for all digits.\n
While the switch is high, the stopwatch should begin to increment. 
You should time it with a different stopwatch to make sure that your stopwatch is keeping accurate time.\n
You can concatenate the 4 digits together to create the `datain` signal for `SevenSegmentControl`.\n\n
NOTE: We are giving you the Seven Segement Control Module. 
This allows you to show 4 unique digits by quickly alternativing between the 4 different valuse faster than your eyes can see.\n\n   
* `dataIn`: 16 bits, each 4 bits are a hex value which is shown as a digit.\n
* `digitDisplay`: 4 bits, if you want all 4 digits, pass `1111` into it.\n
* `digitPoint`: This determines which digit point is on.\n
* `anode`: Hook this up to the output `anode` signal\n
* `segment`: Hook up to the output `segment` signal\n
* `reset`, and `clk`: Self-explanatory inputs\n
        """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "stopwatch_top",

    "xdc_exists": False,
    "xdc_title": "",
    "xdc_body":
    """
text goes here
        """,

    "f4pga_exists": True,
    "download_exists": True,
    "download_body": 
    """
You can use this configuration file and the program openOCD to download the bitstream to your board. 
You will need to download this file and the bitstream to your local machine.
        """,

    "top": "stopwatch_top",
    "folder": "Stopwatch",
    "files": "mod_counter.sv stopwatch.sv stopwatch_top.sv",

    "next_lesson": "state_machine_lab",
}

def get_data():
    for key in data:
        if "body" in key:
            data[key]=data[key].replace('"', '\\"')
            data[key]=data[key].replace('\\s', '\\\\s')
            data[key]=data[key].splitlines()
        if "questions" in key:
            for question in data[key]:
                i = 0
                for line in question.title:
                    line=line.replace('"', '\\"')
                    question.title[i] = line
                    i+=1
    return data

