# @s (carnotaure) : casse les structures légères autour de lui (outposts)
execute store result score $tvb2 mg.st run fill ~-2 ~ ~-2 ~2 ~3 ~2 minecraft:air replace #mg:tv_light
execute if score $tvb2 mg.st matches 1.. run playsound minecraft:entity.zombie.break_wooden_door hostile @a ~ ~ ~ 1 0.7
execute if score $tvb2 mg.st matches 1.. run particle minecraft:block{block_state:"minecraft:oak_planks"} ~ ~1 ~ 1 1 1 0 30
