from datetime import datetime
import math

from sqlalchemy.ext.mutable import MutableDict, MutableList
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.Text)

    # Use mutable JSON columns so changes are tracked; works with Postgres JSON and falls back on SQLite
    skills = db.Column(MutableList.as_mutable(db.JSON), default=list)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    credits = db.Column(db.Integer, default=0)
    badges = db.Column(MutableList.as_mutable(db.JSON), default=list)
    verified = db.Column(MutableDict.as_mutable(db.JSON), default=dict)

    rating_quality = db.Column(db.Float, default=0.0)
    rating_reliability = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    # Password helpers
    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    # Rating update: incremental average
    def update_rating(self, quality: float, reliability: float) -> None:
        total = self.rating_count or 0
        self.rating_quality = ((self.rating_quality or 0.0) * total + float(quality)) / (total + 1)
        self.rating_reliability = ((self.rating_reliability or 0.0) * total + float(reliability)) / (total + 1)
        self.rating_count = total + 1

    # Haversine distance in kilometers
    def distance_to(self, lat: float, lon: float) -> float:
        if self.latitude is None or self.longitude is None or lat is None or lon is None:
            return float('inf')
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [self.longitude, self.latitude, lon, lat])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of earth in kilometers
        return c * r

    def to_dict(self, include_email: bool = False) -> dict:
        data = {
            'id': self.id,
            'username': self.username,
            'bio': self.bio,
            'skills': self.skills or [],
            'latitude': self.latitude,
            'longitude': self.longitude,
            'credits': self.credits,
            'badges': self.badges or [],
            'verified': self.verified or {},
            'rating_quality': self.rating_quality,
            'rating_reliability': self.rating_reliability,
            'rating_count': self.rating_count,
            'created_at': None if not self.created_at else self.created_at.isoformat(),
            'updated_at': None if not self.updated_at else self.updated_at.isoformat(),
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data: dict, new_user: bool = False) -> None:
        for field in ['username', 'email', 'bio', 'latitude', 'longitude', 'credits']:
            if field in data:
                setattr(self, field, data[field])

        if 'skills' in data and isinstance(data['skills'], list):
            self.skills = data['skills']
        if 'badges' in data and isinstance(data['badges'], list):
            self.badges = data['badges']
        if 'verified' in data and isinstance(data['verified'], dict):
            self.verified = data['verified']
        if new_user and 'password' in data:
            self.set_password(data['password'])
