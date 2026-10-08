# Sous-pas de vol (macro x y z) : bloc plein devant → impact ; sinon le mouton avance
$execute positioned ~$(x) ~$(y) ~$(z) unless block ~ ~0.3 ~ #mg:sheep_pass run return run function mg:sheepwar/fly_hit
$tp @s ~$(x) ~$(y) ~$(z)
