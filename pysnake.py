import curses
import random
import time

def game_loop(window,difficult):
    
    curses.curs_set(0)
    snake = [[10,15], [10,14], [10,13], [10,12]]
    fruit = get_new_fruit(window=window)
    current_direction = curses.KEY_RIGHT
    snake_ate_fruit = False
    score = 0

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit,window=window,char=curses.ACS_DIAMOND)
        direction = get_direction(window=window, timeout=difficult)

        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction,current_direction=current_direction):
            direction = current_direction
        move_snake(snake=snake,direction=direction,snake_ate_fruit=snake_ate_fruit)  

        if snake_hit_border(snake=snake,window=window):
            break
        if snake_hit_itself(snake=snake):
            break
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window=window)
            score += 1
        else:
            snake_ate_fruit = False
        current_direction = direction
    finish_game(score=score, window=window)

def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2),random.randint(1, width-2)]

def draw_screen(window):
        window.clear()
        window.border(0)

def draw_actor(actor,window,char):
    window.addch(actor[0], actor[1], char)

def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head,window=window, char='●')
    body = snake[1:]
    for part in body:
        draw_actor(actor=part, window=window, char='○')

def get_direction(window, timeout):
        window.timeout(timeout)
        direction = window.getch()
        if direction in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]:
             return direction
        else:
             return None

def direction_is_opposite(direction, current_direction):
    if direction == curses.KEY_UP:
        return current_direction == curses.KEY_DOWN
    elif direction == curses.KEY_DOWN:
        return current_direction == curses.KEY_UP
    elif direction == curses.KEY_LEFT:
        return current_direction == curses.KEY_RIGHT
    elif direction == curses.KEY_RIGHT:
        return current_direction == curses.KEY_LEFT

def move_actor(actor, direction):
        if direction == curses.KEY_UP:
            actor[0] -= 1
        elif direction == curses.KEY_DOWN:
            actor[0] += 1
        elif direction == curses.KEY_LEFT:
            actor[1] -= 1
        elif direction == curses.KEY_RIGHT:
            actor[1] += 1

def move_snake(snake,direction,snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    if not snake_ate_fruit:
        snake.pop()

def actor_hit_border(actor,window):
    height, width = window.getmaxyx()

    if actor[0] <= 0 or actor[0] >= height - 1:
        return True
    if actor[1] <= 0 or actor[1] >= width -1:
        return True
    return False

def snake_hit_border(snake,window):
    head = snake[0]
    return actor_hit_border(actor=head, window=window)

def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body

def snake_hit_fruit(snake,fruit):
    return fruit in snake

def finish_game(score,window):
    height, width = window.getmaxyx()
    s = f'Você perdeu! Coletou {score} frutas!'
    y, x = int((height)/2), int((width-len(s))/2)
    window.addstr(y,x,s)
    window.refresh()
    time.sleep(5)

def difficult():
    difficult_levels = {'1' : 250, '2' : 120, '3' : 60, '4' : 30, '5' : 15}
    
    while True:
        answer = input('Selecione uma dificuldade de 1 à 5: ')
        difficult = difficult_levels.get(answer)
        if difficult is not None:
            return difficult
        print('Selecione dificuldade de 1 à 5!')

if __name__ == '__main__':
    curses.wrapper(game_loop,difficult=difficult())
