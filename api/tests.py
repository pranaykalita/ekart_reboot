from django.shortcuts import render, get_object_or_404
class MultipleFieldLookupORMixin(object):
    def get_object(self):
        queryset = self.get_queryset()  # Get the base.html queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            try:  # Get the result with one or more fields.
                filter[field] = self.kwargs[field]
            except Exception:
                pass
        return get_object_or_404(queryset, **filter)  # Lookup the object
