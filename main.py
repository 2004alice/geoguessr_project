import random
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

meta_base = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
pic_base = 'https://maps.googleapis.com/maps/api/streetview?'
api_key = 'AIzaSyDp5B31TCZ9NjBZ0Z1MElnDkeIRgeqxcVw'


def new_york():
    latitude = random.uniform(40.681926, 40.681288)
    print(round(latitude, 6))
    longitude = random.uniform(-73.943806, -73.941969)
    print(round(longitude, 6))

    latitude_string = str(latitude)
    print(round(latitude, 6))
    longitude_string = str(longitude)
    print(round(longitude, 6))

    coordinates = ""
    if coordinates == "":
        coordinates += latitude_string + ", " + longitude_string
        print(coordinates)
    # ^ coordinates of ny/london, test area
    location = coordinates
    meta_params = {'key': api_key,
                   'location': location}
    # define the params for the picture request
    pic_params = {'key': api_key,
                  'location': location,
                  'size': "640x640"}
    # obtain the metadata of the request
    meta_response = requests.get(meta_base, params=meta_params)
    print(meta_response.json())
    # if statement for not found image
    pic_response = requests.get(pic_base, params=pic_params)
    for key, value in pic_response.headers.items():
        print(f"{key}: {value}")
    with open('test.jpg', 'wb+') as file:
        file.write(pic_response.content)
    pic_response.close()
    plt.figure(figsize=(10, 10))
    img = mpimg.imread('test.jpg')
    imgplot = plt.imshow(img)
    plt.show()


def london():
    latitude = random.uniform(51.500851, 51.502080)
    print(round(latitude, 6))
    longitude = random.uniform(-0.127605, -0.117570)
    print(round(longitude, 6))

    latitude_string = str(latitude)
    print(round(latitude, 6))
    longitude_string = str(longitude)
    print(round(longitude, 6))

    coordinates = ""
    if coordinates == "":
        coordinates += latitude_string + ", " + longitude_string
        print(coordinates)
    # ^ coordinates of ny/london, test area
    location = coordinates
    meta_params = {'key': api_key,
                   'location': location}
    # define the params for the picture request
    pic_params = {'key': api_key,
                  'location': location,
                  'size': "640x640"}
    # obtain the metadata of the request
    meta_response = requests.get(meta_base, params=meta_params)
    print(meta_response.json())
    # if statement for not found image
    pic_response = requests.get(pic_base, params=pic_params)
    for key, value in pic_response.headers.items():
        print(f"{key}: {value}")
    with open('test.jpg', 'wb+') as file:
        file.write(pic_response.content)
    pic_response.close()
    plt.figure(figsize=(10, 10))
    img = mpimg.imread('test.jpg')
    imgplot = plt.imshow(img)
    plt.show()


def paris():
    latitude = random.uniform(48.857161, 48.850627)
    print(round(latitude, 6))
    longitude = random.uniform(2.343144, 2.356289)
    print(round(longitude, 6))

    latitude_string = str(latitude)
    print(round(latitude, 6))
    longitude_string = str(longitude)
    print(round(longitude, 6))

    coordinates = ""
    if coordinates == "":
        coordinates += latitude_string + ", " + longitude_string
        print(coordinates)
    # ^ coordinates of ny/london, test area
    location = coordinates
    meta_params = {'key': api_key,
                   'location': location}
    # define the params for the picture request
    pic_params = {'key': api_key,
                  'location': location,
                  'size': "640x640"}
    # obtain the metadata of the request
    meta_response = requests.get(meta_base, params=meta_params)
    print(meta_response.json())
    # if statement for not found image
    pic_response = requests.get(pic_base, params=pic_params)
    for key, value in pic_response.headers.items():
        print(f"{key}: {value}")
    with open('test.jpg', 'wb+') as file:
        file.write(pic_response.content)
    pic_response.close()
    plt.figure(figsize=(10, 10))
    img = mpimg.imread('test.jpg')
    imgplot = plt.imshow(img)
    plt.show()


def los_angeles():
    latitude = random.uniform(34.039342, 34.056612)
    print(round(latitude, 6))
    longitude = random.uniform(-118.252698, -118.234370)
    print(round(longitude, 6))

    latitude_string = str(latitude)
    print(round(latitude, 6))
    longitude_string = str(longitude)
    print(round(longitude, 6))

    coordinates = ""
    if coordinates == "":
        coordinates += latitude_string + ", " + longitude_string
        print(coordinates)
    # ^ coordinates of ny/london, test area
    location = coordinates
    meta_params = {'key': api_key,
                   'location': location}
    # define the params for the picture request
    pic_params = {'key': api_key,
                  'location': location,
                  'size': "640x640"}
    # obtain the metadata of the request
    meta_response = requests.get(meta_base, params=meta_params)
    print(meta_response.json())
    # if statement for not found image
    pic_response = requests.get(pic_base, params=pic_params)
    for key, value in pic_response.headers.items():
        print(f"{key}: {value}")
    with open('test.jpg', 'wb+') as file:
        file.write(pic_response.content)
    pic_response.close()
    plt.figure(figsize=(10, 10))
    img = mpimg.imread('test.jpg')
    imgplot = plt.imshow(img)
    plt.show()


def moscow():
    latitude = random.uniform(55.751781, 55.753523)
    print(round(latitude, 6))
    longitude = random.uniform(37.572019, 37.644610)
    print(round(longitude, 6))

    latitude_string = str(latitude)
    print(round(latitude, 6))
    longitude_string = str(longitude)
    print(round(longitude, 6))

    coordinates = ""
    if coordinates == "":
        coordinates += latitude_string + ", " + longitude_string
        print(coordinates)
    # ^ coordinates of ny/london, test area
    location = coordinates
    meta_params = {'key': api_key,
                   'location': location}
    # define the params for the picture request
    pic_params = {'key': api_key,
                  'location': location,
                  'size': "640x640"}
    # obtain the metadata of the request
    meta_response = requests.get(meta_base, params=meta_params)
    print(meta_response.json())
    # if statement for not found image
    pic_response = requests.get(pic_base, params=pic_params)
    for key, value in pic_response.headers.items():
        print(f"{key}: {value}")
    with open('test.jpg', 'wb+') as file:
        file.write(pic_response.content)
    pic_response.close()
    plt.figure(figsize=(10, 10))
    img = mpimg.imread('test.jpg')
    imgplot = plt.imshow(img)
    plt.show()


def random_city():
    num = random.randint(1, 5)
    if num == 1:
        new_york()
    elif num == 2:
        london()
    elif num == 3:
        paris()
    elif num == 4:
        los_angeles()
    elif num == 5:
        moscow()
    guess = str(input("what city is this? options: new york, london, paris, los angeles, moscow"))
    if guess == "new york" and num == 1:
        print("correct!")
    elif guess == "london" and num == 2:
        print("correct!")
    elif guess == "paris" and num == 3:
        print("correct!")
    elif guess == "los angeles" and num == 4:
        print("correct!")
    elif guess == "moscow" and num == 5:
        print("correct!")
    else:
        print("wrong :(")


random_city()
