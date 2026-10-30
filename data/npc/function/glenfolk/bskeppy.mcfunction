execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute unless score bskeppy Value matches 4.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"B'Skeppy","color":"aqua"},{"text":"> Weeeeeelcome to my hidden gallery! Each of my paintings is of a specific view in the Floaty Isles. If you were to ","color":"white"},{"text":"visit each of the 4 spots I painted these paintings from","color":"aqua"},{"text":", you would understand how beeeeeautiful these views are! It would make me ","color":"white"},{"text":"veeeeery happy","color":"red"},{"text":"! Remember, go to the","color":"white"},{"text":" spot where your perspective matches the paintings","color":"aqua"},{"text":", those are the best views!","color":"white"}]
execute if score bskeppy Value matches 4.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"B'Skeppy","color":"aqua"},{"text":"> I see through your pupils, your soul is gleeeeaming with wonder! You've seen these views with your own eyes! How maaaaaarvelous to know that another life has beheld these most wonderous sights. This makes me ","color":"white"},{"text":"incredibly, incredibly happy","color":"red"},{"text":"!","color":"white"}]
execute if score bskeppy Value matches 4.. run setblock -150 33 -96 minecraft:redstone_block
execute if score bskeppy Value matches 4.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force 
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

#set views, latch
setblock -155 33 -96 minecraft:redstone_block
