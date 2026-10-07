# Nouveau joueur de la survie : numéro et coffres de sauvegarde
execute if score $svc mg.st matches 255.. run return run tellraw @s [{"text":"⚠ Plus de place pour de nouveaux joueurs en survie (255).","color":"red"}]
scoreboard players add $svc mg.st 1
scoreboard players operation @s mg.svid = $svc mg.st
scoreboard players set @s mg.svvx 30000
scoreboard players operation @s mg.svvx += @s mg.svid
execute store result storage mg:survie id.x int 1 run scoreboard players get @s mg.svvx
function mg:survie/vault_make with storage mg:survie id
