scoreboard players set @s mg.dlv 13
execute if score @s mg.dsk matches 1.. run return run function mg:dropadv/k_done
tellraw @a[tag=!mg.surv] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" termine les 13 niveaux du Dropper !","color":"yellow"}]
function mg:core/win_player
