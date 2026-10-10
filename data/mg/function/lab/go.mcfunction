# Départ
scoreboard players set $lbt mg.st 0
effect give @a[tag=mg.lbw] minecraft:blindness infinite 0 true
effect give @a[tag=mg.lbw] minecraft:darkness infinite 0 true
effect give @a[tag=mg.lbg] minecraft:night_vision infinite 0 true
effect give @a[tag=mg.lbw] minecraft:glowing infinite 0 true
bossbar add mg:lab {"text":"🙈 Labyrinthe aveugle","color":"light_purple"}
bossbar set mg:lab color purple
bossbar set mg:lab max 4800
bossbar set mg:lab players @a[tag=mg.play]
execute as @a[tag=mg.lbw] run function mg:lab/brief
