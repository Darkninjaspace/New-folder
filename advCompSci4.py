import logic


"""
Anderson was never in room 235
maya's fingerprint were only on the calculus_book
Camron's fingerprints were not on the laptop

Camron
Anderson
Maya

Laptop
charging_cable
calculus_book

room 235
makerspace
fishbowl
"""


Camron = logic.Symbol("Camron")
Anderson = logic.Symbol("Anderson")
Maya = logic.Symbol("Maya")

laptop = logic.Symbol("laptop")
charging_cable = logic.Symbol("charging cable")
calculus_book = logic.Symbol("calculus book")

room_235 = logic.Symbol("room 235")
makerspace = logic.Symbol("makerspace")
fishbowl = logic.Symbol("fishbowl")

knowledge = logic.And(

logic.Or( Camron , Anderson , Maya),
logic.Or(laptop, charging_cable ,  calculus_book),
logic.Or(room_235 ,  makerspace ,  fishbowl ),

#maya's fingerprint were only on the calculus_book:
logic.Or(
    logic.And(Maya, calculus_book ),
    logic.And(logic.Not(Maya), logic.Not(calculus_book)),
    ),
#Camron's fingerprints were not on the laptop
logic.Or(
    logic.And(logic.Not(laptop), Camron),
    logic.And(logic.Not(Camron), laptop),
    logic.And(logic.Not(Camron), logic.Not(laptop))
    ),
#Anderson was never in room 235
logic.Or(
    logic.And(Anderson, logic.Not(room_235)),
    logic.And(room_235, logic.Not(Anderson)),
    logic.And(logic.Not(Anderson), logic.Not(room_235))
),

#calculus book never left the fishbowl
logic.Or(
    logic.And(calculus_book,fishbowl),
    logic.And(logic.Not(calculus_book),logic.Not(fishbowl))
),

#camron and the laptop and the makerspace but at lease one of these three was wrong
logic.Or(logic.Not(Camron),logic.Not(laptop),logic.Not(makerspace)),

#maya was never in the makerspace
logic.Or(
    logic.And(Maya,logic.Not(makerspace)),
    logic.And(makerspace,logic.Not(Maya)),
    logic.And(logic.Not(makerspace),logic.Not(Maya))
),
#Anderson's fingerprints werent found on the charging cable
logic.Or(
    logic.And(Anderson, logic.Not(charging_cable)),
    logic.And(charging_cable, logic.Not(Anderson)),
    logic.And(logic.Not(Anderson), logic.Not(charging_cable))
),

#guessed camron and room 235 and charging cable but was wrong
logic.And(logic.Not(Camron),logic.Not(room_235),logic.Not(charging_cable)),

#not in fishbowl
logic.Not(fishbowl)
)

print ("Camron:",logic.model_check(knowledge,Camron))
print ("Anderson:",logic.model_check(knowledge,Anderson))
print ("Maya:",logic.model_check(knowledge,Maya))
print ("Charging Cable:",logic.model_check(knowledge,charging_cable))
print ("Laptop:",logic.model_check(knowledge,laptop))
print ("Calculus Book:",logic.model_check(knowledge,calculus_book))
print ("Room 235:",logic.model_check(knowledge,room_235))
print ("Makerspace:",logic.model_check(knowledge,makerspace))
print ("Fishbowl:",logic.model_check(knowledge,fishbowl))