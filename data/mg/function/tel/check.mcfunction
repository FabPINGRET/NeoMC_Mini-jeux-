# Macro : la devinette $(k) de la chaîne $(c) est-elle le mot de départ ? +1 au devineur (a) et au constructeur (b)
$data modify storage mg:tel cmp set from storage mg:tel ch[$(c)].s0
$execute store success score $tneq mg.st run data modify storage mg:tel cmp set from storage mg:tel ch[$(c)].$(k)
execute if score $tneq mg.st matches 1 run return run tellraw @a[tag=!mg.surv] {"text":"     ✘ ce n'est plus le mot de départ…","color":"red"}
$scoreboard players add @a[scores={mg.ti=$(a)}] mg.tpt 1
$scoreboard players add @a[scores={mg.ti=$(b)}] mg.tpt 1
tellraw @a[tag=!mg.surv] {"text":"     ✔ C'EST LE MOT DE DÉPART ! +1 au devineur et au constructeur","color":"green","bold":true}
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2
