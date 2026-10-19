# Brennic, seigneur des brigands : charge
effect give @s minecraft:speed 3 3 true
playsound minecraft:entity.vindicator.celebrate hostile @a ~ ~ ~ 2 0.7
execute facing entity @a[tag=mg.olw,gamemode=adventure,sort=furthest,distance=..30,limit=1] feet rotated ~ -10 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.6}
function mg:ombre/push
