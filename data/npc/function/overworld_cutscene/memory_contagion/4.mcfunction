execute positioned -9960 99 370 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.zoglin.angry neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -9960 99 370 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Memory Nexus","color":"green"},{"text":"> Alright, if you take a quick look around, we're in my \"kill-you\" chamber.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/5 8s

spawnpoint @a[tag=mg.flw] -9960 100 358 0 0
scoreboard players set $flsp mg.st 31

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
