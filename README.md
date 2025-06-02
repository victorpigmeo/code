## Keystroke guesser 
This is a simple application to guess which key was typed on the keyboard using its sound

### How To Run
First you need a microphone and a mongodb running locally (with default username and password: `root`:`example`), if you want to use another database adapt the code to it

With the mongodb up and running execute the `fill_db.py` file
> Here is advised to create a python venv (`py -m venv env` on Windows or `python3 -m venv env` on Linux & Mac)
```
    python3 fill_db.py (Linux & Mac)
    py fill_db.py (Windows)
```
After that run the `__main__` program
The menu has two options Listen and guess and Exit

After entering the `Listen and guess` (Option 1) the program will count down from 3 to 1 and listen for 1 second
Then it will try to guess which key you type on your keyboard

### Available letters
* A (4 Samples)
* S (4 Samples)
* D (4 Samples)
* F (4 Samples)
* L (4 Samples)
* \+ (4 Samples)

> The sample count is low so as of now it is guessing very wrongly

## TODO: Add more samples and more letters