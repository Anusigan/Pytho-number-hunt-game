# Destroyer of Numbers

Welcome to the **Destroyer of Numbers** game! This is a simple text-based game where players attempt to "destroy" randomly generated numbers within a limited number of attempts. The game keeps track of the player's progress and records the game statistics in a log file.

## How to Play

1. Run the game script.
2. Enter your player name when prompted.
3. You will be presented with a set of numbers to "fight" in each attempt.
4. Select a number to fight by typing it in.
5. If the selected number is one of the presented numbers and is less than or equal to your life score, you will "kill" the number, and your life score will increase by the value of that number.
6. If the selected number is greater than your life score, the game ends, and the selected number "kills" you.
7. If you select a number that is not presented, the game ends.
8. You have a maximum of 20 attempts to survive and increase your life score.

## Game Features

- **Random Number Generation**: The game generates random numbers within specified ranges based on the current attempt number.
- **Error Handling**: Ensures that the player's input is an integer and provides feedback if it is not.
- **Game Logging**: Records game statistics, including player name, life score, presented numbers, selected number, and game status, in a log file.

## Files

- `destroyer_of_numbers.py`: The main game script.
- `README.md`: This readme file.

## Example Log Filename

The log file is named using the current date, time, and a random number to ensure uniqueness. An example filename might be `2024_06_09_12_34_56_1234.txt`.

## Requirements

- Python 3.x

## Running the Game

1. Ensure you have Python 3 installed on your system.
2. Download the `destroyer_of_numbers.py` script.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   ```bash
   python destroyer_of_numbers.py
