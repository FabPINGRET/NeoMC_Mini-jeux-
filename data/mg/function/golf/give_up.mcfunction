# @s : 8 coups sans rentrer la balle → trou abandonné (compte 8)
scoreboard players set @s mg.gfc 8
tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" abandonne le trou (8 coups).","color":"gray"}]
function mg:golf/own
kill @e[tag=mg.gfmy]
function mg:golf/score
