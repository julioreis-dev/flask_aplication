from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def indexname(number):
    if number < random_number:
        return 'Too Low, Try again!!!' \
               '<img src="https://th.bing.com/th/id/R94ae4c12621a0baddbd4a9af1c31103f?rik=cct2sxfHquU8fw&riu=http%3a%2f%2fwww.revistapazes.com%2fcontent%2fuploads%2f2016%2f10%2ftriste-696x404.jpg&ehk=sZSzuhsP%2fqPZTxXfOytibFOux4nQIFQENXo9wEU7UKI%3d&risl=&pid=ImgRaw">'
    elif number > random_number:
        return 'Too Hight, Try again!!!' \
               '<img src="https://th.bing.com/th/id/R79b5915e9c81b5e49c477b7b8cf62ea2?rik=McL3%2bAAnKfQWTA&riu=http%3a%2f%2fs2.glbimg.com%2fcOKr1-10No6o161sRKPBC30W0GE%3d%2f620x450%2fe.glbimg.com%2fog%2fed%2ff%2foriginal%2f2015%2f07%2f30%2fthinkstockphotos-177363232.jpg&ehk=opeV3xAq7KiKSB5b9B5CEBpys0wnwz4fAje%2bvusWXZ4%3d&risl=&pid=ImgRaw">'
    else:
        return 'You found me!!!' \
               '<img src="https://th.bing.com/th/id/Re396678be6047cb155e842a770ee2b31?rik=LWHoBiYO2RgoGw&riu=http%3a%2f%2f3.bp.blogspot.com%2f-IF-FQBaL1Yk%2fUYEZ-TslZdI%2fAAAAAAAATGg%2fOwg9ksO2a6k%2fs1600%2fA-felicidade-anda-por-ai-disfarcada-de-tudo-isso.jpg&ehk=hSEPk%2b%2bmoNuaWpy6w2%2bWjpI61RhjpEqecFrBScE6C2U%3d&risl=&pid=ImgRaw">'


if __name__ == "__main__":
    app.run(debug=True)
