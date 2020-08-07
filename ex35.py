from sys import exit

def gold_room():
    print('this room is full of gold, how much do you take?')

    next = raw_input('> ')
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead('man, learn how to type a number')


    if how_much < 50:
        print 'nice! your not too greedy. you win!'
        exit(0)
    else:
        dead('you greedy bastard!')


def bear_room():
    print 'there is a bear here.'
    print 'the bear has a bunch of honey'
    print 'the fat bear is in fromt of another door'
    print 'how are you going to move the bear?'
    bear_moved = False


    while True:
        next = raw_input('> ')

        if next == 'take honey':
            dead('the bear looks at you then pimp slaps you in the face')
        elif next == 'taunt bear' and not bear_moved:
            print 'the bear has moved from the door now. you can go through.'
            bear_moved = True
        elif next == 'taunt bear' and bear_moved:
            dead('the bear gets pissed off and chews your crotch off')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print 'i have no idea what that means.'


def bolofumps_room():
    print 'here you see the great evil bolofump'
    print 'he, it whatever stares at you and you go insane'
    print 'do you flee for your life or eat your head?'

    next = raw_input('> ')
    if 'flee' in next:
        start()
    elif 'head' in next:
        dead('well, that was tasty!')
    else:
        bolofumps_room()

def dead(why):
    print why, 'good job!'
    exit(0)


def start():
    print 'you are in a dark room'
    print 'there is a door to your left and right'
    print 'which one do you take?'

    next = raw_input('> ')

    if next == 'left':
        bear_room()
    elif next == 'right':
        bolofumps_room()
    else:
        dead('you stumble around the room until you starve to death')


start()