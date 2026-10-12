execute unless score $state mg.st matches 0 run return run tellraw @s {"text":"Une partie est en cours.","color":"red"}
execute if score $evon mg.st matches 1.. run return run tellraw @s {"text":"Un événement est déjà en cours (⛔ Arrêter dans le menu des événements).","color":"red"}
scoreboard players set $evn mg.st 60
scoreboard players set $evf mg.st 1
function mg:lobby/ev/pick
scoreboard players set $evf mg.st 0
scoreboard players set $evn mg.st 11
bossbar set mg:ev max 10
tellraw @s {"text":"✔ Événement lancé : il commence dans 10 s.","color":"green"}
