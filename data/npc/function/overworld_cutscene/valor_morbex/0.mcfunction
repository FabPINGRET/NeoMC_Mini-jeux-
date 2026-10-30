execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> We are standing in the ","color":"white","bold":false},{"text":"Lords’ Chamber","color":"gold"},{"text":", the very heart of authority in the Dark Isles. My ","color":"white"},{"text":"Dreadwardens","color":"light_purple"},{"text":" have seized all Seven Lords who used to rule here, and their power is now mine.","color":"white"},{"text":" ⇒","color":"light_purple"}]

tag @a[tag=mg.flw] add cutscene


schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/1 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
