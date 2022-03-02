from create_app import create_app
import os


app_settings = os.getenv('APP_SETTINGS', 'src.config.BaseConfig')

app = create_app(app_settings)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
