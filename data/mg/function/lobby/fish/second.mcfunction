# Toutes les 2 s (core/tick : $lan mg.t = 30, chunk du socle chargé) : cannes, stat de lancers, entités du socle
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{mg_rod:1b}] run kill @s
function mg:lobby/fish/purge
execute as @a unless function mg:lobby/fish/keep run clear @s *[minecraft:custom_data~{mg_rod:1b}]
# lancers : stat vanilla used:fishing_rod (lancer et remontée comptent chacun), reportée dans $use (seulement pour qui passe keep), remise à zéro pour tous
execute as @a[scores={mg.lfu=1..}] if function mg:lobby/fish/keep run scoreboard players operation $use mg.lfn += @s mg.lfu
scoreboard players set @a[scores={mg.lfu=1..}] mg.lfu 0
# socle : deux entités (zone cliquable et panneau), refaites s'il en manque ; coupé par un admin : plus rien
execute if score $lfoff mg.st matches 1 run return 0
execute store result score #lfe mg.st if entity @e[tag=mg.lfs]
execute unless score #lfe mg.st matches 2 if block 36 64 -27 minecraft:spruce_log run function mg:lobby/fish/entities
