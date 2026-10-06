# Attente d'un achat (trigger mg.dice 31..33, 39 = partir), fermeture au bout de 15 s
scoreboard players remove $mpw mg.st 1
execute if entity @a[tag=mg.mpcur,scores={mg.dice=31}] as @a[tag=mg.mpcur] run return run function mg:party/buy {n:"mid",p:10,t:"🎲🎲 un dé double"}
execute if entity @a[tag=mg.mpcur,scores={mg.dice=32}] as @a[tag=mg.mpcur] run return run function mg:party/buy {n:"mit",p:18,t:"🎲🎲🎲 un dé triple"}
execute if entity @a[tag=mg.mpcur,scores={mg.dice=33}] as @a[tag=mg.mpcur] run return run function mg:party/buy {n:"mip",p:15,t:"🔀 un tuyau"}
execute if entity @a[tag=mg.mpcur,scores={mg.dice=39}] run return run function mg:party/shop_close
execute if score $mpw mg.st matches ..0 run function mg:party/shop_close
execute unless entity @a[tag=mg.mpcur] run function mg:party/shop_close
