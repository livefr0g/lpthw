from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        cur = self.map.opening_scene()

        while True:
            next = cur.enter()
            cur = self.map.next_scene(next)

class Death(Scene):

    quips = [
        "You died, you dummy.",
        "Way to go, you've been returned to dust.",
        "Your soul is smashed to a million pieces.",
        "You suck at this game.",
        "My dog is better at this than you."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)], "Good job!"
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print """
    The Gothons of Planet Percal #25 have entered your ship and destroyed
    your entire crew. You are the last surviving member and your last
    mission is to get the neutron destruct bomb from the Weapons Armory,
    put it in the bridge, and blow the ship up after getting into an
    escape pod.
    \n
    You're running down the central corridor to the Weapons Armory when
    a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
    costume flowing around his hate filled body. He's blocking th door
    to the Armory and about to pull a weapon to blast you.
    \n
    What do you do?
    """
        action = raw_input("> ")
        if "shoot" in action:
            print """
    Quick on the draw, you pull out your blaster and shoot him in his stupid
    face. His clown costume is flowing and moving around his body, which messes
    up your aim. Your laser hits his costume, but misses him entirely. This
    completely ruins his brand new costume which his mommy just bought him.
    Enraged, he shoots you repeatedly in the face until you die. Then he eats
    your soul.
    """
            return 'death'
        elif "dodge" in action:
            print """
    Like a world class boxer you dodge, weave, slip and slide right as
    the Gothon's blaster cranks a laser past your head. In the middle of
    your artful dodge your foot slips and you bang your head on the metal
    wall and pass out.

    You wake up shortly afterwards, only to die as the Gothon stomps your
    ugly face in and devours your soul.
    """
            return 'death'
        elif "joke" in action:
            print """
    Luck for you, you were forced to learn Gothon insults at the Academy.
    You tell the one Gothon joke you know:
    \n\t'Lefhj ghdfjk, fjfhi ui oid fdhj kusgdy.'\n
    The Gothon stops, tries not to laugh, and then falls to the floor, rolling
    in laughter. While he's laughing, you run up and shoot him squarely in the
    face. His writhing body goes lifeless, and you jump over his ugly corpse
    into the Armory.
    """
            return 'laser_weapon_armory'
        else:
            print "lol wut?"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print """
    You do a dive roll into the Weapon Armory, crouch, and scan the room for
    more Gothons than may be hiding. It's dead quiet; in fact, TOO quiet.
    You stand up and run to the far side of the room where the neutron destruct
    bomb is housed inside a container. There's a keypad lock on the box, and
    you need the code to get the bomb out. If you get the code wrong 10 times
    then the box is closed forever, and you can't get the bomb. The code is
    3 digits.
    """
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        print "[code is: %s]" % code
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:

            print "BZZZ!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print """
    The container clicks open and the seal breaks, letting gas out.
    You grab the neutron bomb and run as fast as you can to the bridge,
    where you must place it in the right spot.
    """
            return 'the_bridge'
        else:
            print"""
    The lock buzzes one last time and you hear a sickening melting sound
    as the mechanism is fused together.
    You decide to sit there, and finally the Gothons blow up your ship and
    you die.
    """
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print """
    You burst onto the Bridge with the neutron destruct bomb under your arm
    and surprise 5 Gothons who are trying to take control of the ship. Each of
    them has an even uglier clown costume than the last. They haven't pulled
    their weapons out yet, as they see the active bomb under your arm and
    don't want to set it off.
    """
        action = raw_input("> ")

        if "throw" in action:
            print """
    In a panic, you throw the bomb at the group of Gothons and make a leap for
    the door. Right as you drop it a Gothon shoots you right in the back,
    killing you.\n
    As you die, you see another Gothon frantically trying to disarm the bomb.
    You die knowing they will probably blow up when it goes off.
    """
            return 'death'
        elif "place" in action:
            print """
    You point your blaster at the bomb under your arm, and the Gothons put
    their arms up and start to sweat. You inch backwards towards the door,
    open it, and carefully place the bomb on the floor, pointing your blaster
    at it.\n
    You then jump back through the door, punch the close button and blast the
    lock so the Gothons can't get out.\n
    Now that the bomb is placed, you run to the escape pod to get out of this
    dire situation.
    """
            return 'escape_pod'
        else:
            print "lol wut?!"
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print """
    You rush through the whole ship, desperately trying to make it to the
    escape pod before the whole ship goes KABOOM!\n
    It seems like hardly any Gothons are on the ship, so your run is clear
    of interference. You get to the chamber with the escape pods, and now
    need to pick one to take. Some of them could be damaged, but you don't
    have time to look. There's 5 pods: which one do you take?
    """
        good_pod = randint(1, 5)
        print "[correct pod is %d]" % good_pod
        guess = raw_input("[pod #] ")

        if guess == 'cheat':
            print "Cheaters never prosper. Except in this game."
            return 'win'
        elif int(guess) == good_pod:
            print """
    You jump into pod %s and hit the eject button. The pod easily slides out
    into space heading to the planet below. As it flies to the planet, you look
    back and see your ship implode then explode like a supernova, taking out
    the Gothon ship at the same time.
    """ % guess
            return 'win'
        else:
            print """
    You jump into pod %s and hit the eject button. The pod escapes out into the
    void of space, and then implodes as the hull ruptures, crushing your body
    into jelly.
    """ % guess
            return 'death'

class Win(Scene):

    def enter(self):
        print "You won. Good job!"
        exit(0)

class Map(object):

    scenes = {
        "central_corridor": CentralCorridor(),
        "death": Death(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "win": Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()