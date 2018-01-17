from django.http import Http404, HttpResponse

from .models import Poem


# Create your views here.

def more_poems(request):
    if request.is_ajax():
        objects = Poem.objects.all()

        data = get_json_objects(objects, Poem)

        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404()
    # objects = Poem.objects.all()
    #
    # data = get_json_objects(objects, Poem)
    #
    # return HttpResponse(data, content_type='application/json')


def json_filed(filed_data):
    if isinstance(filed_data, str):
        return "\"" + filed_data + "\""
    if isinstance(filed_data, bool):
        if filed_data == False:
            return False
        else:
            return True
    return str(filed_data)

def json_encode_dict(dict_data):
    json_data = "{"
    for (key, value) in dict_data.items():
        json_data = json_data + json_filed(key) + ": " + json_filed(value) + " "
    json_data = json_data[:-2] + "}"

    return json_data


def json_encode_list(list_data):
    json_res = "["
    for item in list_data:
        json_res = json_res + json_encode_dict(item) + ", "
    return json_res[:-2] + "]"


def get_json_objects(objects, model_meta):
    concreate_model = model_meta._meta.concrete_model
    list_data = []
    for obj in objects:
        dict_data = {}
        for field in concreate_model._meta.local_fields:
            if field.name == 'id':
                continue
            value = field.value_from_object(obj)
            dict_data[field.name] = value
            # print(type(dict_data))
            print(dict_data)
        list_data.append(dict_data)
    data = json_encode_list(list_data)
    return data
