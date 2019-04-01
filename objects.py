# this is a very basic framework for some of the game objects that i whipped up in a bout of insomnia. its probably very
# likely that we will completely change this

# also why doesnt python have multiline comments

# note that i use "id_" instead of just id because id is a built-in keyword of python and PEP 8 advises appending an _


class Player:
    id_ = ""
    # todo: figure out how this object is structured


class Actor:  # nonplayer characters
    id_ = 0
    name = ""
    regionid = 0
    locationid = 0
    questids = []  # ids of quests given by actor
    inventory = []  # npc inventory in case of pickpocketing/killing?

    def __init__(self, id_, name, region, location, quests, inventory):
        self.id_ = id_
        self.name = name
        self.region = region
        self.location = location
        self.quests = quests
        self.inventory = inventory


class Item:
    id_ = 0
    name = ""
    description = ""
    stats = [["att", 0], ["def", 0], ["stam", 0]]  # placeholder stats to indicate structure of stats object

    def __init__(self, id_, name, description, stats):
        self.id_ = id_
        self.name = name
        self.description = description
        self.stats = stats


class Region:
    id_ = 0
    name = ""
    description = ""
    locations = []

    def __init__(self, id_, name, description, locations):
        self.id_ = id_
        self.name = name
        self.description = description
        self.locations = locations


class Location:
    id_ = 0
    name = ""
    description = ""

    def __init__(self, id_, name, description):
        self.id_ = id_
        self.name = name
        self.description = description


class Guest:
    id_ = 0
    name = ""
    description = ""
    events = []  # todo: reevaluate this

    def __init__(self, id_, name, description, events):
        self.id_ = id_
        self.name = name
        self.description = description
        self.events = events

# class event
