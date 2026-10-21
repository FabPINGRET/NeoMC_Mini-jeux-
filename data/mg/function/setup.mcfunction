# Installation (à lancer UNE fois par un OP) — règles + chargement des zones, puis construction

# Celui qui installe devient admin des mini-jeux
tag @s add mg.admin
# Lancé depuis la console/rcon (@s n'est pas un joueur) : personne n'est admin, le premier joueur qui rejoint le devient (à la première installation seulement)
execute if entity @s[type=minecraft:player] run scoreboard players set $adm mg.st 1
execute unless entity @s[type=minecraft:player] unless score $setup mg.st matches 1 run scoreboard players set $adm mg.st 0

# --- Règles de jeu (isolées dans core/rules pour la robustesse) ---
function mg:core/rules
time set noon
weather clear
difficulty normal

# --- Zones toujours chargées (lobby + arènes) ---
function mg:core/forceloads

# --- Construction différée (le temps que les chunks se chargent) ---
tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Chargement des zones... construction dans 3 secondes.","color":"gray"}]
schedule function mg:core/setup_build 3s
