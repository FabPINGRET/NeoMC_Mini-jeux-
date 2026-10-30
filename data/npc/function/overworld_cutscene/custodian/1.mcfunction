execute positioned 10319 34 -103 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.allay.ambient_with_item neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

execute positioned 10319 34 -103 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kovács János","color":"dark_purple"},{"text":"> Would you take up my station? I cannot leave without knowing it is in the hands of a capable successor.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/custodian/2 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
