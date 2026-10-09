# @s : quille tombée en mouvement, un sous-pas (frottement, rebond sur les kickbacks, chocs en chaîne)
scoreboard players operation #ln mg.st = @s mg.bln
scoreboard players operation @s mg.bx += @s mg.bvx
scoreboard players operation @s mg.bz += @s mg.bvz
execute if score @s mg.bx matches 2300.. if score @s mg.bvx matches 1.. run function mg:bowl/kick
execute if score @s mg.bx matches ..-2300 if score @s mg.bvx matches ..-1 run function mg:bowl/kick
scoreboard players set #k mg.st 16
scoreboard players operation #q mg.st = @s mg.bvx
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation @s mg.bvx -= #q mg.st
scoreboard players operation #q mg.st = @s mg.bvz
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation @s mg.bvz -= #q mg.st
scoreboard players operation #ax mg.st = @s mg.bvx
execute if score #ax mg.st matches ..-1 run scoreboard players operation #ax mg.st *= #km1 mg.st
scoreboard players operation #az mg.st = @s mg.bvz
execute if score #az mg.st matches ..-1 run scoreboard players operation #az mg.st *= #km1 mg.st
scoreboard players operation #S mg.st = #ax mg.st
scoreboard players operation #S mg.st > #az mg.st
scoreboard players operation #q mg.st = #ax mg.st
scoreboard players operation #q mg.st < #az mg.st
scoreboard players set #k mg.st 2
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation #S mg.st += #q mg.st
execute if score #S mg.st matches ..24 run return run function mg:bowl/pin_stop
execute if score @s mg.bz matches 19501.. run return run function mg:bowl/pin_stop
scoreboard players operation #px mg.st = @s mg.bx
scoreboard players operation #pz mg.st = @s mg.bz
scoreboard players operation #mvx mg.st = @s mg.bvx
scoreboard players operation #mvz mg.st = @s mg.bvz
execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run function mg:bowl/pin_test
scoreboard players operation @s mg.bvx = #mvx mg.st
scoreboard players operation @s mg.bvz = #mvz mg.st
