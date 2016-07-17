import xml.etree.ElementTree
import glob
import sys

output=list();
open(sys.argv[3], 'w').close()

def parse(filename):
    root=xml.etree.ElementTree.parse(filename).getroot();
    length = len(sys.argv)-4;
    for i in range(length):
        count=0;
        for child in root.iter(tag=sys.argv[i+4]):
            count=1;
            output.insert(i,child.text); 
        for child in root.iter():
            for key in child.attrib:
                if child.attrib[key]==sys.argv[i+4]:
                    count=1;
                    output.insert(i,child.text);
        if count==0:
            output.insert(i,'Trait not found in the given data');
    outputfile=open(sys.argv[3],"a+");
    for i in range(len(output)):
            outputfile.write(output[i]+',');
    outputfile.write('\n');
    outputfile.close();
    del output[:];

if sys.argv[1]=='-file':
    parse(sys.argv[2])
elif sys.argv[1]=='-folder':
    for filename in glob.iglob(sys.argv[2]+'*.xml'):
        parse(filename)