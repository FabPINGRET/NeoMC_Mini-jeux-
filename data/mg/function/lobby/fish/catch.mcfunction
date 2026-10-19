# @s : a remonté sa ligne avec un objet (advancement mg:lobby_fish) : marque le joueur, pose un marqueur à l'hameçon, tire la prise
advancement revoke @s only mg:lobby_fish
tag @s add mg.lfc
execute as @e[type=minecraft:fishing_bobber,distance=..40] at @s on origin if entity @s[tag=mg.lfc] run summon minecraft:marker ~ ~ ~ {Tags:["mg.lfm","mg.lfx"]}
execute unless function mg:lobby/fish/keep run return run tag @e[type=minecraft:marker,tag=mg.lfx] remove mg.lfx
function mg:lobby/fish/roll
tag @e[type=minecraft:marker,tag=mg.lfx] remove mg.lfx
