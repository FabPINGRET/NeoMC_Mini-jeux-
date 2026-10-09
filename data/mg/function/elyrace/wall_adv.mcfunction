# Avancement mg:elyrace_wall : le joueur (@s) vient de subir des dégâts de collision en vol
advancement revoke @s only mg:elyrace_wall
# solo : le joueur est dans sa phase de course (le solo ne passe pas par $game ni $state)
execute if entity @s[tag=mg.xso,scores={mg.xph=2}] run return run function mg:elyrace/wall
execute if entity @s[tag=mg.xso] run return 0
execute unless score $game mg.st matches 66 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play,scores={mg.xf=0}] run return 0
function mg:elyrace/wall
