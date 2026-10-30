execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.allay.ambient_with_item neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute positioned 10319 34 -103 if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kovács János","color":"dark_purple"},{"text":"> Please, if there are others like you, bring them here. I am growing weary of this cave.","color":"white","italic":false}]

execute positioned 10319 34 -103 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run function npc:overworld_cutscene/custodian/0 

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
