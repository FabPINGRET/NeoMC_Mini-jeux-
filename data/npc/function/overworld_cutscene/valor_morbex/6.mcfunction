execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Bah, have this city, hero. I am needed elsewhere. The ","color":"white","bold":false},{"text":"Seven Lords","color":"gold"},{"text":" will never return to this tower, and you cannot stop us without the power of ","color":"white"},{"text":"all seven","color":"gold"},{"text":".","color":"white","bold":false},{"text":" ⇒","color":"light_purple"}]

fill 10013 91 -98 10013 91 -101 air

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/7 12s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
