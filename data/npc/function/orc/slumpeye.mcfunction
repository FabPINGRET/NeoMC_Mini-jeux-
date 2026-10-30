execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Slumpeye","color":"green"},{"text":"> Buh grummmm. Grum grug bagogo bagrud! GUHHHHH BRUGRUGGGGGG!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Slumpeye","color":"green"},{"text":"> Why the ","color":"white"},{"text":"Germ Eaters","color":"dark_aqua"},{"text":" chose to establish their encampment in our wilds is beyond me. They possess not the faintest regard for the sanctity of nature! Fools.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
