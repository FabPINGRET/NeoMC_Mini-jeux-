execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> It’s time you do as all mortals must. Fade.","color":"white","bold":false}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/4 6s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
