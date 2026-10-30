execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Stinky Paul","color":"aqua"},{"text":"> It takes a ton of wood to build these beauties, and wood doesn't grow on trees. In grows ","color":"white"},{"text":"in","color":"white","italic":true},{"text":" them, so we cut them down!","color":"white","italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
