function music:end
execute as @a[tag=mg.flw] at @s run playsound minecraft:soundtrack.slime_man_action record @s ~ ~ ~ 1 1 1
scoreboard players set slime_man_theme_music Countdown 1099
