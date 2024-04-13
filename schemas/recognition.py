from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(description="Название продукта", default="")
    CompanyName: str = Field(description="название компании, изготавливающей продукт", default="")
    category: str = Field(description="Категория продукта", default="")
    old: str = Field(description="Возрастная маркировка и рекомендованный возраст", default="")
    HasSugar: bool = Field(description="Наличие сахара", default=False)
    HasSodium: bool = Field(description="Наличие натрия", default=False)
    HasSubSugar: bool = Field(description="Наличие подсластителей", default=False)
    HasTransFat: bool = Field(description="Наличие транс-жиров", default=False)
    HasGMO: bool = Field(description="Наличие ГМО", default=False)
    kcal: int = Field(description="Количество килокалорий в продукте", default=0)
    composition: str = Field(description="Состав продукта через запятую", default="")
    proteins: float = Field(description="Показатель белков и протеина", default=0.0)
    fats: float = Field(description="Показатель жиров", default=0.0)
    carbohydrates: float = Field(description="Показатель углеводов", default=0.0)
    energy: float = Field(description="Энергетическая ценность", default=0.0)
    HasMarketingLabels: bool = Field(description="Рекламные заголовки в тексте", default=False)


class RecognizeRequest(BaseModel):
    front_side: str
    back_side: str


class RecognizeResponse(BaseModel):
    product: Product
    rule: str
