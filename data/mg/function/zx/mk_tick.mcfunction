# @s : grenade singe posée (3 s) : les zombies à 24 blocs marchent vers elle (sans traverser les murs)
scoreboard players add @s mg.zmc 1
tp @s ~ ~ ~ ~18 ~
execute as @e[tag=mg.zz,distance=..24] at @s facing entity @e[type=minecraft:item_display,tag=mg.zmk,sort=nearest,limit=1] feet rotated ~ 0 positioned ^ ^ ^0.2 if block ~ ~0.1 ~ #mg:ray_pass if block ~ ~1.1 ~ #mg:ray_pass unless entity @e[type=minecraft:item_display,tag=mg.zmk,distance=..1.2] run tp @s ~ ~ ~ ~ ~
scoreboard players operation $zq mg.st = @s mg.zmc
scoreboard players set #5 mg.st 5
scoreboard players operation $zq mg.st %= #5 mg.st
execute if score $zq mg.st matches 0 run particle minecraft:note ~ ~0.6 ~ 0.3 0.3 0.3 1 2
execute if score $zq mg.st matches 0 run playsound minecraft:block.note_block.bell master @a ~ ~ ~ 1.5 1.8
execute if score @s mg.zmc matches 60.. run function mg:zx/mk_boom
