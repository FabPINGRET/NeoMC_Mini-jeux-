execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> I saw you enter the pool, but I'm unable to see where you are now. Hopefully that means you've found the location of the ","color":"white"},{"text":"Dreadwarden","color":"aqua"},{"text":". I'll see you upon your safe return, hero!","color":"white"}]

return 1
