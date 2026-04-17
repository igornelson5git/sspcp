import os
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
p = PDBParser()

dataset_file = open("petase.txt", "r")

for line in dataset_file:
    if (line.startswith(">")):
        line.strip()
        prot_name = line.split(")")[1].strip()
        
        print(prot_name[:4])
        os.system('pdb_fetch '+prot_name[:4]+' > '+prot_name[:4]+'.pdb')

        structure = p.get_structure(prot_name[:4],prot_name[:4]+ '.pdb')
        
        # use only the first model
        model = structure[0]
        print(prot_name[:4]+ '.pdb')
        
        # calculate DSSP
        dssp = DSSP(model,prot_name[:4]+ '.pdb', file_type='PDB')
        # extract sequence and secondary structure from the DSSP tuple
        sequence = ''
        sec_structure = ''
        for z in range(len(dssp)):
            a_key = list(dssp.keys())[z]
            sequence += dssp[a_key][1]
            sec_structure += dssp[a_key][2]

        # print extracted sequence and structure

        print(sequence)
        print(sec_structure)
        
        sec_structure = sec_structure.replace('-', 'C')
        sec_structure = sec_structure.replace('I', 'C')
        sec_structure = sec_structure.replace('T', 'C')
        sec_structure = sec_structure.replace('S', 'C')
        sec_structure = sec_structure.replace('G', 'H')
        sec_structure = sec_structure.replace('B', 'E')
        print(sec_structure)