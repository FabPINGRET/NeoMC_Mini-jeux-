execute positioned 173 59 2 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 173 59 2 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thragmotum","color":"dark_aqua"},{"text":"> The bridge to Dwarf City was demolished, but a self-assembling backup bridge can be activated with a well-placed arrow.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
