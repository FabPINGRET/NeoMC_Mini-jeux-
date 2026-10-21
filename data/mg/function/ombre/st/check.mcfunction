# Au chargement : entités permanentes à (re)poser si le datapack les a changées
execute unless data storage mg:ombre built run return 0
execute unless data storage mg:ombre {sv:2087534156} run function mg:ombre/st/start
