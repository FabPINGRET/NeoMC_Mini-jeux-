execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Wigglefist","color":"green"},{"text":"> Bum grumgo buhh. Gub gruhhhhhhh GROHH!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Wigglefist","color":"green"},{"text":"> Every Orc is accompanied by a ","color":"white"},{"text":"Cao","color":"green"},{"text":", beasts of the utmost humility, noble and fair. Mine is named Spucky.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
