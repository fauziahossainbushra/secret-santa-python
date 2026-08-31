# Secret Santa Assignment Program
## Overview
 A simple Python program that automates Secret Santa assignments for a group of participants.
The program randomly assigns each participant another person while ensuring that:
* A participant cannot be assigned to themselves.
* Each participant is assigned only once.
## How it Works
The program uses Python's random module to randomly select participants.
A while loop checks whether the selected person:
1. Is the same as the current participant.
2. Has already been assigned to someone else.
If either condition is true, the program selects another participant. Once a valid assignment is found, the person is added to the list of assigned participants and the assignment is displayed.
## Technologies Used
* Python
* random module
## Example Output
Amy -> Tom
Ben -> Emma
Cara -> Amy
Tom -> Ben
Emma -> Cara
The output will be different each time the program runs because the assignments are randomized.
## How to Run
1. Make sure Python is installed on your computer.
2. Clone this repository.
3. Open the project in your preferred Python IDE.
4. Run: python secret_santa_version1.py
## What I learned
This project helped me practice Python control flow and problem-solving by creating rules that the program must follow while generating random assignments.
It was also an opportunity to practice using Git and GitHub to manage and publish a project.
