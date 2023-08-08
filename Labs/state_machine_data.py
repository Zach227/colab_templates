import random
import string

class Question:
    def __init__(self, title, code):
        self.title = title
        self.code = code


data = {
    "notebook_dir": "state_machine_lab",
    "intro_title": "One Shot",
    "intro_body": """
One large problem when dealing with inputs is that they are read every single cycle.
It is impossible to press a button for a single clock cycle. So if we press the button
it may be pressed for thousands of clock cycles. This is where a one shot helps us.

It only reads the button press for cycle. 
It does this by converting the button into a different signal which after one cycle goes low. 
Releasing and pressing again can reset the oneshot.
One Shot should have 3 states, IDLE, ONESHOT, WAIT.  

IDLE: Waiting for an input. When in goes high, transitions to ONESHOT.

ONESHOT: Input received, out is high for one cycle. Goes to WAIT.

WAIT: Waits for the input to go low. Out is low. When out goes to low, transitions to IDLE.

| Module Name: | OneShot |||
| -- --------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
| reset \t|Input \t|1| Active high reset|
| in \t|Input \t|1| Signal to One Shot|
| out |Output |1| One Shot signal|
| clk \t|Input \t|1| Clock Signal |
        """,

    "part1_exists": False,
    "part1_title": "",
    "part1_body": """
text goes here
        """,
    "part1_wavedrom": True,
    "part1_testbench": True,
    "part1_sim_file": "",

    "part2_exists": False,
    "part2_title": "",
    "part2_body": """
text goes here
        """,
    "part2_wavedrom": True,
    "part2_testbench": True,
    "part2_sim_file": "",


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

    "top_module_title": "Safe Combination State Machine",
    "top_module_body": """

For this lab you will design a combination lock state machine.
States:  

<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab/main/State_Machine/media/StateDiagram.svg"
width="500" height="300" style="display: block; margin: 0 auto " />
<br>

Intermediate Signals:  
CODE: If the correct code for the current state is input, then CODE is high, else, CODE is low.  
Q: If any button is pressed, Q is high. This represents entering the code.  


State Machine:  

IDLE: The state machine will wait for BTNC to be pressed.

COMBINATION_ONE: IF Q is low, nothing happens. If Q is High and Code is high, the correct code has been entered and go to next state. If Q is High and Code is Low, the incorrect code has been entered so go back to the IDLE state. In this state, LED should be given a value of `1`. 

COMBINATION_TWO: IF Q is low, nothing happens. If Q is High and Code is high, the correct code has been entered and go to next state. If Q is High and Code is Low, the incorrect code has been entered so go back to the IDLE state.  LED should be given a value of `2`. 


COMBINATION_THREE: IF Q is low, nothing happens. If Q is High and Code is high, the correct code has been entered and go to next state. If Q is High and Code is Low, the incorrect code has been entered so go back to the IDLE state.  LED should be given a value of `3`. 

OPEN: After the 3 codes have been entered, the safe will 'open' and show an LED code. If BTNC is pressed the safe will go back to IDLE state.

| Module Name: | State Machine |||
| -- --------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|reset \t|Input \t|1| Active high reset|
|clk \t|Input \t|1| Clock used for timing|
|btnu \t|Input \t|1| Button Up|
|btnd \t|Input \t|1| Button Down|
|btnc \t|Input \t|1| Button Center|
|btnl \t|Input \t|1| Button Left|
|btnr \t|Input \t|1| Button Right|
|sw \t|Input \t|16 | Input used for the code|
| led | Output | 16 | Output for the State Machine |

Specifications:

Q: If btnu, btnd, btnc, btnr, or btnl are high, then Q is high.

CODE:  
Combination 1: btnd, and sw = `16'b0000000000000001`

Combination 2: btnr and sw = `16'b1111001111001111`

Combination 3: btnc and sw = `16'b0100101010100111`
        """,
    "top_module_wavedrom": True,
    "top_module_testbench": True,
    "top_module_sim_file": "statemachine",

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

    "top": "StateMachine",
    "folder": "StateMachine",
    "files": "Makefile xdc.xdc statemachine.sv",

    "next_lesson": "",
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

