class Ingredient:
    def __init__(self, name, quantity, unit, is_optional):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.is_optional = is_optional


class JowResult:
    def __init__(
        self,
        id=None,
        url=None,
        name=None,
        ingredients=None,
        image_url=None,
        video_url=None,
        json=None,
        description=None,
        preparation_time=None,
        preparation_extra_time_per_cover=None,
        covers_count=None,
        cooking_time=None,
    ):
        self.id = id
        self.url = url
        self.name = name
        self.ingredients = ingredients
        self.image_url = image_url
        self.video_url = video_url
        self.description = description
        self.preparation_time = preparation_time
        self.cookingTime = cooking_time
        self.preparation_extra_time_per_cover = preparation_extra_time_per_cover
        self.covers_count = covers_count
        self.json = json

