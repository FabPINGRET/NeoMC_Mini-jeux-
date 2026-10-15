# 🎄 Le lutin donne trois feux d'artifice (@s = joueur) ; appelé par lobby/theme/npc_use
execute if score @s mg.thc matches 1.. run return run title @s actionbar [{"text":"🎄 Reviens dans ","color":"green"},{"score":{"name":"@s","objective":"mg.thc"},"color":"yellow"},{"text":" s","color":"green"}]
execute store result score $thg mg.st run clear @s *[minecraft:custom_data~{mg_thg:1b}] 0
execute if score $thg mg.st matches 2.. run return run title @s actionbar {"text":"🎄 Utilise d'abord ton cadeau !","color":"green"}
give @s minecraft:firework_star[minecraft:custom_data={mg_thg:1b,mg_thfw:1b},minecraft:item_model="minecraft:firework_rocket",minecraft:custom_name={"text":"Feu d'artifice du lutin","color":"red","italic":false},minecraft:lore=[{"text":"Clic droit à ciel ouvert : il part tout seul.","color":"gray","italic":false}],minecraft:enchantment_glint_override=true,minecraft:consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:entity.firework_rocket.launch",has_consume_particles:false},minecraft:use_cooldown={seconds:1.5f}] 3
scoreboard players add @s mg.thfw 3
scoreboard players set @s mg.thc 30
execute at @s run playsound minecraft:block.note_block.bell neutral @a[distance=..16] ~ ~ ~ 1 1.2
execute at @e[type=minecraft:interaction,tag=mg.thnpci,limit=1] run particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0.05 15 normal
title @s actionbar {"text":"🎄 Joyeux Noël ! À lancer à ciel ouvert.","color":"green"}
