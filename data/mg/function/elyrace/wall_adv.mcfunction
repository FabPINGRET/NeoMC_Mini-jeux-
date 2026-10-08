# Avancement mg:elyrace_wall : le joueur (@s) vient de subir des dégâts de collision en vol
advancement revoke @s only mg:elyrace_wall
execute unless score $game mg.st matches 66 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play,scores={mg.xf=0}] run return 0
function mg:elyrace/wall
