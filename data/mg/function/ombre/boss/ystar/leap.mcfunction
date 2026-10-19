# Ysh'tar, la reine-araignée : leap
execute facing entity @p[tag=mg.olw,gamemode=adventure] feet rotated ~ -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.4}
function mg:ombre/push
playsound minecraft:entity.spider.step hostile @a ~ ~ ~ 2 0.5
