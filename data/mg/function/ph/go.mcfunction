# Départ : 30 s pour se cacher
scoreboard players set $pht mg.st 0
scoreboard players set $phc mg.st 0
scoreboard players set @a mg.deaths 0
scoreboard players set @a[tag=mg.play] mg.phpt 0
execute as @a[tag=mg.phh] run function mg:ph/become_prop
execute as @a[tag=mg.phs] run function mg:ph/seeker_kit
effect give @a[tag=mg.phs] minecraft:blindness 31 0 true
execute if score $phm mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🏚 Manoir","color":"aqua","bold":true}]
execute if score $phm mg.st matches 2 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"⚓ Entrepôt du port","color":"aqua","bold":true}]
execute if score $phm mg.st matches 3 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🛒 Supermarché","color":"aqua","bold":true}]
execute if score $phm mg.st matches 4 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🌿 Serre","color":"aqua","bold":true}]
tellraw @a[tag=mg.phh] [{"text":"🎭 PROP HUNT : tu te caches ! ","color":"gold","bold":true},{"text":"Regarde un objet de la carte et ACCROUPIS-TOI pour en prendre l'apparence. Reste immobile 2 s pour te caler sur la grille. Les chercheurs arrivent dans 30 s ; toutes les 20 s tu fais un petit bruit, et ta corne (clic droit) en fait un quand tu veux. Attention : 5 cœurs seulement ! Points : plus un chercheur te regarde, plus tu en gagnes, et bouger en rapporte aussi.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🎭 Mode entraînement (seul) : tu es cacheur, essaie les déguisements (accroupi devant un objet) et le calage sur la grille. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}]
tellraw @a[tag=mg.phs] [{"text":"🎭 PROP HUNT — tu cherches ! ","color":"red","bold":true},{"text":"Les cacheurs se transforment en objets du manoir. Tu es libéré dans 30 s : frappe les objets suspects, écoute les bruits !","color":"gray"}]
