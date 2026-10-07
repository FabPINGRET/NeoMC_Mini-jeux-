# Bloups : encre sur tous les pilotes devant soi
scoreboard players operation $kme mg.st = @s mg.krk
execute as @a[tag=mg.play] if score @s mg.krk < $kme mg.st run function mg:kart/inked
tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" envoie Bloups 🦑 sur les premiers !","color":"dark_purple"}]
