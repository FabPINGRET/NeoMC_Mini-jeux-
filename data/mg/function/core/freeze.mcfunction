# Gel pendant le compte à rebours (@s = joueur), retiré par core/unfreeze :
# - pas de saut ni de coup (-100 %) ;
# - position x/z verrouillée par core/freeze_hold (chaque tick) au lieu d'une vitesse à -100 % : plus de zoom de l'écran
attribute @s minecraft:jump_strength modifier add mg:freeze -1 add_multiplied_total
attribute @s minecraft:entity_interaction_range modifier add mg:freeze -1 add_multiplied_total
function mg:core/freeze_anchor
tag @s add mg.frz
