# Example python script that reads protobuf messages of serialized R objects.
# To (re)produce these messages yourself, see /inst/messages/build.R script 
# in the RProtoBufUtils package. Before running this script, download and 
# compile the .proto files (see compile_python.sh)

#import the compiled proto definition, see compile_python.sh
import rexp_pb2;

#reading from a file:
import os;
os.system('wget https://raw.github.com/jeroenooms/RProtoBufUtils/master/inst/messages/cars_rexp.bin');
cars1 = rexp_pb2.REXP();
f = open('cars_rexp.bin', 'rb')
cars1.ParseFromString(f.read())
f.close();
print(cars1)

#reading from http url
import urllib2
cars2 = rexp_pb2.REXP();
response = urllib2.urlopen('https://raw.github.com/jeroenooms/RProtoBufUtils/master/inst/messages/cars_rexp.bin')
cars2.ParseFromString(response.read());
print(cars2)