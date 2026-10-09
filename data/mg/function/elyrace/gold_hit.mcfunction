# @s = joueur qui traverse un anneau d'or : turbo de 3 s (gravité renforcée pendant 60 ticks ; un 2e or le relance à pleine durée ;
# c<N>/player le termine, c<N>/respawn le coupe)
scoreboard players set @s mg.xu 60
attribute @s minecraft:gravity base set 0.13
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.4 0.4 0.3 25
tellraw @s [{"text":"★ Anneau d'or ! ","color":"gold","bold":true},{"text":"Turbo de 3 s : tu piques plus vite.","color":"gray"}]
