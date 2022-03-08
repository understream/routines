import sys

template = """import sys

if __name__ == "__main__":
    if len(sys.argv) < %(min_args_needed)d:
        print("%(usage_str)s" %% sys.argv[0])
        sys.exit(-1)

%(lines)s

    #start writing logics here
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python %s <argument list...>" % sys.argv[0] )
        print("\t arument format: [type:]<argument_name>[:optional]")
        print("\t type: in|out|int")
        sys.exit(-1)

    args = []
    for a in sys.argv[1:]:
        parts = a.split(":")
        t = ""
        optional = False
        argname = ""
        if len(parts) == 1:
            t = ""
            argname = parts[0]
            optional = False
        elif len(parts) == 2:
            t = parts[0]
            if t not in ["in", "out", "int"]: t = ""
            argname = parts[1]
        else:
            t = parts[0]
            if t not in ["in", "out", "int"]: t = ""
            argname = parts[1]
            optional = parts[2] == "optional"

        args.append( [t,argname,optional] )

    def p_arg( arg ):
        tpl = "<%s>"
        if arg[2]:
            tpl = "[%s]"

        if arg[0] == "in":
            return tpl % ("input file " + arg[1])
        elif arg[0] == "out":
            return tpl % ("output file " + arg[1])
        else: 
            return tpl % arg[1]
            
    d = {}
    d['min_args_needed'] = list(map( lambda x: x[2], args )).count( False ) + 1
    d['usage_str'] = "Usage: python %%s %s" % (" ".join( p_arg(k) for k in args ) )

    def mk_padded_line( tabs, line ):
        return ("    " * tabs) + line

    lines = []
    c = 1
    for arg in args:
        if arg[0] == "in":
            line = """%s = open(sys.argv[%d], "r")""" % (arg[1], c)
        elif arg[0] == "out":
            line = """%s = open(sys.argv[%d], "a")""" % (arg[1], c)
        elif arg[0] == "int":
            line = """%s = int(sys.argv[%d])""" % (arg[1], c)
        else:
            line = """%s = sys.argv[%d]""" % (arg[1], c)

        if arg[2]:
            if arg[0] == "in" or arg[0] == "out":
                default = "None"
            elif arg[0] == "int":
                default = "0"
            else:
                default = "''"
            before = "%s = %s" % (arg[1], default)
            lines.append( before )
            lines.append( "if len(sys.argv) >= %d:" % (c+1) )
            lines.append( mk_padded_line( 1, line ) )
        else:
            lines.append( line )
        c += 1

    d['lines'] = "\n".join([mk_padded_line(1,line) for line in lines])
    
    print( template % d )
    
            

            
