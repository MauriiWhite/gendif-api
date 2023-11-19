from cloudinary.uploader import destroy
from cloudinary.exceptions import NotFound
from cloudinary.uploader import upload
from cloudinary.api import resource, subfolders, create_folder
from rest_framework.exceptions import NotFound as AlertNotFound, NotAcceptable
from rest_framework.response import Response

from api.middlewares import get_model


def get_media(media):
    try:
        return resource(media)
    except NotFound:
        raise AlertNotFound("File not found.")


def destroy_resource(public_id):
    try:
        return destroy(public_id)
    except:
        raise AlertNotFound("File not destroy.")


def load_resource(user_id, file, folder: str):
    path = f"{folder}/{user_id}"

    subfolder_names = {subfolder["name"] for subfolder in subfolders(folder)["folders"]}
    if user_id not in subfolder_names:
        create_folder(path)
    return upload(file, folder=path, secure=True)


def set_url_img(representation, default, default_url, value="image"):
    cell = representation.get(value)
    if cell == default:
        representation[value] = default_url
    else:
        representation[value] = get_media(cell)["secure_url"]
    return representation


def resource_update(request, model, value_id, folder, file_type="image"):
    media_id = request.data.get(value_id)
    object = get_model(model, media_id)
    file = request.FILES.get(file_type)
    try:
        request.FILES["image"].content_type
    except:
        raise AlertNotFound("Not valid.")
    if not file:
        raise AlertNotFound("Image not found.")

    media = load_resource(media_id, file, folder=folder)
    object.image = media["public_id"]
    object.save()
    return Response({"msg": "success"})


def delete_resource(request, model, value_id, default):
    media_id = request.data.get(value_id)
    obj = get_model(model, media_id)
    if obj.image == default:
        raise NotAcceptable("It isn't possible...")
    destroy_resource(public_id=obj.image)
    obj.image = default
    obj.save()
    return Response({"msg": "success"})
