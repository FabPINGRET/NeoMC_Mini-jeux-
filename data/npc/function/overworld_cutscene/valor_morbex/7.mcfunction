execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> My ","color":"white","bold":false},{"text":"Contagions","color":"dark_aqua"},{"text":" and ","color":"white"},{"text":"Dreadwardens","color":"light_purple"},{"text":" will not fail me.","color":"white","bold":false},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/8 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
