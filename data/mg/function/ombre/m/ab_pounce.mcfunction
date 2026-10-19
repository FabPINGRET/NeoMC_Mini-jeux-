# Loup-garou : bond sur sa proie
execute facing entity @p[tag=mg.olw,gamemode=adventure] feet rotated ~ -18 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.1}
function mg:ombre/push
playsound minecraft:entity.wolf.growl hostile @a ~ ~ ~ 1.2 0.6
