execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> That's it! This is how the furniture was when we were packing up to move. It made me think about how empty the room looked, especially because the","color":"white"},{"text":" ceiling was so high","color":"#44BBFF","italic":true},{"text":"!","color":"white","italic":false}]

return 1
