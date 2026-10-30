execute positioned 168 59 -3 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 168 59 -3 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Houggar","color":"dark_aqua"},{"text":"> Nobody trusts anyone else in Dwarf City anymore, everyone is suspicious of their neighbors. Here people work together at least.","color":"white"}]
execute positioned 168 59 -3 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Houggar","color":"dark_aqua"},{"text":"> Dwarves are beginning to trust each other again, thanks to your help!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
