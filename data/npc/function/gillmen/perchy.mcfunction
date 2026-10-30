execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score bubble_lake Story matches 0..3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Perchy","color":"yellow"},{"text":"> We found a dormant ","color":"white"},{"text":"Worldgate","color":"dark_purple"},{"text":" at the bottom of the ","color":"white"},{"text":"Lake","color":"blue"},{"text":". It seems like it wants to open, but it needs a little boost. The death of the ","color":"white"},{"text":"Lake Freak Supreme","color":"dark_green"},{"text":" might just tip it over the edge...\n\nLet me show you the locations of all the","color":"white"},{"text":" Lake Freaks","color":"dark_green"},{"text":".","color":"white"}]
execute if score bubble_lake Story matches 0..3 run effect give @e[tag=l_freak,distance=0..] minecraft:glowing 30 0 true
execute if score bubble_lake Story matches 0..3 run effect give @e[tag=l_f_supreme,distance=0..] minecraft:glowing 30 0 true

execute if score bubble_lake Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Perchy","color":"yellow"},{"text":"> ","color":"white"},{"text":"Bubble Lake","color":"blue"},{"text":" is much safer now thanks to you!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
