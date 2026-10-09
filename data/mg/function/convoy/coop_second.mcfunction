# Coop : dégâts au convoi, vague toutes les 8 s
execute at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cvn mg.st if entity @e[tag=mg.cvm,distance=..3]
scoreboard players operation $cvh mg.st -= $cvn mg.st
scoreboard players operation $cvh mg.st -= $cvn mg.st
execute if score $cvn mg.st matches 1.. at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run particle minecraft:damage_indicator ~ ~1 ~ 0.4 0.3 0.4 0 3
execute if score $state mg.st matches 2 if score $cvh mg.st matches ..0 run return run function mg:convoy/coop_lose
kill @e[type=minecraft:item,x=-75,y=60,z=21185,dx=150,dy=50,dz=30]
scoreboard players add $cvw mg.st 1
execute if score $cvw mg.st matches 8.. run function mg:convoy/wave
