# @s sur un tremplin : envolée d'une seconde (macro : $(a) = force)
$effect give @s minecraft:levitation 1 $(a) true
effect give @s minecraft:slow_falling 3 0 true
playsound minecraft:entity.breeze.jump player @a ~ ~ ~ 0.8 1.2
particle minecraft:gust ~ ~0.2 ~ 0.3 0.1 0.3 0 3
