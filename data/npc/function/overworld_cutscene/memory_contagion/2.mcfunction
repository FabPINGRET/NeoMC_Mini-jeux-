execute positioned 10670 77 -84 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.zoglin.angry neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10670 77 -84 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Memory Nexus","color":"green"},{"text":"> And you? You will never remember anything ever again.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/3 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
