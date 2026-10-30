"""Invariants du pack serveur / optionnel (tools/resourcepack/floaty_split.py) : verifie() sur la sortie, puis sur des sorties falsifiées (cas inverses).
Fixtures synthétiques partagées avec test_floaty_split.py (importées : pas de jar, de carte ni de manifeste commité).
- le pack serveur ne contient aucun chemin « remplacé » sauf les items/X.json enveloppés (select minecraft:context_dimension, UN cas mg:floaty,
  repli = définition vanilla à l'identique, sans floaty:), ni X.png.mcmeta dont X.png est remplacé ;
- le pack optionnel est disjoint du pack serveur : ni items/, ni assets/mg, ni lang/, ni assets/floaty ; les écartés ne sont dans aucun ;
- toute référence floaty: pointe sur un fichier du pack serveur ;
- le pack optionnel ne reçoit que des remplacements (rien de neuf) ; chaque item attendu du manifeste est enveloppé dans le pack serveur ;
- aucun fichier de la carte n'est perdu : tout fichier non écarté est dans l'un des deux packs, à sa place (renommé sous assets/floaty/ si besoin).
Le vrai manifeste commité est aussi passé à la scission, sur une carte factice qui a tous ses chemins remplacés.
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import copy
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))          # fixtures de test_floaty_split (même dossier, comme test_floaty_chunks)
from test_floaty_split import APPLE, EXTRA, MANIFEST, MAP_SWORD, MC, RP, SWORD, fs, js, mdl, split  # noqa: E402


def verifie(server, opt, man, extra=EXTRA):
    """Violations des invariants sur (serveur, optionnel) pour la carte extra : liste de messages, vide si tout est bon."""
    bad = []
    replaced = {p for paths in man['replaced'].values() for p in paths}
    wrapped = set(man['items'])
    for p in sorted(wrapped):
        if p not in server:
            bad.append(f'serveur : item enveloppé absent {p}')
    for p in sorted(opt):
        if p not in replaced:
            bad.append(f'optionnel : pas un remplacement {p}')
    for p in sorted(extra):
        if p in man['dropped']:
            continue
        if p not in replaced or p.startswith(MC + 'items/'):
            want, pack = p, server
        elif p.startswith((MC + 'textures/item/', MC + 'models/item/')):
            want, pack = 'assets/floaty/' + p[len(MC):], server
        else:
            want, pack = p, opt
        if want not in pack:
            bad.append(f'carte : {p} perdu (attendu {want})')
    for p in sorted(server):
        if p in replaced and p not in wrapped:
            bad.append(f'serveur : remplacé non enveloppé {p}')
        if p.endswith('.png.mcmeta') and p[:-len('.mcmeta')] in replaced:
            bad.append(f'serveur : mcmeta d\'une texture remplacée {p}')
        if p in wrapped or (p.startswith(MC + 'items/') and p in replaced):
            sel = json.loads(server[p].decode('utf-8'))['model']
            if p not in wrapped:
                bad.append(f'serveur : item remplacé non enveloppé {p}')
            elif sel.get('type') != 'minecraft:select' or sel.get('property') != 'minecraft:context_dimension':
                bad.append(f'serveur : {p} pas un select context_dimension')
            elif [c['when'] for c in sel['cases']] != [fs.FLOATY_DIM]:
                bad.append(f'serveur : {p} cas autre que mg:floaty')
            elif sel['fallback'] != man['items'][p]['model']:
                bad.append(f'serveur : {p} repli différent de vanilla')
            elif 'floaty:' in json.dumps(sel['fallback']):
                bad.append(f'serveur : {p} floaty: dans le repli')
    for p in sorted(opt):
        if p in server:
            bad.append(f'optionnel : aussi dans le serveur {p}')
        if p.startswith((MC + 'items/', 'assets/mg/', 'assets/floaty/')) or '/lang/' in p:
            bad.append(f'optionnel : interdit {p}')
        if p in man['dropped']:
            bad.append(f'optionnel : écarté {p}')
    for p in man['dropped']:
        if p in server:
            bad.append(f'serveur : écarté {p}')
    for p, data in sorted(server.items()):
        if p.endswith('.json'):
            for ref in set(re.findall(r'floaty:([a-z0-9_./-]+)', data.decode('utf-8'))):
                target = f'assets/floaty/models/{ref}.json' if p.startswith(MC + 'items/') else f'assets/floaty/textures/{ref}.png'
                if p.startswith('assets/floaty/models/') and f'"parent": "floaty:{ref}"' in data.decode('utf-8'):
                    target = f'assets/floaty/models/{ref}.json'
                if target not in server:
                    bad.append(f'serveur : {p} réf floaty:{ref} sans fichier')
    return bad


class ValidOutput(unittest.TestCase):
    def test_output_respects_every_invariant(self):
        server, opt = split()
        self.assertEqual(verifie(server, opt, MANIFEST), [])

    def test_real_manifest_with_a_stand_in_map(self):
        """floaty_vanilla.json commité + carte factice (tous ses chemins remplacés / écartés, items vanilla, sons neufs) : invariants tenus."""
        man = json.loads((RP / 'floaty_vanilla.json').read_text(encoding='utf-8'))
        rep = man['replaced']
        extra = {p: b'x' for paths in rep.values() for p in paths}
        extra.update({p: b'x' for p in man['dropped']})
        extra.update({p: js(man['items'][p]) for p in rep['items']})                                # définitions de la carte : celles de vanilla
        extra.update({p: js({'parent': 'item/handheld', 'textures': {'layer0': 'minecraft:item/blaze_rod'}}) for p in rep['models']})
        tex = rep['textures_item'][0][len(MC + 'textures/'):-len('.png')]
        extra.update({MC + 'textures/item/fresh.png': b'x', MC + 'models/item/fresh.json': js({'parent': 'item/generated', 'textures': {'layer0': 'minecraft:' + tex}}),
                      MC + 'items/fresh.json': js({'model': mdl('minecraft:item/blaze_rod')}), MC + 'sounds.json': js({e: {} for e in man['sounds']['new']})})
        man['names_sha256'] = fs.floaty_names_digest(extra)
        gen = (RP / 'gen_rp.py').read_text(encoding='utf-8')
        pack_fmt = json.loads(re.search(r'^PACK_FMT = (\{.*\})', gen, re.M).group(1))
        server, opt = fs.floaty_split(extra, pack_fmt, man)
        self.assertEqual(verifie(server, opt, man, extra), [])
        self.assertEqual(sum(1 for p in server if p.startswith(MC + 'items/')), len(man['items']) + 1)            # enveloppés + l'item neuf
        self.assertEqual(json.loads(server[MC + 'items/fresh.json'].decode('utf-8'))['model']['model'], 'floaty:item/blaze_rod')
        fresh = json.loads(server[MC + 'models/item/fresh.json'].decode('utf-8'))
        self.assertEqual(fresh['textures']['layer0'], 'floaty:' + tex)                                          # modèle neuf réécrit vers floaty:


class InverseCases(unittest.TestCase):
    """Chaque invariant doit détecter sa violation : on falsifie une sortie valide."""
    def setUp(self):
        self.server, self.opt = split()

    def found(self, server=None, opt=None, needle=''):
        bad = verifie(self.server if server is None else server, self.opt if opt is None else opt, MANIFEST)
        self.assertTrue(any(needle in b for b in bad), (needle, bad))

    def test_replaced_texture_on_the_server_is_rejected(self):
        self.found({**self.server, MC + 'textures/entity/zombie/zombie.png': b'z'}, needle='remplacé non enveloppé')

    def test_unwrapped_vanilla_item_is_rejected(self):
        self.found({**self.server, SWORD: js(MAP_SWORD)}, needle='pas un select')
        self.found({**self.server, SWORD: js({'model': mdl('minecraft:item/sword')})}, needle='pas un select')

    def test_different_fallback_is_rejected(self):
        sel = json.loads(self.server[SWORD].decode('utf-8'))
        sel['model']['fallback'] = mdl('minecraft:item/other')
        self.found({**self.server, SWORD: js(sel)}, needle='repli différent')

    def test_floaty_ref_in_fallback_is_rejected(self):
        man = copy.deepcopy(MANIFEST)
        man['items'][APPLE] = {'model': mdl('floaty:item/apple')}
        server, _ = split(man=man)
        bad = verifie(server, self.opt, man)
        self.assertTrue(any('floaty: dans le repli' in b for b in bad), bad)

    def test_second_case_is_rejected(self):
        sel = json.loads(self.server[SWORD].decode('utf-8'))
        sel['model']['cases'].append({'when': 'minecraft:overworld', 'model': mdl('minecraft:item/x')})
        self.found({**self.server, SWORD: js(sel)}, needle='cas autre')

    def test_other_dimension_is_rejected(self):
        sel = json.loads(self.server[SWORD].decode('utf-8'))
        sel['model']['cases'][0]['when'] = 'minecraft:the_end'
        self.found({**self.server, SWORD: js(sel)}, needle='cas autre')

    def test_mcmeta_of_replaced_texture_is_rejected(self):
        self.found({**self.server, MC + 'textures/block/stone.png.mcmeta': b'{}'}, needle='mcmeta d\'une texture remplacée')

    def test_optional_pack_violations_are_rejected(self):
        self.found(opt={**self.opt, APPLE: b'{}'}, needle='interdit')
        self.found(opt={**self.opt, 'assets/mg/x.json': b'{}'}, needle='interdit')
        self.found(opt={**self.opt, MC + 'lang/en_us.json': b'{}'}, needle='interdit')
        self.found(opt={**self.opt, MC + 'sounds.json': b'{}'}, needle='aussi dans le serveur')
        self.found(opt={**self.opt, MC + 'textures/misc/enchanted_glint_entity.png': b'x'}, needle='écarté')

    def test_dropped_on_the_server_and_dangling_floaty_ref_are_rejected(self):
        self.found({**self.server, MC + 'textures/misc/enchanted_glint_entity.png': b'x'}, needle='écarté')
        server = {p: d for p, d in self.server.items() if p != 'assets/floaty/models/item/apple.json'}
        self.found(server, needle='sans fichier')

    def test_dangling_ref_with_dot_or_dash_is_rejected(self):
        model = js({'parent': 'item/generated', 'textures': {'layer0': 'floaty:item/a-b.c'}})
        server = {**self.server, 'assets/floaty/textures/item/a.png': b'x', 'assets/floaty/models/item/apple.json': model}      # item/a existe, pas item/a-b.c
        self.found(server, needle='floaty:item/a-b.c')

    def test_optional_pack_with_a_new_file_is_rejected(self):
        self.found(opt={**self.opt, MC + 'textures/block/new.png': b'x'}, needle='pas un remplacement')

    def test_missing_wrapped_item_is_rejected(self):
        self.found({p: d for p, d in self.server.items() if p != APPLE}, needle='item enveloppé absent')

    def test_lost_map_files_are_rejected(self):
        fresh = MC + 'textures/item/fresh.png'
        self.found({p: d for p, d in self.server.items() if p != fresh}, needle=f'carte : {fresh} perdu')                         # neuf, perdu
        self.found(opt={p: d for p, d in self.opt.items() if p != MC + 'textures/block/stone.png'}, needle='stone.png perdu')   # remplacé global, perdu
        renamed = {p: d for p, d in self.server.items() if p != 'assets/floaty/textures/item/apple.png'}
        self.found(renamed, needle='attendu assets/floaty/textures/item/apple.png')                                               # renommé, perdu
        self.found({**self.server, MC + 'textures/item/apple.png': b'apple'}, needle='remplacé non enveloppé')                   # laissé sous son nom vanilla


if __name__ == '__main__':
    unittest.main()
