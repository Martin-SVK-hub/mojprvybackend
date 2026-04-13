from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# základná route
@app.route('/')
def home():
    return render_template('index.html')
 
databaza = {
    "students": [
        {
            "id": 1,
            "name": "Martin",
            "surname": "Deglovič",
            "nickname": "Martin-SVK",
            "img":"https://www.bud-cool.cz/upload/pic/158-vtipne-obrazky-matka-pepka.jpg"
        },
        {
            "id": 2,
            "name": "Karolína",
            "surname": "Kmeťová",
            "nickname": "K.Karolína",
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg1Ae2rXgmPye0mdujYgKNfqpMGQfZt9bhbw&s"
        }, {
            "id": 3,
            "name": "Markus",
            "surname": "Martiš",
            "nickname": "cigga",
                 "img": "https://www.csgoroll.com/blog/content/images/size/w2000/2025/02/1f828-17109267473263-1920.webp"
        }, {
            "id": 4,
            "name": "Janka",
            "surname": "Vargová",
            "nickname": "dzejna",
                    "img": "https://www.pcgamesn.com/wp-content/sites/pcgamesn/2024/02/best-cs2-settings.jpg"
        }, 
        {
            "id": 5,
            "name": "Marko",
            "surname": "Mihalička",
            "nickname": "marko.mihalicka",
                    "img": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"
        },  
            {
                "id": 6,
                "name": "Samo",
                
                "surname": "Martiš",
                "nickname": "the.mlaka",
                     "img":"https://www.gearpatrol.com/wp-content/uploads/sites/2/2020/06/Best-Fun-New-Cars-to-Buy-gear-patrol-lead-full-jpg.webp"
            },
                {
                    "id": 7,
                    "name": "Lukáš",
                    "surname": "Vindiš",
                    "nickname": "Lukáš.Vindis",
                    "img":"https://www.lgt.com/resource/image/34316/landscape_ratio8x5/1380/863/9f8c982aada32e07fac4372dc2c4fe23/4512D3D511D8B3022F921B35F55002F8/20-093-classic-car-racing-en.webp"
                } ,
                    {
                        "id": 8,
                        "name": "Samuel",
                        "surname": "Uhrík",
                        "nickname": "Samuel.Uhrik",
                        "img":"https://dragon2000-multisite.s3.eu-west-2.amazonaws.com/wp-content/uploads/sites/599/2024/11/12105034/Fisher-Performance-home-page-hero-set-2-image-10_2024-1.jpg"
                    },
                        {
                            "id": 9,
                            "name": "Matúš",
                            "surname": "Holečka",
                            "nickname": "Matúš_Holečka",
                            "img": "https://img.sector.sk/files/novinky/0/2025/3-4-18-7-84/gta-v-enhanced-edition-je-dost-image-376.jpg"
                        },
                            {
                                "id": 10,
                                "name": "Samo",
                                "surname": "Haring",
                                "nickname": "Samo.Haring",
                                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0vZV759qtM8X6CY6NPM_6vDsYXxr-SCHNcA&s"
                            }

    ]
}

@app.route('/api')
def api():
    return jsonify(databaza)

@app.route('/api/student/<int:id>')

def find_student(id):
   #search for student
    for student in databaza ["students"]:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"error": "not found"}),

# spustenie servera
if __name__ == '__main__':
    app.run(debug=True)
