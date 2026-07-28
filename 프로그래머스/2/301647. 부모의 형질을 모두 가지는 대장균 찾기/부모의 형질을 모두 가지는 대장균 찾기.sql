select a.id, a.genotype, b.genotype as parent_genotype
from ecoli_data a, ecoli_data b
where a.parent_id = b.id
and b.genotype & a.genotype = b.genotype
order by id;