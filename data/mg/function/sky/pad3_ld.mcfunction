# 1 si la plateforme est chargée
execute unless loaded -8 195 28992 run return fail
execute unless loaded -8 195 29008 run return fail
execute unless loaded 8 195 28992 run return fail
execute unless loaded 8 195 29008 run return fail
return 1
