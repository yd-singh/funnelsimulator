Onboarding Funnel Simulation

This project simulates a customer onboarding funnel, allowing you to model and analyze the flow of customers through various verification modules. It calculates key metrics such as success rates, costs, and processing times, providing insights into the efficiency and effectiveness of your onboarding process.

Table of Contents

	•	Features
	•	Getting Started
	•	Prerequisites
	•	Installation
	•	Usage
	•	Running the Simulation
	•	Understanding the Output
	•	Configuration
	•	Modules Configuration (config.yaml)
	•	Example Output
	•	Customization
	•	License
	•	Acknowledgments

Features

	•	Simulate customer flow through an onboarding funnel with customizable modules.
	•	Calculate success rates, total and average costs, and processing times.
	•	Output detailed results to the terminal and a Markdown file.
	•	Easily configurable via a YAML configuration file.

Getting Started

Prerequisites

Ensure you have the following installed:

	•	Python 3.6 or higher
	•	pip package manager

Installation

	1.	Clone the repository:

git clone https://github.com/yourusername/onboarding-funnel-simulation.git
cd onboarding-funnel-simulation


	2.	Install required Python packages:

pip install -r requirements.txt

If requirements.txt is not provided, install the packages individually:

pip install pandas pyyaml tabulate



Usage

Running the Simulation

	1.	Configure the simulation parameters:
	•	Open main.py and set the customers_count variable to the desired number of customers to simulate.

def main():
    customers_count = 100  # Set the number of customers
    ...


	2.	Run the simulation:

python main.py


	3.	View the results:
	•	The simulation results will be printed in the terminal.
	•	A detailed report will be saved as simulation_results.md in the project directory.

Understanding the Output

	•	Terminal Output:
The terminal will display:
	•	Summary statistics (total success, failures, success rate, total cost, total time).
	•	A detailed table showing the results for each module.
	•	Markdown Report (simulation_results.md):
	•	Contains the same summary statistics and detailed module results in a Markdown format.
	•	You can view this file using any Markdown viewer or text editor.

Configuration

Modules Configuration (config.yaml)

The simulation uses a YAML configuration file (config.yaml) to define the modules in the onboarding funnel.

Example config.yaml:

modules:
  - name: Phone Verification
    is_start: true
    success_rate: 0.97
    cost_per_transaction: 2
    time_to_complete: 30
    next_module_on_success: "PAN Verification"
    next_module_on_failure: "Failed"

  - name: PAN Verification
    success_rate: 0.90
    cost_per_transaction: 1
    time_to_complete: 20
    next_module_on_success: "CKYC Verification"
    next_module_on_failure: "Failed"

  - name: CKYC Verification
    success_rate: 0.75
    cost_per_transaction: 1.75
    time_to_complete: 8
    next_module_on_success: "VCIP"
    next_module_on_failure: "Digilocker Verification"

  - name: Digilocker Verification
    success_rate: 0.70
    cost_per_transaction: 2
    time_to_complete: 15
    next_module_on_success: "VCIP"
    next_module_on_failure: "Failed"

  - name: VCIP
    success_rate: 0.50
    cost_per_transaction: 10
    time_to_complete: 120
    next_module_on_success: "Success"
    next_module_on_failure: "Failed"

Configuration Parameters:

	•	name: The name of the module.
	•	is_start: Indicates if this module is the starting point of the funnel.
	•	success_rate: The probability (between 0 and 1) that a customer passes the module.
	•	cost_per_transaction: The cost incurred per customer processed in the module.
	•	time_to_complete: Time (in seconds) taken to process each customer in the module.
	•	next_module_on_success: The next module if the customer passes. Use "Success" if it leads to final success.
	•	next_module_on_failure: The next module if the customer fails. Use "Failed" if the customer is terminally rejected.
	•	is_parallel (optional): Indicates if the module runs in parallel with others (not utilized in current implementation).

Customizing Modules:

You can add, remove, or modify modules by editing the config.yaml file. Ensure that:

	•	There is exactly one module with is_start: true.
	•	The next_module_on_success and next_module_on_failure refer to valid module names, "Success", or "Failed".

Example Output

Terminal Output:

Total Success: 40
Total Failures: 60
Success Rate: 40.00%
Total Cost: $1293.25
Total Time: 259.43 minutes
Average Cost per Customer: $12.93
Average Time per Customer: 2.59 minutes
             Module  Enter Funnel Success Rate  Pass  Fail  Final Success  Terminally Rejected  Total Cost  Total Time  Average Cost per Customer  Average Time per Customer
Phone Verification           100          97%    97     3              0                    3      200.00     3000.00                       2.00                      30.00
   PAN Verification            97          90%    87    10              0                   10       97.00     1940.00                       1.00                      20.00
CKYC Verification             87          75%    65    22              0                    0      152.25      696.00                       1.75                       8.00
Digilocker Verification       22          70%    15     7              0                    7       44.00      330.00                       2.00                      15.00
              VCIP            80          50%    40    40             40                   40      800.00     9600.00                      10.00                     120.00

Results have been saved to 'simulation_results.md'.

Markdown Report (simulation_results.md):

# Onboarding Simulation Results

## Summary Statistics

- **Total Success:** 40
- **Total Failures:** 60
- **Success Rate:** 40.00%
- **Total Cost:** $1293.25
- **Total Time:** 259.43 minutes
- **Average Cost per Customer:** $12.93
- **Average Time per Customer:** 2.59 minutes

## Detailed Module Results

| Module                  |   Enter Funnel | Success Rate   |   Pass |   Fail |   Final Success |   Terminally Rejected |   Total Cost |   Total Time |   Average Cost per Customer |   Average Time per Customer |
|-------------------------|----------------|----------------|--------|--------|-----------------|-----------------------|--------------|--------------|-----------------------------|-----------------------------|
| Phone Verification      |            100 | 97%            |     97 |      3 |               0 |                     3 |       200.00 |      3000.00 |                        2.00 |                       30.00 |
| PAN Verification        |             97 | 90%            |     87 |     10 |               0 |                    10 |        97.00 |      1940.00 |                        1.00 |                       20.00 |
| CKYC Verification       |             87 | 75%            |     65 |     22 |               0 |                     0 |       152.25 |       696.00 |                        1.75 |                        8.00 |
| Digilocker Verification |             22 | 70%            |     15 |      7 |               0 |                     7 |        44.00 |       330.00 |                        2.00 |                       15.00 |
| VCIP                    |             80 | 50%            |     40 |     40 |              40 |                    40 |       800.00 |      9600.00 |                       10.00 |                      120.00 |

Customization

	•	Changing Customer Count:
Modify customers_count in main.py to simulate a different number of customers.
	•	Adjusting Module Parameters:
Edit config.yaml to change success rates, costs, times, and module flow.
	•	Adding New Modules:
	•	Add a new module definition in config.yaml.
	•	Ensure that the module’s next_module_on_success and next_module_on_failure are properly set.
	•	Parallel Processing (Advanced):
While the current implementation doesn’t support parallel processing, you can set is_parallel: true in config.yaml for future extensions.


Acknowledgments

	•	Python Community: For providing excellent libraries like pandas, pyyaml, and tabulate.
	•	Contributors: Thanks to everyone who contributed to this project.

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is highly appreciated!
