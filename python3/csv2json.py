#encoding=utf-8
import sys
import json

def csv2json( csv_path ):
    line_spliter = ""
    yield "["
    with open(csv_path, "r", encoding='utf-8') as f:
        columns = f.readline().strip().split(",")
        while True:
            l = f.readline()
            if not l.strip(): break
            ll = l.strip().split(",")
            tmp = {}
            for i in range(0, max(len(columns), len(ll))):
                if i < len(columns) and i < len(ll):
                    tmp[ columns[i] ] = ll[i]
                elif i < len(columns):
                    tmp[ columns[i] ] = None 
                elif i < len(ll):
                    tmp[ "$key_%d"%(i+1) ] = ll[i]
            yield line_spliter + json.dumps( tmp ) 
            line_spliter = ","

    yield "]"




        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python %s <csv_file>" % sys.argv[0])
        sys.exit(-1)

    for r in csv2json( sys.argv[1] ):
        print( r )

    
