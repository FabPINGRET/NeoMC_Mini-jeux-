# Gel pendant le compte à rebours (@s = joueur) : plus de déplacement, de saut ni de coup (-100 %), retiré par core/unfreeze
attribute @s minecraft:movement_speed modifier add mg:freeze -1 add_multiplied_total
attribute @s minecraft:jump_strength modifier add mg:freeze -1 add_multiplied_total
attribute @s minecraft:entity_interaction_range modifier add mg:freeze -1 add_multiplied_total
