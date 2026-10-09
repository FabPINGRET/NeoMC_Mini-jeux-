"""Régénère la dimension mg:survie d'un monde (serveur ARRÊTÉ) : sauvegarde, efface le terrain, active les structures.

    python3 regen_survie.py <dossier world> [--dry]

- sauvegarde world/dimensions/mg/survie dans survie-backup-<date>.tar.gz (à côté du dossier world)
- supprime region/, entities/, poi/ de la dimension (le terrain sera régénéré avec la même graine)
- passe generate_structures à 1 dans dimensions/mg/survie/data/minecraft/world_gen_settings.dat
Inventaires, coffres de sauvegarde (monde des mini-jeux) et données des joueurs ne sont pas touchés.
"""
import gzip, os, shutil, sys, tarfile, time

W = sys.argv[1]
DRY = '--dry' in sys.argv
D = os.path.join(W, 'dimensions', 'mg', 'survie')
DAT = os.path.join(D, 'data', 'minecraft', 'world_gen_settings.dat')
assert os.path.isdir(D), f'dimension introuvable : {D}'
raw = gzip.open(DAT).read()
key = b'\x01\x00\x13generate_structures'
i = raw.find(key)
assert i >= 0, 'generate_structures introuvable'
print('generate_structures actuel =', raw[i + len(key)])
if DRY:
    sys.exit(0)
bk = os.path.join(os.path.dirname(os.path.abspath(W)), time.strftime('survie-backup-%Y%m%d-%H%M%S.tar.gz'))
with tarfile.open(bk, 'w:gz') as t:
    t.add(D, arcname='survie')
print('sauvegarde :', bk)
for sub in ('region', 'entities', 'poi'):
    p = os.path.join(D, sub)
    if os.path.isdir(p):
        shutil.rmtree(p); print('supprimé :', p)
raw = raw[:i + len(key)] + b'\x01' + raw[i + len(key) + 1:]
with gzip.open(DAT, 'wb') as f:
    f.write(raw)
print('generate_structures = 1')
