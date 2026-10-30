execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if block 10022 59 -113 sculk run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> By order of ","color":"white"},{"text":"Lord Morbex","color":"dark_aqua"},{"text":", no one is allowed inside Valor Tower! You are not worthy of his presence, stranger. He is the emissary of the glorious ","color":"white"},{"text":"World Virus ","color":"dark_aqua"},{"text":"itself.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless block 10022 59 -113 sculk run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> By order of ","color":"white"},{"text":"Lord Morbex","color":"dark_aqua"},{"text":", no one is allowed inside Valor Tower!\n\n... Wait, what? Why is the door open?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
