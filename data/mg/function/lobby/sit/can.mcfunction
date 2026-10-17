# @s : peut s'asseoir / faire une emote ? Retourne 1 ou 0 ; refus : message court en actionbar
execute if score $sitoff mg.st matches 1 run title @s actionbar {"text":"🪑 Assis et emotes désactivés par un admin.","color":"gray"}
execute if score $sitoff mg.st matches 1 run return 0
execute unless function mg:lobby/sit/ok run title @s actionbar {"text":"🪑 Pas possible ici (au spawn, hors activité).","color":"gray"}
execute unless function mg:lobby/sit/ok run return 0
# déjà dans un véhicule (kart, montagne russe...) : non ; assis, c'est notre propre siège
execute unless entity @s[tag=mg.sit] if predicate mg:in_vehicle run title @s actionbar {"text":"🪑 Descends d'abord de ton véhicule.","color":"gray"}
execute unless entity @s[tag=mg.sit] if predicate mg:in_vehicle run return 0
return 1
