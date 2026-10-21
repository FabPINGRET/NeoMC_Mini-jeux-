# Contexte : dimension. Rouvre toute porte sans drapeau si un joueur d'Ombrelune a dépassé son étape (coins chargés requis)
execute unless data storage mg:ombre doors.kgate if loaded -4 67 140 if loaded 4 79 141 if entity @a[tag=mg.olw,scores={mg.olch=42..}] run function mg:ombre/door/kgate_open
execute unless data storage mg:ombre doors.citadel if loaded -158 67 176 if loaded -158 72 180 if entity @a[tag=mg.olw,scores={mg.olch=48..}] run function mg:ombre/door/citadel_open
execute unless data storage mg:ombre doors.pyramid if loaded 197 65 -39 if loaded 199 67 -39 if entity @a[tag=mg.olw,scores={mg.olch=33..}] run function mg:ombre/door/pyramid_open
