from __future__ import division
import conformal_blocks.cbbundle as cbd
import cbclient.cbclient as cbc
import time
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.rings.rational_field import RationalField

def experiment():
    rank = 5
    level = 4
    num_points = 10

    client = cbc.CBClient()
    liealg = cbd.TypeALieAlgebra(rank, store_fusion=True, exact=True)
    print("Weight", "Rank", "Divisor")
    rays = []
    for wt in liealg.get_weights(level):
        cbb = cbd.SymmetricConformalBlocksBundle(client, liealg, wt, num_points, level)
        if cbb.get_rank() == 0:
            #print(wt, 0)
            continue
        divisor = cbb.get_symmetrized_divisor()
        rays = rays + [divisor]
        print(wt, cbb.get_rank(), divisor)

    p = Polyhedron(rays=rays, base_ring=RationalField(), backend="cdd")
    print(p.Vrepresentation())

if __name__ == '__main__':
    experiment()