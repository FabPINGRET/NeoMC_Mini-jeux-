# Macro : note $(k) de la construction de la chaîne $(c) (constructeur a) → points au constructeur
$execute store result score $tsv mg.st run data get storage mg:tel ch[$(c)].$(k)
execute unless score $tsv mg.st matches 1..5 run return run tellraw @a[tag=!mg.surv] {"text":"     (pas de note)","color":"dark_gray"}
$scoreboard players operation @a[scores={mg.ti=$(a)}] mg.tpt += $tsv mg.st
execute if score $tsv mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"     ★☆☆☆☆","color":"gold"},{"text":"  +1 point(s) au constructeur","color":"gray"}]
execute if score $tsv mg.st matches 2 run tellraw @a[tag=!mg.surv] [{"text":"     ★★☆☆☆","color":"gold"},{"text":"  +2 point(s) au constructeur","color":"gray"}]
execute if score $tsv mg.st matches 3 run tellraw @a[tag=!mg.surv] [{"text":"     ★★★☆☆","color":"gold"},{"text":"  +3 point(s) au constructeur","color":"gray"}]
execute if score $tsv mg.st matches 4 run tellraw @a[tag=!mg.surv] [{"text":"     ★★★★☆","color":"gold"},{"text":"  +4 point(s) au constructeur","color":"gray"}]
execute if score $tsv mg.st matches 5 run tellraw @a[tag=!mg.surv] [{"text":"     ★★★★★","color":"gold"},{"text":"  +5 point(s) au constructeur","color":"gray"}]
