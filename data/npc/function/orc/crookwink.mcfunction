execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Crookwink","color":"green"},{"text":"> BUHHHHHHHHHHHHHHH gruhguh oog. OUOUOUOUUOUGGHHGHHGHGH bagoo mubgrud.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Crookwink","color":"green"},{"text":"> The nocturnal monsters have never been so severe. It must be the influence of the ","color":"white"},{"text":"World Virus","color":"dark_aqua"},{"text":" touching our world. I once believed we Orcs would endure this trial as we have all others, yet now I fear we may be forced to resist it directly and with force. Ancestors help us.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
