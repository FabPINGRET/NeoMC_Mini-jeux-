# Position, dimension, point de réapparition et XP de @s (macro id)
$data modify storage mg:survie p.k$(id).pos set from entity @s Pos
$data modify storage mg:survie p.k$(id).rot set from entity @s Rotation
$data modify storage mg:survie p.k$(id).dim set from entity @s Dimension
$data remove storage mg:survie p.k$(id).resp
$data modify storage mg:survie p.k$(id).resp set from entity @s respawn
$execute store result storage mg:survie p.k$(id).xpl int 1 run xp query @s levels
$execute store result storage mg:survie p.k$(id).xpp int 1 run xp query @s points
