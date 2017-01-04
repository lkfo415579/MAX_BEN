import sys
import numbers
import collections

def getsize(obj):
    # recursive function to dig out sizes of member objects:               
    def inner(obj, _seen_ids = set()):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, (basestring, numbers.Number, xrange)):
            pass # bypass remaining control flow and return                
        elif isinstance(obj, (tuple, list, set, frozenset)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, collections.Mapping) or hasattr(obj, 'iteritems'):
            size += sum(inner(k) + inner(v) for k, v in obj.iteritems())
        else:
            attr = getattr(obj, '__dict__', None)
            if attr is not None:
                size += inner(attr)
        return size
    return inner(obj)