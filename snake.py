#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)
    
    # Check if terminal is big enough
    height, width = stdscr.getmaxyx()
    min_height, min_width = 10, 20
    if height < min_height or width < min_width:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Terminal too small! Minimum size: {min_width}x{min_height}")
        stdscr.refresh()
        stdscr.getch()
        return
    
    # Safe drawing function to avoid writing to bottom-right corner
    def safe_addch(y, x, char, attr=curses.A_NORMAL):
        if y < height-1 or x < width-1:  # Avoid bottom-right corner
            try:
                stdscr.addch(y, x, char, attr)
            except curses.error:
                pass  # Ignore out-of-bounds errors
    
    # Color pair definitions
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    # Initial snake position and direction
    snake = [(10, 10)]  # Start at center-ish
    direction = (0, 1)  # Moving right initially
    
    # Initial food position
    food = (5, 5)
    
    # Game settings
    score = 0
    game_speed = 0.1  # seconds between updates
    
    while True:
        # Clear screen
        stdscr.clear()
        
        # Update dimensions in case terminal was resized
        height, width = stdscr.getmaxyx()
        
        # Draw border (avoiding bottom-right corner)
        for i in range(height):
            safe_addch(i, 0, '|')
            if i < height-1:  # Avoid bottom-right corner
                safe_addch(i, width-1, '|')
        for i in range(width):
            safe_addch(0, i, '-')
            if i < width-1:  # Avoid bottom-right corner
                safe_addch(height-1, i, '-')
        
        # Draw snake
        for y, x in snake:
            safe_addch(y, x, '#', curses.color_pair(1))
        
        # Draw food
        safe_addch(food[0], food[1], '*', curses.color_pair(2))
        
        # Show score
        try:
            stdscr.addstr(0, 2, f' Score: {score} ')
        except curses.error:
            pass  # Ignore potential errors
        
        # Refresh screen
        stdscr.refresh()
        
        # Get user input
        stdscr.timeout(100)
        key = stdscr.getch()
        
        # Update direction based on key
        if key == curses.KEY_UP and direction != (1, 0):
            direction = (-1, 0)
        elif key == curses.KEY_DOWN and direction != (-1, 0):
            direction = (1, 0)
        elif key == curses.KEY_LEFT and direction != (0, 1):
            direction = (0, -1)
        elif key == curses.KEY_RIGHT and direction != (0, -1):
            direction = (0, 1)
        elif key == ord('q'):
            break
        
        # Calculate new head position
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        # Update dimensions in case terminal was resized
        height, width = stdscr.getmaxyx()
        
        # Check for collisions with boundaries or self
        if (new_head[0] <= 0 or new_head[0] >= height-1 or 
            new_head[1] <= 0 or new_head[1] >= width-1 or 
            new_head in snake):
            break
        
        # Add new head
        snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == food:
            score += 1
            # Generate new food position
            # Make sure we have space for food
            safe_height = max(3, height-2)
            safe_width = max(3, width-2)
            
            attempts = 0
            while True:
                food = (random.randint(1, safe_height-1), 
                       random.randint(1, safe_width-1))
                if food not in snake:
                    break
                attempts += 1
                if attempts > 50:  # Prevent infinite loop
                    food = (1, 1)  # Default position if we can't find a free spot
                    break
        else:
            snake.pop()
        
        # Control game speed
        time.sleep(game_speed)

# Start the game
curses.wrapper(main)
