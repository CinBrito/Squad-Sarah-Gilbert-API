from flask import Flask, render_template
import  urllib.request, json


app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    characters = json.loads(data)["results"]

    return render_template("characters.html", characters=characters)

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations = json.loads(response.read())["results"]

    return render_template("locations.html", locations=locations)

@app.route("/location/<id>")
def get_location_profile(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    location_profile = json.loads(response.read())

    return render_template("location_profile.html", location_profile=location_profile)

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    profile = json.loads(response.read())

    return render_template("profile.html", profile=profile)

@app.route("/lista")
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = json.loads(response.read())["results"]

    return render_template("characters.html", characters=characters)


@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes_data = json.loads(response.read())["results"]

    return render_template("episodes.html", episodes=episodes_data)

@app.route("/episode/<id>")
def get_episode_profile(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episode_profile = json.loads(data)

    return render_template("episode_profile.html", episode_profile=episode_profile)

@app.route("/episode_profile/<id>")
def episode_profile(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response_episode = urllib.request.urlopen(url)
    data_episode = response_episode.read()
    episode_profile = json.loads(data_episode)

    characters_list = []
    for character_url in episode_profile["characters"]:
        response_character = urllib.request.urlopen(character_url)
        data_character = response_character.read()
        character = json.loads(data_character)
        characters_list.append(character)

    return render_template("episode.html", episode_profile=episode_profile, characters_list=characters_list)


@app.route("/location_profile/<id>")
def location_profile(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response_location = urllib.request.urlopen(url)
    data_location = response_location.read()
    location_profile = json.loads(data_location)

    # Obtém a lista de personagens associados à localização
    characters_list = []
    for character_url in location_profile["residents"]:
        response_character = urllib.request.urlopen(character_url)
        data_character = response_character.read()
        character = json.loads(data_character)
        characters_list.append(character)

    return render_template("location_profile.html", location_profile=location_profile, characters_list=characters_list)


if __name__ == "__main__":
    app.run(debug=True)