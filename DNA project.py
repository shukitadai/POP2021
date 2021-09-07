import random

chemicals = ["A","T","C","G"]

start = "ATG"

end = ["TAG","TAA","TAG"]


def make_codon():
    codon = ""
    for x in range(3):
        codon += chemicals[random.randint(0,len(chemicals)-1)]
    return codon

#print(codon)

gene = [start]
for x in range(random.randint(10,100)):
    codon = make_codon()
    while codon == start or codon in end:
        codon = make_codon()
        #print("start!!!")
#    if codon in end:
#        print("end")
    gene.append (make_codon())

print(gene)
    
