import time, threading

def count_time(cb):
    global time, timer
    cb()
    time += 1
    timer = threading.Timer(1, count_time, (cb,))
    timer.start()

def game(keywords, user_in):
    if user_in in keywords:
        keywords[user_in] = True
        return True
    else:
        return False

def total_points_game(keywords, N):
    values = keywords.values()
    points = sum(values)
    return (points, True) if points == N else (points, False)

time = 0
timer = None
if __name__ == '__main__':
    keywords = {'void': False, 'int': False, 'float': False}
    N = len(keywords)
    
    print('Type a keyword: ')
    count_time(lambda: print('-> time: %s' % time))
    while time < 10:
        user_in = input()
        if game(keywords, user_in):
            print('Correct!')
        else: 
            print('Wrong :(')        
        
        (points, all_done) = total_points_game(keywords, N)
        if all_done:
            break

    timer.cancel()
    print('----------------------------')
    print('Game Over')
    print('total points: %s' % points)
    print('total time: %s' % time)
    print('keywords result: ', keywords)
    print('----------------------------')

