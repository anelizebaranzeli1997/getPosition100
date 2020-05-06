# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:33:48 2017

@author: anelize
"""

import sys

my_positions = open(sys.argv[1], 'r')
my_fasta = open(sys.argv[2], 'r')

with open(sys.argv[1], 'r') as f:    
    lines = len(f.readlines())

names= []
seqs = []
#ids = []
#posa = []
#posb = []

def read_positions(my_positions):
            
        line = my_positions.read()            
        values = line.split()         
        return values
            
def read_fasta(my_fasta):

        name, seq = None, []   
        
        for line in my_fasta:                        

            line = line.rstrip()
            
            if line.startswith(">"):

                if name: yield (name, ''.join(seq))
                    
                name, seq = line, []                            

            else:
                
                seq.append(line)
        
        if name: yield (name, ''.join(seq))                

for name, seq in read_fasta(my_fasta):
    
        seqs.append(seq)
        names.append(name)
 
if __name__ == '__main__':
    output_file=open(sys.argv[3],"w+")    
    a=0
    b=a+1
    positions = read_positions(my_positions)

    for i in range(lines):
        
            single_seqs = seqs [0]   
        #print i     
            #print names[0]+'_my_gene_name', '\n', single_seqs[int(positions[a])-1:int(positions[b])]
            if positions[a] < positions[b] :           
            #print names[0]+'_my_gene_name', '\n', single_seqs[int(positions[a])-1:int(positions[b])]
        #print 'a < b'
                print >> output_file, names[0]+'_my_gene_name', '\n', single_seqs[int(positions[a])-110:int(positions[b])+100]
                #print int(positions[a])-11
                #print int(positions[b])+10
            elif  positions[b] < positions[a] :           

            #print names[0]+'_my_gene_name', '\n', single_seqs[int(positions[b])-1:int(positions[a])]
            #print names[0]+'_my_gene_name', '\n', single_seqs[int(positions[b])-1:int(positions[a])]
        #print 'a > b'
                print >> output_file, names[0]+'_my_gene_name', '\n', single_seqs[int(positions[b])-110:int(positions[a])+100]              
                #print int(positions[a])+11
                #print int(positions[b])-10


            a = b+1       
            b = a+1

    output_file.close()



