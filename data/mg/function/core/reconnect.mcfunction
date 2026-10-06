# Joueur qui revient après une déconnexion (@s = joueur)
scoreboard players reset @s mg.lg

# Partie en cours (compte à rebours, jeu ou fin) → il rejoint l'arène en SPECTATEUR
execute if score $state mg.st matches 1..3 run return run function mg:core/reconnect_spec

# Sinon → lobby, inventaire vidé
function mg:core/reset_player
tellraw @s [{"text":"Bon retour ! Tu as été replacé au lobby.","color":"gray"}]
