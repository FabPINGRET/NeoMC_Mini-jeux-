# Toutes les 2 s (core/tick) : l'objet 🎉 Emotes est retiré à qui ne le garde pas, rendu à qui l'a perdu
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{mg_emote:1b}] run kill @s
function mg:lobby/sit/item_purge
execute as @a unless function mg:lobby/sit/item_keep run clear @s *[minecraft:custom_data~{mg_emote:1b}]
execute as @a[tag=!mg.lsg,gamemode=!creative] if function mg:lobby/sit/item_keep run function mg:lobby/sit/item_check
