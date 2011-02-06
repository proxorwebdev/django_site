def inspect_model_vars(self):
    return "; ".join(["%s: %s" % (f.name, getattr(self,f.name)) for f in self._meta.fields])
