# @s (Quick Revive) : relevé au bout de 5 s
scoreboard players remove @s mg.zrt 1
execute if score @s mg.zrt matches 1.. run return 0
tag @s remove mg.zqrw
tellraw @a[tag=mg.play] [{"text":"💙 ","color":"aqua"},{"selector":"@s","color":"aqua"},{"text":" est relevé par sa Quick Revive !","color":"gray"}]
function mg:zm3/revive
