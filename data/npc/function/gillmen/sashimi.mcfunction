execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_bread_1,tag=mg.flw] [{"text":"<"},{"text":"Sashimi","color":"yellow"},{"text":"> Nothin' like bread baked below sea level! Or underwater in the sky anyway. It's still good, I promise!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_bread_1,tag=mg.flw] [{"text":"<"},{"text":"Sashimi","color":"yellow"},{"text":"> Gotta bake more! Thanks for asking though, I'm glad you like it.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_bread_1,tag=mg.flw] bread 8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_bread_1,tag=mg.flw] add vendor_bread_1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
