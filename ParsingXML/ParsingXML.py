import xml.etree.ElementTree
import glob
import sys

if len(sys.argv) < 5:
    print('Usage:');
    print('  python ParsingXML.py -folder input_path output_file trait_1 trait_2 ...');
    print('  python ParsingXML.py -file input_file output_file trait_1 trait_2 ...');
    sys.exit()

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
            output.insert(i,'N/A');
    outputfile=open(sys.argv[3],"a+");
    for i in range(len(output)):
        if i==len(output)-1:
            outputfile.write(output[i]);
        else:
            outputfile.write(output[i]+',');
    outputfile.write('\n');
    outputfile.close();
    del output[:];

if sys.argv[1]=='-file':
    parse(sys.argv[2])
elif sys.argv[1]=='-folder':
    for filename in glob.iglob(sys.argv[2]+'*.xml'):
        parse(filename)