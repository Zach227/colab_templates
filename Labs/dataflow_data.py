import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "dataflow_lab",
    "intro_title": "Overview of the Lab",
    "intro_body": """
Because of how testbenches and Verilator works, it's important that you define all of your signals with the provided names and you define your modules with the provided names. 
If you used a different name you can change the name in Verilator but be careful.
You will implement 4 different functions. 
Each function will only be active when its button is pressed. 
If no button is pressed, the LEDs should show which switches are flipped.
Each function will take the input (switches) and change it. 
This will be displayed on the LEDs.
    """,
    "part1_title": "Function 1:",
    "part1_body": """
Down Button (btnd): Shift all the bits of the input to the left 3 times when you press the down button.
If the button is not pressed, the LEDs should show the value of the switches.
Input your code below for this function. 
When ready run it and it will be linted then tested. 
If it doesn't work, make changes and try again.
    """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "function1",

    "part2_exists": True,
    "part2_title": "Function 2:",
    "part2_body": """
Left Button (btnl): Using all 16 switches and LEDs, do a bitwise XOR with the left and right half of the input. 
Set the left half of the output to 0, and the right half as the result of the XOR
If the button is not pressed, the LEDs should show the value of the switches.
        """,
    "part2_wavedrom": True,
    "part2_testbench": True,
    "part2_sim_file": "function2",


    "part3_exists": True,
    "part3_title": "Function 3:",
    "part3_body": """
Down button (btnr): Implement the following function while btnr is high:  
![picture](https://raw.githubusercontent.com/anon36424/digital_design_colab/main/Dataflow/media/function3.png)

If btnr is low, then have the LED be equal to sw. A will be the first switch, B the second and C the third. 
F will be the first LED. If the button is not pressed, the LEDs should show the value of the switches.

Hint: `A = sw[0]`. You may also create intermediate signals if you prefer

    """,
    "part3_wavedrom": True,
    "part3_testbench": True,
    "part3_sim_file": "function3",

    "part4_exists": True,
    "part4_title": "Function 4:",
    "part4_body": """
Up Button btnu:  \n
The door to the digital design lab has an electronic lock. 
When someone swipes their ID card, it could be a student or a professor. 
If it is a student, and it is between 7am and 10pm, the door will unlock. 
If it is a professor, the door will open no matter what time it is. 
Implement this functionality when the up button is pressed.

**Inputs:**\n
Sw[0] - is student?  
Sw[1] - is professor?  
Sw[2] - 0 = am, 1 = pm  
Sw[6:3] - binary representation of the hour of the day  

**Output:**  
If the door unlocks, turn on all LEDs

**Note:** If the student input and the professor input are both high, the door should stay locked (this should not be possible—it is an imposter). 
If you receive an invalid time (ex: 15:00am) the door should also stay locked.

If the button is not pressed, the LEDs should show the value of the switches.
    """,
    "part4_wavedrom": True,
    "part4_testbench": True,
    "part4_sim_file": "function4",

    "top_module_title": "Bringing it together",
    "top_module_body": """
Now add all of your functions together. When a certain button is pressed it should implement that function. When no button is pressed, it the leds should show the value of the switches.

You will just combine all of your functions together.

The module should be called `dataflow_sv`
It should have `sw` as a 16 bit wide inputs.
It should have `btnl`, `btnd`, `btnr`, and `btnu` as single bit inputs.
It should have `led` as a 16 bit wide output

You will have to rename and refactor some of your inputs. For example, on Function 3, instead of having A, B, and C be inputs, you will need to assign them as intermediate signals:

```
assign A = sw[2];
assign B = sw[1];
assign C = sw[0];
```

This is because one input is mapped to one signal. You should use if/else if/else branches to switch between your 4 functions.

| Module Name: |dataflow_sv|||
| ----------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|btnd 	|Input 	|1| Activates Function1	|
|btnl 	|Input 	|1| Activates Function2	|
|btnr 	|Input 	|1| Activates Function3	|
|btnu 	|Input 	|1| Activates Function4	|
|sw 	|Input 	|16 |	The value of the switches|
|led| 	Output 	|16| The value to display on the LEDs|
""",
    "top_module_text2": True,
    "top_module_text2_type": "code",
    "top_module_title2": "Hint",
    "top_module_body2":
    """
%%html

<style>
div.warn {    
    color: #356A89;
    background-color: #D4EAF7;
    border-left: 5px solid #3C82E3;
    padding: 0.5em;
    }
 </style>
<div class=warn>
The module should be called dataflow. It should have sw as a 16 bit wide inputs. <br> 
It should have btnl, btnd, btnr, and btnu as single bit inputs. It should have led as a 16 bit wide output.
</div>
    """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "dataflow",

    "xdc_exists": True,
    "xdc_title": "XDC Files:",
    "xdc_body":
    """
XDC stands for Xilinx Design Constraints. 
The master XDC file  has each of the ports for input and output on the Basys3 board. 
The XDC file connects signals with physical hardware. 
This will be needed to bind signals to switches, LEDs and buttons.
Uncomment the lines containing `btnr`, `btnl`, `btnu`, and `btnd`. 
This tells the FPGA what input is linked to button.\n
***NOTE***: In future labs, if you're clever about how you name your signals in your top level module, you won't need to rename any signals in the .xdc but will just uncomment the lines that you need.\n
You will need to uncomment the lines that contain the button signals.\n
The lines look like this:  \n
`# set_property -dict { PACKAGE_PIN U18   IOSTANDARD LVCMOS33 } [get_ports { btnc }];`\n\n
Then run the codeblock to save your constraints file.
    """,

    "f4pga_exists": True,
    "download_exists": True,
    "download_body": 
    """
To Download it to the board you will need OpenOCD.
First create a folder to house the files on your local machine. 
Then download the OpenOCD configure file and the bitstream from this Notebook and add then to your folder (they will be in a zip file in /content/dataflow_sv.zip). 
On command line go into the folder and run the command\n
`openocd --file dataflow_sv.cfg`\n
It should only take a few moments to download to the board.
    """,

    "top": "dataflow_sv",
    "folder": "Dataflow_SV",
    "files": "Makefile xdc.xdc dataflow.sv",

    "next_lesson": "twos_compliment",
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