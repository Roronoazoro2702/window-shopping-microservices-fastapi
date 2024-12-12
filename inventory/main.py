from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel


app = FastAPI()



redis = get_redis_connection(
    host= "redis-15411.c301.ap-south-1-1.ec2.redns.redis-cloud.com",
    port= 15411,
    password="n3q33wApsH6wun2EOBwdTlMxgmSuOgDT",
    decode_responses=True
    
)
class Product(HashModel):
    name: str
    price: float
    quantity: int


    class Meta:
        database = redis
        model_config = {
            "arbitrary_types_allowed": True  
        }
       


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]


def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)

