from genericpath import exists
from http.client import OK
from msilib.schema import Class
import requests
import json


base_url = "https://tidy-queens-dance-31-154-46-114.loca.lt/api/v1/cars/"

payload = {}
headers = {}


# class CAR:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


def get_cars_list():
    response = requests.request("GET", base_url, headers=headers, data=payload)
    return response.json(), response.status_code


def get_car_by_id(car_id):
    get_by_id_url = base_url + str(car_id)
    response = requests.request("GET", get_by_id_url, headers=headers, data=payload)
    return response.json(), response.status_code


def post_new_car(name, price):
    payload = {name: name, price: price}
    response = requests.request("POST", base_url, headers=headers, json=payload)
    return response.json(), response.status_code


if __name__ == "__main__":
    #    Tests
    # 1. post ~100 cars and validate they accessbile by id and by get list of cars (len)
    # 2. validate that multiple car objects can create with different id and same properties.
    # 3. get by id: assert that get by invalid id return 404 or not 200.
    # 4. post new car: assert that both properties (name, price) accespt only strings.
    # 5 assert that get car by id retrieve the correct car object even if tere are multiple cars with same properties.

    # car_list = []
    # for i in range(10):
    #     name = f"car_{i}"
    #     price = f"${10*i + 10}"
    #     # car = {"name": name, "price": price}
    #     post_new_car(name, price)
    # car_list.append(car)
    # print(car_list)

    def test_car():
        # create new car
        car_name = "tesla"
        car_price = "$1000"
        car_response, status = post_new_car(car_name, car_price)
        car_id = car_response["id"]
        car_obj = get_car_by_id(car_id)

        car_name = "tesla"
        assert car_obj["name"] == car_name
        assert car_obj["price"] == car_price

    test_car()
