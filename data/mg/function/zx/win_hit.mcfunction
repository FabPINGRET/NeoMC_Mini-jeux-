# Un zombie arrache une planche
scoreboard players remove @s mg.zws 1
function mg:zx/win_set
particle minecraft:block{block_state:"minecraft:spruce_planks"} ~ ~1 ~ 0.3 0.5 0.3 0 12
playsound minecraft:entity.zombie.attack_wooden_door hostile @a ~ ~ ~ 0.8 1
