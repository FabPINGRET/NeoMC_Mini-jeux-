execute positioned 123 47 -53 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block 132 42 -51 air positioned 123 47 -53 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gugubrug","color":"dark_aqua"},{"text":"> The bartender is an okay guy, but when I ask him for a ","color":"white"},{"text":"Sludge Blaster","color":"dark_aqua"},{"text":", he just gives me a weird look like he wants to cry. I already told him the recipe is at the","color":"white"},{"text":" top of a tower","color":"dark_aqua"},{"text":" if he needs to go double check it.","color":"white"}]
execute if block 132 42 -51 target positioned 123 47 -53 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gugubrug","color":"dark_aqua"},{"text":"> This sludge hits just right. I really love how the crunchy rocks in it feel when I bite down hard on them with my little teeth!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
