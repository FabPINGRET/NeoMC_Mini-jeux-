# Au chargement (/reload ou démarrage) : version des fichiers chargés + heure de jeu. Généré par tools/version/gen_version.py.
data remove storage mg:version files
function #mg:version
execute store result storage mg:version gt long 1 run time query gametime
