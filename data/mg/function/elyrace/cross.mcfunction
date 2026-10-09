# macro : $(p) = plan de l'anneau (x, centiemes), $(yl)..$(yh) et $(zl)..$(zh) = trou (voir sweep.bounds) ; appelee seulement quand
# l'origine #xox est avant le plan et la position #xqx apres (donc #xqd >= 1). #xhit = 1 si le segment origine -> position coupe le trou
scoreboard players set #xhit mg.st 0
$scoreboard players set #xta mg.st $(p)
scoreboard players operation #xta mg.st -= #xox mg.st
scoreboard players operation #xiy mg.st = #xqy mg.st
scoreboard players operation #xiy mg.st -= #xoy mg.st
scoreboard players operation #xiy mg.st *= #xta mg.st
scoreboard players operation #xiy mg.st /= #xqd mg.st
scoreboard players operation #xiy mg.st += #xoy mg.st
scoreboard players operation #xiz mg.st = #xqz mg.st
scoreboard players operation #xiz mg.st -= #xoz mg.st
scoreboard players operation #xiz mg.st *= #xta mg.st
scoreboard players operation #xiz mg.st /= #xqd mg.st
scoreboard players operation #xiz mg.st += #xoz mg.st
# ordre de deplacement de Minecraft (Y, puis axe horizontal le plus long, puis autre axe) : trois points du trajet testes, comme sweep.hits
# (#xiy,#xiz) = point du segment droit ; (#xqy,#xoz) et (#xqy,#xqz) = trajets en equerre
$execute if score #xiy mg.st matches $(yl)..$(yh) if score #xiz mg.st matches $(zl)..$(zh) run scoreboard players set #xhit mg.st 1
$execute if score #xqy mg.st matches $(yl)..$(yh) if score #xoz mg.st matches $(zl)..$(zh) run scoreboard players set #xhit mg.st 1
$execute if score #xqy mg.st matches $(yl)..$(yh) if score #xqz mg.st matches $(zl)..$(zh) run scoreboard players set #xhit mg.st 1
