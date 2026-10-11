execute unless score $state mg.st matches 0 run return run tellraw @s {"text":"Une partie est en cours.","color":"red"}
scoreboard players set $evn mg.st 60
function mg:lobby/ev/pick
scoreboard players set $evn mg.st 11
