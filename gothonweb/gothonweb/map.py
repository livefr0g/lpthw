class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class Death(Room):

    def __init__(self, description):
        super(Death, self).__init__("death", description)

class End(Room):

    def __init__(self, description):
        super(End, self).__init__("The End", description)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have entered your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you, you were forced to learn Gothon insults at the Academy.
You tell the one Gothon joke you know:
'Lefhj ghdfjk, fjfhi ui oid fdhj kusgdy.'
The Gothon stops, tries not to laugh, and then falls to the floor, rolling
in laughter. While he's laughing, you run up and shoot him squarely in the
face. His writhing body goes lifeless, and you jump over his ugly corpse
into the Armory.

You do a dive roll into the Weapon Armory, crouch, and scan the room for
more Gothons that may be hiding. It's dead quiet; in fact, TOO quiet.
You stand up and run to the far side of the room where the neutron destruct
bomb is housed inside a container. There's a keypad lock on the box, and
you need the code to get the bomb out. If you get the code wrong 10 times
then the box is closed forever, and you can't get the bomb. The code is
3 digits.
""")

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the bridge,
where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb under your arm
and surprise 5 Gothons who are trying to take control of the ship. Each of
them has an even uglier clown costume than the last. They haven't pulled
their weapons out yet, as they see the active bomb under your arm and
don't want to set it off.
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm, and the Gothons put
their arms up and start to sweat. You inch backwards towards the door,
open it, and carefully place the bomb on the floor, pointing your blaster
at it.
You then jump back through the door, punch the close button and blast the
lock so the Gothons can't get out.
Now that the bomb is placed, you run to the escape pod to get out of this
dire situation.

You rush through the whole ship, desperately trying to make it to the
escape pod before the whole ship goes KABOOM!
It seems like hardly any Gothons are on the ship, so your run is clear
of interference. You get to the chamber with the escape pods, and now
need to pick one to take. Some of them could be damaged, but you don't
have time to look. There's 5 pods: which one do you take?
""")

end_win = End(
"""
You jump into pod 2 and hit the eject button. The pod easily slides out
into space heading to the planet below. As it flies to the planet, you look
back and see your ship implode then explode like a supernova, taking out
the Gothon ship at the same time.

Good job. You won!
""")

end_lose = End(
"""
You jump into a random pod and hit the eject button. The pod escapes out into the
void of space, and then implodes as the hull ruptures, crushing your body
into jelly.
""")

generic_death = Death("you died.")

shoot_death = Death(
"""
Quick on the draw, you pull out your blaster and shoot him in his stupid
face. His clown costume is flowing and moving around his body, which messes
up your aim. Your laser hits his costume, but misses him entirely. This
completely ruins his brand new costume which his mommy just bought him.
Enraged, he shoots you repeatedly in the face until you die. Then he eats
your soul.
"""
)

dodge_death = Death(
"""
Like a world class boxer you dodge, weave, slip and slide right as
the Gothon's blaster cranks a laser past your head. In the middle of
your artful dodge your foot slips and you bang your head on the metal
wall and pass out.

You wake up shortly afterwards, only to die as the Gothon stomps your
ugly face in and devours your soul.
"""
)

laser_weapon_armory_death = Death(
"""
The lock buzzes one last time and you hear a sickening melting sound
as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up your ship and
you die.
"""
)

the_bridge_death = Death(
"""
In a panic, you throw the bomb at the group of Gothons and make a leap for
the door. Right as you drop it a Gothon shoots you right in the back,
killing you.
As you die, you see another Gothon frantically trying to disarm the bomb.
You die knowing they will probably blow up when it goes off.
"""
)

escape_pod.add_paths({
    '2': end_win,
    '*': end_lose
})

the_bridge.add_paths({
    'throw the bomb': the_bridge_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': laser_weapon_armory_death
})

central_corridor.add_paths({
    'shoot': shoot_death,
    'dodge!': dodge_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor