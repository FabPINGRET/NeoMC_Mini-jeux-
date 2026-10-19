# Malveth, l'archimage : guards
execute if entity @s[tag=mg.olshd] unless entity @e[tag=mg.olminion_malveth] run function mg:ombre/boss/malveth/unshield
execute if score $hp mg.st matches ..683 unless entity @s[tag=mg.olg1] run function mg:ombre/boss/malveth/shield
execute if score $hp mg.st matches ..341 unless entity @s[tag=mg.olg2] run function mg:ombre/boss/malveth/shield
