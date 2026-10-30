execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 132 42 -50 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Sticks","color":"yellow"},{"text":"> I'm thirsty for a nice ","color":"white"},{"text":"Lavender Sky","color":"light_purple"},{"text":", but Mozmio acts weird whenever I ask him for one. I told him the recipe is","color":"white"},{"text":" behind a painting ","color":"yellow"},{"text":"if he just needs to go look at it, nothing wrong with needing a refresher.","color":"white"}]
execute if block 132 42 -50 target at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Sticks","color":"yellow"},{"text":"> Mmm this reminds me of the good old days. Back when things were more... stable.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
