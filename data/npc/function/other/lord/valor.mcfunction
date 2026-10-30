execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute if score lord_of_valor Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> It's time for that big meanie ","color":"white"},{"text":"Morbex","color":"dark_aqua"},{"text":" to get what's coming to him. A slimy fist right in the teeth and a mouthful of the knuckles of justice!","color":"white"}]

execute if score lord_of_valor Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> When you decide to confront the","color":"white"},{"text":" World Virus","color":"dark_aqua"},{"text":" once and for all, we will fight alongside you. This isn't over until the ","color":"white"},{"text":"Virus","color":"dark_aqua"},{"text":" has a playdate with Uncle Kill-You.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
