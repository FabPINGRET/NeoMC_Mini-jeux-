# Éliminé (@s) — macro {why}
$tellraw @a[tag=!mg.surv] [{"text":"🪽 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" $(why).","color":"gray"}]
scoreboard players reset @s mg.sks
scoreboard players set @s mg.skl 0
scoreboard players set @s mg.sko 0
effect clear @s minecraft:levitation
clear @s *[minecraft:custom_data~{mg_sky:1b}]
function mg:core/eliminate
