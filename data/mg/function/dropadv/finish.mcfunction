scoreboard players set @s mg.dlv 10
tellraw @a[tag=!mg.surv] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" termine les 10 niveaux du Dropper !","color":"yellow"}]
function mg:core/win_player
