# /function mg:setup_lobby (OP) : reconstruit seulement le spawn, ses constructions et son décor (pas les arènes ni les mondes)
execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : lance d'abord /function mg:setup","color":"red"}
execute if score $slb mg.st matches 1 run return run tellraw @s {"text":"⏳ Reconstruction du lobby déjà en cours.","color":"yellow"}
scoreboard players set $slb mg.st 1
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Reconstruction du lobby lancée (environ 1 minute)...","color":"gray"}]
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Reconstruction du lobby lancée (environ 1 minute)...","color":"gray"}]
data remove storage mg:lobby v6
data remove storage mg:lobby food1
data remove storage mg:lobby ely4
data remove storage mg:lobby elyclean6
data remove storage mg:lobby deco3
data remove storage mg:lobby decofix3
function mg:lobby/build
schedule function mg:lobby/food_build 20s
schedule function mg:elytra/spawn_clean 22s
schedule function mg:elytra/build 24s
schedule function mg:hall/build 26s
schedule function mg:pvpc/build_start 28s
schedule function mg:lobby/fish/build 30s
schedule function mg:hub/build 32s
schedule function mg:core/setup_lobby_done 60s
