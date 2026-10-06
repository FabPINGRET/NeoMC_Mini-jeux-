# Installation (à lancer UNE fois par un OP) — règles + chargement des zones, puis construction

# Celui qui installe devient admin des mini-jeux
tag @s add mg.admin

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
