execute as @a[tag=mg.flw] unless score @s SoundtrackOverride matches 1 at @s if entity @s[x=-1000,dx=6000] run stopsound @s record
execute as @a[tag=mg.flw] unless score @s SoundtrackOverride matches 1 at @s if entity @s[x=9000,dx=6000] run stopsound @s record

execute as @a[tag=mg.flw] unless score @s SoundtrackOverride matches 1 at @s if entity @s[x=-1000,dx=6000] run playsound minecraft:soundtrack.3am record @s
execute as @a[tag=mg.flw] unless score @s SoundtrackOverride matches 1 at @s if entity @s[x=9000,dx=6000] run playsound minecraft:soundtrack.3am_dark record @s
