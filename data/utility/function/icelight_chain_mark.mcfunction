tag @s add icelight_marked
tag @s remove icelight_nexttarget

scoreboard players add icelight_chain Value 1

execute at @s if score icelight_chain Value matches ..9 if entity @e[tag=enemy,tag=!icelight_marked,distance=..15] run function utility:icelight_loop
