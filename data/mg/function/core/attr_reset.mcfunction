# Remet le recul des explosions à la normale pour @s (isolé)
attribute @s minecraft:explosion_knockback_resistance base set 0
attribute @s minecraft:movement_speed base set 0.1
attribute @s minecraft:jump_strength base set 0.42
attribute @s minecraft:fall_damage_multiplier base set 0
# Prop Hunt (cacheurs à 5 cœurs) : vie max normale au retour
attribute @s minecraft:max_health base set 20
function mg:core/attr_reset_g
function mg:core/unfreeze
