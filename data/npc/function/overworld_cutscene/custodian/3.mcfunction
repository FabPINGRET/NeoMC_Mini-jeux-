playsound minecraft:entity.allay.ambient_with_item neutral @a[tag=mg.flw] -10441 84 439 2 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Kovács János","color":"dark_purple"},{"text":"> If you can survive the unbridled power of the","color":"white"},{"text":" Spheres","color":"light_purple"},{"text":", I will entrust their power to your care...","color":"white"}]

schedule function floaty:sched/npc/overworld_cutscene/custodian/4 7s

spawnpoint @a[tag=mg.flw] -10441 84 429 0 0
scoreboard players set $flsp mg.st 27

execute positioned -10441 58 439 run function summon:custodian_of_the_spheres

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
