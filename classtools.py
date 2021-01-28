#!/usr/bin/env python3
class AttrDisplay:
 """
 ...
 """
 def __gatherAttrs(self):
  attrs=[]
  for key in sorted(self.__dict__):
   attrs.append('%s=%s' % (key,getattr(self,key)))
  return ', '.join(attrs)
 def __str__(self):
  return '[%s: %s]' % (self.__class__.__name__,self.__gatherAttrs())
 def __repr__(self):
  return self.__str__()

  



















print(1+1,2+2,4+4,'...',65536*2)
