execute positioned -270 41 -58 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -270 41 -58 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ubgubli","color":"dark_aqua"},{"text":"> I try to tell myself I come here all the time because the food is good but... well, I worry I'm just stress eating. The food is good though.","color":"white"}]
execute positioned -270 41 -58 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ubgubli","color":"dark_aqua"},{"text":"> I've spent most of my savings on the food here, it's just that good! Don't tell my family.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
