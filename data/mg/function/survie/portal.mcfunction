# Macro {x, z} : arrivée par un portail du Nether → même x / z dans le monde de survie, à la surface ; au-dessus de l'eau (spreadplayers échoue)
# → repli au point de départ du joueur (storage mg:survie id posé par from_overworld)
$execute in mg:survie store success score #sp mg.st run spreadplayers $(x) $(z) 0 1 false @s
execute if score #sp mg.st matches 0 run function mg:survie/home with storage mg:survie id
