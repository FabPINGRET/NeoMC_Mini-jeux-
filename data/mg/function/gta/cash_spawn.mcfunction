# Une valise de billets (+75 $) sur ce trottoir
scoreboard players set $gcv mg.st 75
execute positioned ~ ~0.8 ~ run function mg:gta/cash_new
tellraw @a[tag=mg.gtw] {"text":"💰 Une valise de billets est apparue quelque part en ville !","color":"green"}
