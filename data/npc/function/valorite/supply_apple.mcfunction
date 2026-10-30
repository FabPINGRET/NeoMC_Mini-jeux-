execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_apple_2,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> An apple a day keeps the horrors away.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_apple_2,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> You've taken your fair share of apples for the day.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_apple_2,tag=mg.flw] apple 8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_apple_2,tag=mg.flw] add vendor_apple_2


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
