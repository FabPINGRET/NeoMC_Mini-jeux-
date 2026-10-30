execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if block 9981 49 -160 minecraft:ancient_debris at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phanios","color":"#D47453"},{"text":"> The tunnel was going well, but I've hit a rough patch. Stranger, do you know anyone who is ","color":"white"},{"text":"really good at digging","color":"aqua"},{"text":"? Someone","color":"white"},{"text":" experienced at digging tunnels","color":"aqua"},{"text":"? If so, ","color":"white"},{"text":"please tell them we need help","color":"gold"},{"text":" to dig into the prison.","color":"white"}]
execute if block 9981 49 -160 minecraft:air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phanios","color":"#D47453"},{"text":"> What the... some kid just ripped through here and finished the tunnel so quickly I hardly had time to blink. I think he dug ","color":"white"},{"text":"straight through the prison","color":"gold"},{"text":" and ","color":"white"},{"text":"into the basement of Valor Tower","color":"gold"},{"text":". If you can get to the top of Valor Tower through here, you could challenge ","color":"white"},{"text":"Lord Morbex","color":"dark_aqua"},{"text":"!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]
execute if score cinder_concord Story matches 0 run scoreboard players set cinder_concord Story 1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
