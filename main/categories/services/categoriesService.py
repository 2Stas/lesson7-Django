
from main.models import Category


def create_category(name, description=''):
    category = Category.objects.create( name=name,description=description )

    return category


def update_category(category_id, name, description=''):
    category = Category.objects.filter(id=category_id).first()

    if category is None:
        return None

    category.name = name
    category.description = description
    category.save()

    return category


def delete_category(category_id):
    category = Category.objects.filter(id=category_id).first()

    if category is None:
        return False

    category.delete()

    return True
