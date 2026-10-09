# Départ : 30 s pour se cacher
scoreboard players set $pht mg.st 0
scoreboard players set $phc mg.st 0
scoreboard players set @a mg.deaths 0
execute as @a[tag=mg.phh] run function mg:ph/become_prop
execute as @a[tag=mg.phs] run function mg:ph/seeker_kit
effect give @a[tag=mg.phs] minecraft:blindness 31 0 true
tellraw @a[tag=mg.phh] [{"text":"🎭 PROP HUNT — tu te caches ! ","color":"gold","bold":true},{"text":"Regarde un objet du manoir et ACCROUPIS-TOI pour en prendre l'apparence. Reste immobile 2 s pour te caler sur la grille. Les chercheurs arrivent dans 30 s ; toutes les 20 s tu fais un petit bruit, et ta corne (clic droit) en fait un quand tu veux. Attention : 5 cœurs seulement !","color":"gray"}]
tellraw @a[tag=mg.phs] [{"text":"🎭 PROP HUNT — tu cherches ! ","color":"red","bold":true},{"text":"Les cacheurs se transforment en objets du manoir. Tu es libéré dans 30 s : frappe les objets suspects, écoute les bruits !","color":"gray"}]
