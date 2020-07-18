import os

class Config:
    SECRET_KEY='5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = 'True'
    MAIL_USERNAME="inksplash2711@gmail.com"
    MAIL_PASSWORD="Inksplash.art@2711"
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
