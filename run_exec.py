from src import create_app
from config import config
app = create_app('Base')



if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port = 5000)



    