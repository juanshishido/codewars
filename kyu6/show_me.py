def show_me(instname):
    name = instname.__class__.__name__
    attrs = sorted(instname.__dict__.keys())
    att_f = ', '.join(attrs[:-1])
    att_l = attrs[-1]
    if len(attrs) == 1:
        return ("Hi, I'm one of those %ss! Have a look at my %s." %
               (name, attrs[0]))
    else:
        return ("Hi, I'm one of those %ss! Have a look at my %s and %s." %
               (name, att_f, att_l))
