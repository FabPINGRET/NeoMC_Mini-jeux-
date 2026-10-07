# Entretien chaque seconde
scoreboard players set $svt mg.st 0
function mg:survie/sweep_mobs
# Lobby et mini-jeux : pas de dégâts de chute, vision nocturne (la nuit existe maintenant pour la survie)
execute as @a[tag=!mg.surv] run attribute @s minecraft:fall_damage_multiplier base set 0
effect give @a[tag=!mg.surv] minecraft:night_vision infinite 0 true
# Survie : la nuit passe quand tous les joueurs du monde de survie dorment
function mg:survie/sleep
