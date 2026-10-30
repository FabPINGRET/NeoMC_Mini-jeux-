execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score lord_of_valor Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Fool, what do you think you're doing up here? Nothing in this realm can harm me, the Seven Lords are broken. Begone with you.","color":"white","bold":false}]

execute if score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Me? You want me to be the seventh Lord? Were you dropped on your head as a baby? Begone with you, imbecile. I'm ashamed to call you my enemy.","color":"white","bold":false}]

execute if score lord_of_valor Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Fool, what do you think you're doing up here? Nothing in this realm can harm me, the Seven Lords are broken. Begone with you.","color":"white","bold":false}]

execute if score lord_of_valor Story matches 3 positioned 10392 171 -12 if entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] positioned 10396 170 -12 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Is this a challenge? Why would you approach me without","color":"white"},{"text":" everyone here","color":"aqua"},{"text":" first?.","color":"white","bold":false}]

execute if score lord_of_valor Story matches 3 positioned 10392 171 -12 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] positioned 10396 170 -12 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:overworld_cutscene/machine/0


#","color":"white"},{"text":"
