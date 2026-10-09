# Dégèle (@s = joueur) : retire les modificateurs de core/freeze et le verrou de position (sans effet s'ils ne sont pas posés)
attribute @s minecraft:movement_speed modifier remove mg:freeze
attribute @s minecraft:jump_strength modifier remove mg:freeze
attribute @s minecraft:entity_interaction_range modifier remove mg:freeze
tag @s remove mg.frz
