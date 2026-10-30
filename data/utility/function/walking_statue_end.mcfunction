execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta run fill ~ ~ ~ ~ ~1 ~ chiseled_deepslate replace air
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run particle block{block_state:"chiseled_deepslate"} ~ ~1 ~ 0.5 1 0.5 0 150
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run particle block{block_state:"polished_deepslate"} ~ ~1 ~ 0.5 1 0.5 0 150
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run particle composter ~ ~1 ~ 0.5 1 0.5 0 75

execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run playsound minecraft:block.stone.break master @a[tag=mg.flw] ~ ~ ~ 1 1 
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run playsound minecraft:entity.iron_golem.hurt master @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta align xz run playsound minecraft:item.wolf_armor.repair master @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta run tp @s ~ -100 ~
execute if block ~ ~-0.1 ~ minecraft:lime_glazed_terracotta run kill @s
