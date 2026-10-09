# @s : temps écoulé sans finir le trou → compte 8
scoreboard players set @s mg.gfc 8
tellraw @a[tag=mg.play] [{"text":"⏱ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" n'a pas fini à temps (8 coups).","color":"gray"}]
function mg:golf/own
kill @e[tag=mg.gfmy]
function mg:golf/score
