execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 132 42 -52 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Varbax","color":"aqua"},{"text":"> I'm thirsty for a ","color":"white"},{"text":"Floaty Summer","color":"gold"},{"text":", but the bartender forgot how to make it. I put the recipe ","color":"white"},{"text":"in a tree","color":"aqua"},{"text":". Don't know why I did that to be honest, but it's there.","color":"white"}]
execute if block 132 42 -52 target at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Varbax","color":"aqua"},{"text":"> This is great! You make it?","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
