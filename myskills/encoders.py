from django.core.serializers.json import DjangoJSONEncoder


class CustomEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return DjangoJSONEncoder.default(self, obj)
