execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Vyrn the Artificer","color":"#D47453"},{"text":"> Ah, a non-Pygmy! Maybe you will appreciate my ","color":"white"},{"text":"Aegiscraft","color":"gold"},{"text":". In the center of the room is my Device; it can empower your shield with what I'm calling ","color":"white"},{"text":"Vyrn's Enfeeblement","color":"green"},{"text":"! It's a retributive modification that temporarily weakens foes who hit your shield, severely lowering their strength for a couple seconds. If you have a ","color":"white"},{"text":"shield","color":"aqua"},{"text":" please give it a try!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
