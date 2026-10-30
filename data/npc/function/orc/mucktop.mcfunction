execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Mucktop","color":"green"},{"text":"> Grug buh. Gruhhh ga boogoo grum gruggggg!!! GrAHHH brumgud gub gub grugo bagrummmm.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Mucktop","color":"green"},{"text":"> The bones of generations of Orcs and their Caos rest here, blanketed by the consoling weight of cool earth. I visit often to tour my future quarters out of some morbid instinct. It feels like... preparing a room for a dear friend. A friend whose comfort I care about deeply, though I know they will never use the furniture.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
