import os 
import shutil
import unittest
import subprocess
from . import TestCase


class TestTaxonomy(TestCase):
    @unittest.skip
    def test_count_taxa(self):
        input_file = os.path.join('test', 'data', 
                                  'test_ncbi_taxa_count.txt.gz')
        output_prefix = os.path.join(self.output_dir,
                                    'ncbo_taxa_count_output_')
        nodes_dump = os.path.join('inst', 'taxdump', 'nodes.dmp')
        names_dump = os.path.join('inst', 'taxdump', 'names.dmp')
        cmd = f'''
        python -m htstk.taxonomy count-taxa
            --input-file {input_file}
            --output-prefix {output_prefix}
            --nodes-dump {nodes_dump}
            --names-dump {names_dump}
        '''
        subprocess.run(cmd.split())
