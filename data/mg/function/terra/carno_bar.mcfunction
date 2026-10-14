# @s (carnotaure) : barre de vie pour les colons proches
execute store result bossbar mg:tvcarno value run data get entity @s Health
bossbar set mg:tvcarno players @a[tag=mg.tvw,distance=..48]
