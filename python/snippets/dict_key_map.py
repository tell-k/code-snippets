model_names = {'k1': 1, 'k2': 2}

print dict(map((lambda x:('draft_'+x, model_names[x])), model_names))

print dict(("draft_"+k, model_names[k]) for k in model_names)

print {"draft_"+k:v for k,v in model_names.iteritems()}

print dict([('draft_'+k, v) for k, v in model_names.iteritems()])

print dict([('draft_' + k if v else k, v) for k, v in model_names.iteritems()])
