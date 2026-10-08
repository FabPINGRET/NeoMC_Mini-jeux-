# Une fusée pour chaque survivant
give @a[tag=mg.play] minecraft:firework_rocket[minecraft:custom_data={mg_sky:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du ciel","color":"gold","italic":false}] 1
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 1.4
