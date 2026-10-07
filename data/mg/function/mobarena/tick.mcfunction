# Mob Arena — tick de jeu

# Phase de pause entre les vagues
execute if score $wt mg.st matches 1.. run function mg:mobarena/pause_tick
# Phase de combat
execute if score $wt mg.st matches ..0 run function mg:mobarena/fight_tick

# Scoreboard latéral (vague, monstres restants, joueurs en vie) + barre de vie du boss
execute store result score Monstres_restants mg.mb if entity @e[tag=mg.mob]
execute store result score Joueurs_en_vie mg.mb if entity @a[tag=mg.play]
function mg:mobarena/boss_bar

# Pyromane : clic droit avec la "boule de feu" (snowball) → vraie boule de feu
execute as @a[tag=mg.play,scores={mg.us=1..}] at @s run function mg:mobarena/fb_use

# Il reste 3 monstres ou moins → surlignés (visibles à travers les murs)
execute if score Monstres_restants mg.mb matches 1..3 run effect give @e[tag=mg.mob] minecraft:glowing 2 0 true
execute if score Monstres_restants mg.mb matches 1..3 if score $gl mg.st matches 0 run function mg:mobarena/glow_notice

# Monstre échappé ou tombé → replacé au centre
execute if score $mt mg.st matches ..5 as @e[tag=mg.mob] at @s positioned 0 64 1800 unless entity @s[distance=..26] run tp @s 0.5 64 1800.5

# Morts → spectateur
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Tout le monde est tombé → défaite
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:mobarena/defeat

# Shulkers : ils se téléportent quand on les touche → s'ils sortent de l'arène, retour sur un point d'appui
execute if score $mt mg.st matches 2 as @e[type=minecraft:shulker,tag=mg.mob] at @s unless entity @s[x=-14,y=63,z=1786,dx=28,dy=10,dz=28] run function mg:mobarena/shulker_home
execute if score $mt mg.st matches 10 as @e[type=minecraft:shulker,tag=mg.mob] at @s unless entity @s[x=-22,y=64,z=10678,dx=44,dy=30,dz=44] run function mg:mobarena/shulker_home

# Thèmes à 20 vagues : horloge, retour des monstres échappés, mécaniques propres à chaque arène
execute if score $mt mg.st matches 6..10 run scoreboard players add $bt mg.st 1
execute if score $mt mg.st matches 6 as @e[tag=mg.mob] at @s positioned 0 65 9100 unless entity @s[distance=..36] run tp @s 0.5 65 9100.5
execute if score $mt mg.st matches 7 as @e[tag=mg.mob] at @s positioned 0 65 9500 unless entity @s[distance=..30] run tp @s 0.5 65 9500.5
execute if score $mt mg.st matches 8 as @e[tag=mg.mob] at @s positioned 0 64 9900 unless entity @s[distance=..36] run tp @s 0.5 64 9910.5
execute if score $mt mg.st matches 9 as @e[tag=mg.mob] at @s positioned 0 66 10300 unless entity @s[distance=..40] run tp @s 0.5 66 10300.5
execute if score $mt mg.st matches 10 as @e[tag=mg.mob] at @s positioned 0 65 10700 unless entity @s[distance=..32] run tp @s 0.5 65 10689.5
execute if score $mt mg.st matches 6 run function mg:mobarena/cathedral/tick
execute if score $mt mg.st matches 7 run function mg:mobarena/lab/tick
execute if score $mt mg.st matches 8 run function mg:mobarena/temple/tick
execute if score $mt mg.st matches 9 run function mg:mobarena/forge/tick
execute if score $mt mg.st matches 10 run function mg:mobarena/ship/tick
# Le temps n'est plus figé à minuit (survie) : les monstres ne brûlent pas au soleil
execute as @e[tag=mg.mob,tag=!mg.fr] run function mg:mobarena/fire_res
