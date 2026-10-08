# @s a utilisé /trigger mg.tel (1 = valider le livre)
execute unless score $state mg.st matches 2 run return run scoreboard players reset @s mg.tel
execute unless score $game mg.st matches 83 run return run scoreboard players reset @s mg.tel
execute unless score @s mg.ti matches 0.. run return run scoreboard players reset @s mg.tel
execute unless score $tp mg.st matches 0 unless score $tp mg.st matches 2 unless score $tp mg.st matches 4 run return run scoreboard players reset @s mg.tel
execute if entity @s[tag=mg.tdone] run tellraw @s {"text":"✔ Déjà validé (tu peux encore corriger : réécris puis valide à nouveau).","color":"gray"}
function mg:tel/read_book
scoreboard players reset @s mg.tel
