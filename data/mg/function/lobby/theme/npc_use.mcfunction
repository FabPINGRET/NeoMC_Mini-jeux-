# @s : zone cliquable du PNJ cliqué (appelé chaque tick par lobby/theme/tick) : cadeau du thème en place
execute if data entity @s interaction on target if entity @s[tag=!mg.play,tag=!mg.surv,gamemode=!spectator] if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/npc_give
execute if data entity @s interaction on target if entity @s[tag=!mg.play,tag=!mg.surv,gamemode=!spectator] if score $theme mg.st matches 2 run function mg:lobby/theme/noel/npc_give
execute if data entity @s attack on attacker if entity @s[tag=!mg.play,tag=!mg.surv,gamemode=!spectator] if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/npc_give
execute if data entity @s attack on attacker if entity @s[tag=!mg.play,tag=!mg.surv,gamemode=!spectator] if score $theme mg.st matches 2 run function mg:lobby/theme/noel/npc_give
data remove entity @s interaction
data remove entity @s attack
