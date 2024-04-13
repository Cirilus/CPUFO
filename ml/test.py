import json

from schemas.recognition import Product
from utils.utils import str2json

pipeline_json = '{\n    "name": "ЙОГУРТ «АГУША» С КЛУБНИКОЙ И БАНАНОМ",\n    "brand": "АГУША",\n    "category": "Молочные продукты",\n    "old": "для питания детей старше 8 месяцев",\n    "HasSugar": true,\n    "kcal": 105,\n    "composition": "молоко нормализованное, фруктовый наполнитель «Клубника-банан» (сахар, вода, пюре концентрированное клубничное, пюре банановое, ароматизаторы натуральные «Клубника», «Банан»), крахмал кукурузный, загуститель = пектины, соки концентрированные (из красной свеклы, лимонный)), пребиотик - олигофруктоза, концентрат сывороточных белков, закваска, пробиотические микроорганизмы - бифидобактерии ВВ12..",\n    "proteins": 8,\n    "fats": 2.7,\n    "carbohydrates": 5,\n    "energy": 390,\n    "HasMarketingLabels": false\n}'

pipeline_json = str2json(pipeline_json)

product = Product().parse_obj(pipeline_json)

print(product)