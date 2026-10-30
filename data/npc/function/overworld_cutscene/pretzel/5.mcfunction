spawnpoint @a[tag=mg.flw] -10340 88 435 0 0
scoreboard players set $flsp mg.st 33
execute positioned -10340 50 446 run function summon:pretzel_jenkins

execute positioned -10341 89 445 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> This is my Item-admiring chamber. Aren't you excited? Let's see what kinds of things could be inside ","color":"white"},{"text":"The Inviolable Barrel of One Billion Crud","color":"red"},{"text":"!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/6 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
