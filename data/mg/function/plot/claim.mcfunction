# Attribution d'un plot libre à @s (le numéro reste acquis dans mg.plot)
execute if score $pn mg.st matches 15.. run return run tellraw @s [{"text":"⚠ Les 15 plots sont déjà pris.","color":"red"}]
scoreboard players add $pn mg.st 1
scoreboard players operation @s mg.plot = $pn mg.st

# Pseudo du propriétaire (lu sur sa tête de joueur) pour le panneau du plot
loot replace entity @s hotbar.0 loot mg:plot_head
execute store result storage mg:plot cur.n int 1 run scoreboard players get @s mg.plot
data modify storage mg:plot cur.name set value ""
data modify storage mg:plot cur.name set from entity @s Inventory[{Slot:0b}].components."minecraft:profile".name
item replace entity @s hotbar.0 with minecraft:air
function mg:plot/owner_save with storage mg:plot cur

tellraw @a [{"selector":"@s","color":"yellow"},{"text":" prend le plot n°","color":"gray"},{"score":{"name":"@s","objective":"mg.plot"},"color":"gold"},{"text":" !","color":"gray"}]
