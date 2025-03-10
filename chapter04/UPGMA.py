import sys
from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

aln = AlignIO.read(sys.argv[1],"fasta")
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)
tree.root_at_midpoint()
Phylo.draw_ascii(tree)
