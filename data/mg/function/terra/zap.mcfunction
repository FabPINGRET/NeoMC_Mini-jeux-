# @s (prédateur entré dans la colonie) : les tourelles du périmètre le frappent et le repoussent
damage @s 10 minecraft:lightning_bolt
particle minecraft:electric_spark ~ ~1 ~ 0.4 0.8 0.4 0.3 30
playsound minecraft:entity.lightning_bolt.impact hostile @a ~ ~ ~ 0.5 1.6
execute facing 0 65 0 rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.2}
function mg:terra/push
