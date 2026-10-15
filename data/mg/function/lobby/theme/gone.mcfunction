# Retire un animal du thème sans animation de mort ni butin (@s)
# bonhomme de neige : la traînée sous ses pieds fond (ses pieds seulement : ses points d'apparition sont de l'air d'origine)
execute if entity @s[type=minecraft:snow_golem] at @s if block ~ ~ ~ minecraft:snow[layers=1] run setblock ~ ~ ~ minecraft:air
execute on passengers run kill @s[type=minecraft:item_display]
execute at @s run tp @s ~ -300 ~
kill @s
