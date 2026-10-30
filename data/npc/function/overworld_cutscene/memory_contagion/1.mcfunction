execute positioned 10670 77 -84 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.zoglin.angry neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10670 77 -84 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> Their minds are feeble and unguarded. Soon they will remember nothing but service to the ","color":"white"},{"text":"Virus ","color":"dark_aqua"},{"text":"and devotion to me, the ","color":"white"},{"text":"Memory Contagion","color":"green"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/2 12s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
