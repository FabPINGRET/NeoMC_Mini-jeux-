execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_chicken_0,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> Pro-chicken-eating-tip for you: spit out the bones.","color":"white"}]
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_chicken_0,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> You've taken your fair share of chicken for the day.","color":"white"}]
execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> We can't afford to stock up on chicken right now, the economy being what it is. Sorry.","color":"white"}]

execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_chicken_0,tag=mg.flw] cooked_chicken 6
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_chicken_0,tag=mg.flw] add vendor_chicken_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
