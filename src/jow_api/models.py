class Ingredient:
    def __init__(self, name, quantity, unit, isOptional):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.isOptional = isOptional


class JowResult:
    def __init__(
        self,
        id=None,
        url=None,
        name=None,
        ingredients=None,
        imageUrl=None,
        videoUrl=None,
        json=None,
        description=None,
        preparationTime=None,
        preparationExtraTimePerCover=None,
        coversCount=None,
        cookingTime=None,
    ):
        self.id = id
        self.url = url
        self.name = name
        self.ingredients = ingredients
        self.imageUrl = imageUrl
        self.videoUrl = videoUrl
        self.description = description
        self.preparationTime = preparationTime
        self.cookingTime = cookingTime
        self.preparationExtraTimePerCover = preparationExtraTimePerCover
        self.coversCount = coversCount
        self.json = json

