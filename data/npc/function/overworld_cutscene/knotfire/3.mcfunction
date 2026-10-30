execute positioned -10697 71 89 run playsound minecraft:entity.creaking.attack neutral @a[tag=mg.flw] ~ ~ ~ 2 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> Like the pilgrims who have made the great ascent before you, your body will be cracked like a doll. The meager ","color":"white"},{"text":"spark","color":"green"},{"text":" behind your eyes will be supplanted by my majesty.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/knotfire/4 12s

execute positioned -10697 41 89 run function summon:knotfire
spawnpoint @a[tag=mg.flw] -10682 72 89 90 0
scoreboard players set $flsp mg.st 30

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
