execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -222 33 244 if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Icelorn Tenor","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhhhuuuhhuh","color":"gray","italic":true},{"text":" Everyone...","color":"white","italic":false},{"text":" huuhhuhuhhhuuuuh ","color":"gray","italic":true},{"text":"Get... Everyone... Here... First...","color":"white","italic":false},{"text":" hhhuuuuhuuhuuuhuuhuuhhuhuuu","color":"gray","italic":true}]

execute positioned -222 33 244 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run function npc:overworld_cutscene/icelorn_choir/0 

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
