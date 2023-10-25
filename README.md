# 2048
2048 game

# Summaries
logic.py contains the main functions for the game (i.e. move_up, move_right, addnum, etc.  I wrote this code myself.
2048_terminal.py allows you to play the game in the terminal
2048_searchahead.py automatically plays the game using the Monte Carlo method from [this Kite video](https://www.youtube.com/watch?v=FE_oAQ5FzMk).  For each possible next move, it tries x next moves x times, and adds the scores.  Then it chooses the move that has the best score.

# Notes on logic.py
- 90% chance of a 2 spawning, 10% chance of a 4

# Notes on 2048_searchahead.py
- The code 2048_searchahead.py is taken directly from [this Kite video](https://www.youtube.com/watch?v=FE_oAQ5FzMk)
- I'm pretty sure I followed the code exactly as it's written in the video, but it can never get past 1024 for me.
- If someone can help me understand what I've done wrong, I'd really appreciate it.

Contact me at czbecher.design@gmail.com
