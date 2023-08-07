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
<h3>Frequency Vs Period</h3>

Frequency is the number of times something occurs in a given time frame, while period is the amount of time it takes for something to occur. They are inverses of one another. 
$Period = \frac{1}{Frequency}$ and $Frequency = \frac{1}{Period}$. 

This is important when dealing with Clocks in circuits.

Example:  
You are running around a pillar while 
playing tag. 

You run around it 3 times every minute. That is your frequency.  

The period would be $\frac{1}{Frequency}$, so every 1/3 of a minute or 20 seconds you would complete a circle. This is the period.


So why does Frequency and Period matter?    

Timing is very important because of the FPGAs built in clock. The clock keeps all elements in the circuit working together and prevents conflicts.    

In this lab, inorder to create a stopwatch, you will need to know how many clock cycles occur in a given time frame, then after counting that many, increment the stopwatch.
        """,
    "part1_title": "The Counter Module",
    "part1_body": """
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/stopwatch_lab/media/mod_counter.png"
width="400" height="150" style="display: block; margin: 0 auto " />
<br>

| Module Name: | mod_counter|||
| -- --------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|reset 	|Input 	|1| Active high reset|
|clk 	|Input 	|1| Clock used for timing|
|increment 	|Input 	|1 | should only increment when enable if its high|
| MOD_VALUE|	Parameter| 	N/A| Value at which counter should reset, default of 10 	|
| rollover	|Output 	|1| 	High for one cycle when counter rolls over|
|count| 	Output 	|4| 	Current value of the counter|


<br>

When increment is high, the counter should begin increasing. When it reaches the MOD_VALUE, it should reset to zero and rollover should be high for that clock cycle. 
        """,
    "part1_wavedrom": False,
    "part1_testbench": False,
    "part1_sim_file": "mod_counter",

    "part2_exists": True,
    "part2_title": "The Stopwatch Module",
    "part2_body": """
<img src="https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/stopwatch_lab/media/stopwatch_module.jpg"
width="500" style="display: block; margin: 0 auto " />
<br><br>

| Module Name: | stopwatch |||
| -- --------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|clk 	|Input 	|1| The Clock Signal|
|reset 	|Input 	|1| Active high reset|  
|run 	|Input 	|1 | High when timer should be running|
| digit0	|Output 	|4| The value of the hundredths of a second digit|
| digit1	|Output 	|4| The value of the tenths of a second digit|
| digit2	|Output 	|4| The value of the seconds digit|
| digit3	|Output 	|4| The value of the tens of seconds digit|

<br>


You will  have to create a separate counter. This one will reset and give a rollover value every .01s. This cannot be an instantiation of `mod_counter` because its `count` value will be wider than 4 bits. This `rollover` will be fed into `digit0` as the `increment`.


You will also have to instantiate 4 different instances of `mod_counter`, `digit0` through `digit3`.

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

    "top_module_title": "Top Level Module",
    "top_module_body": """
| Module Name: | stopwatch_top|||
| -- --------- | ----------- |--|--|
| Port Name      | Direction       |Width|Function|
|clk 	|Input 	|1| The Clock Signal |
| btnc 	|Input 	|1 | Active High Reset|
| sw	|Input 	|1| High when stopwatch should be running |
| anode	|Output 	|4| Seven-segment anode values, from Seven-Segment Controller|
| segment	|Output 	|8| Seven-segment segment values,  from Seven-Segment Controller|  

The `clk` signal is defined in the XDC.  

When `btnc` is pressed, the stopwatch should go to `0` for all digits.

While the switch is high, the stopwatch should begin to increment. You should time it with a different stopwatch to make sure that your stopwatch is keeping accurate time.  

You can concatenate the 4 digits together to create the `datain` signal for `SevenSegmentControl`.

NOTE: We are giving you the Seven Segement Control Module. This allows you to show 4 unique digits by quickly alternativing between the 4 different valuse faster than your eyes can see.   

* `dataIn`: 16 bits, each 4 bits are a hex value which is shown as a digit.  
* `digitDisplay`: 4 bits, if you want all 4 digits, pass `1111` into it.  
* `digitPoint`: This determines which digit point is on.   
* `anode`: Hook this up to the output `anode` signal 
* `segment`: Hook up to the output `segment` signal 
* `reset`, and `clk`: Self-explanatory inputs
        """,
    "top_module_wavedrom": False,
    "top_module_testbench": False,
    "top_module_sim_file": "stopwatch_top",

    "xdc_exists": True,
    "xdc_title": "XDC File",
    "xdc_body":
    """
In the xdc file below, uncomment the lines corresponding to the FPGA I/O that you are using. You will also need to add 2 lines at the top for the clock.
```
# Clock
set_property -dict { PACKAGE_PIN W5    IOSTANDARD LVCMOS33 } [get_ports { clk }];
create_clock -period 10.00 [get_ports {clk}];

```
Then run the code block to create your xdc file.
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
            data[key]=data[key].replace('\n', '\\n')
            data[key]=data[key].replace('\t', '\\t')
            data[key]=data[key].replace('\frac', '\\\\frac')
            data[key]=data[key].splitlines()
    return data