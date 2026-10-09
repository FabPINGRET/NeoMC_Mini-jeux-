# @s : la bombe touche (explosion selon le type, points au lanceur)
scoreboard players operation $bid mg.st = @s mg.bid
execute if score @s mg.bty matches 1 run function mg:bomber/boom/r3
execute if score @s mg.bty matches 2 run function mg:bomber/boom/r6
execute if score @s mg.bty matches 3 run function mg:bomber/boom/r3
execute if score @s mg.bty matches 4 run function mg:bomber/boom/r2
execute if score @s mg.bty matches 5 run function mg:bomber/boom/r11
execute if score @s mg.bty matches 1 run function mg:bomber/fx_small
execute if score @s mg.bty matches 3..4 run function mg:bomber/fx_small
execute if score @s mg.bty matches 2 run function mg:bomber/fx_big
execute if score @s mg.bty matches 5 run function mg:bomber/fx_nuke
execute if score $bk mg.st matches 1.. run summon minecraft:marker ~ ~ ~ {Tags:["mg.bsm"]}
scoreboard players operation $bpts mg.st = $bb mg.st
scoreboard players set #10 mg.st 10
scoreboard players operation $bpts mg.st *= #10 mg.st
scoreboard players operation $bpts mg.st += $bk mg.st
scoreboard players operation $bdes mg.st += $bk mg.st
scoreboard players operation $bdes mg.st += $bb mg.st
execute as @a[tag=mg.play] if score @s mg.bid = $bid mg.st run function mg:bomber/credit
kill @s
