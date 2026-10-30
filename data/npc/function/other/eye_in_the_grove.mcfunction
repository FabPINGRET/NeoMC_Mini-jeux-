execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.spider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] run function npc:overworld_cutscene/eye_in_the_grove/0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"The Eye in the Grove","color":"gold"},{"text":"> Gather ever","color":"white","italic":false},{"text":"yyyyy","color":"gray","italic":true},{"text":"one here...","color":"white","italic":false}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
