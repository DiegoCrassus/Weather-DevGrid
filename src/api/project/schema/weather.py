from src.api.extensions import db


class WeatherData(db.Model):
    __tablename__ = 'weather_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    weather_id = db.Column(db.Integer)
    weather_main = db.Column(db.String(50))
    weather_description = db.Column(db.String(100))
    weather_icon = db.Column(db.String(5))
    temp = db.Column(db.Float, nullable=False)
    feels_like = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    sea_level = db.Column(db.Integer)
    grnd_level = db.Column(db.Integer)
    visibility = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    wind_deg = db.Column(db.Integer)
    wind_gust = db.Column(db.Float)
    clouds_all = db.Column(db.Integer)
    dt = db.Column(db.Integer)
    sys_type = db.Column(db.Integer)
    sys_id = db.Column(db.Integer)
    sys_country = db.Column(db.String(2))
    sys_sunrise = db.Column(db.Integer)
    sys_sunset = db.Column(db.Integer)
    timezone = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    city_name = db.Column(db.String(100))
    cod = db.Column(db.Integer)

    user = db.relationship('Users', backref=db.backref('weather_data', lazy=True))

