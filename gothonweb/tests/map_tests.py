from nose.tools import *
from gothonweb.map import *


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's
                a door to the North.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the Center.")
    north = Room("North", "Test room in the North.")
    south = Room("South", "Test room in the South.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('down'), down)
    assert_equal(west.go('east'), start)
    assert_equal(down.go('up'), start)

def test_gothon_map():
    assert_equal(START.go('shoot'), shoot_death)
    assert_equal(START.go('dodge!'), dodge_death)
    assert_equal(START.go('tell a joke'),
        laser_weapon_armory)

    assert_equal(laser_weapon_armory.go('0132'), the_bridge)
    assert_equal(laser_weapon_armory.go('*'), laser_weapon_armory_death)

    assert_equal(the_bridge.go('throw the bomb'), the_bridge_death)
    assert_equal(the_bridge.go('slowly place the bomb'), escape_pod)

    assert_equal(escape_pod.go('2'), end_win)
    assert_equal(escape_pod.go('*'), end_lose)