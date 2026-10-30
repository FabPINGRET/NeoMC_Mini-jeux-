execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> You know what, I think I'm going to let you! Be my sidekick, that is. But only on ","color":"white"},{"text":"one condition","color":"light_purple"},{"text":". You will need to discover my ","color":"white"},{"text":"secret identity","color":"green"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/10 12s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
