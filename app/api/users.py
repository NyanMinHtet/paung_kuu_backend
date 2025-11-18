from flask import Blueprint, request, jsonify, abort
from app import db
from app.models.user import User

users_blueprint = Blueprint('users', __name__)


def haversine(lat1, lon1, lat2, lon2):
    # simple haversine, returns kilometers
    import math
    if None in (lat1, lon1, lat2, lon2):
        return float('inf')
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return c * r


@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'username, email and password are required'}), 400

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({'error': 'username or email already exists'}), 400

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict(include_email=True))


@users_blueprint.route('/users', methods=['GET'])
def list_users():
    # optional filters: skill, lat, lon, radius (km)
    skill = request.args.get('skill')
    try:
        lat = float(request.args.get('lat')) if request.args.get('lat') else None
        lon = float(request.args.get('lon')) if request.args.get('lon') else None
    except ValueError:
        return jsonify({'error': 'lat and lon must be numbers'}), 400
    radius = float(request.args.get('radius')) if request.args.get('radius') else None

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    # basic query then in-Python filtering for portability (SQLite/Postgres)
    query = User.query
    items = query.paginate(page=page, per_page=per_page, error_out=False).items

    results = []
    for u in items:
        if skill:
            if not u.skills or skill not in u.skills:
                continue
        if lat is not None and lon is not None and radius is not None:
            dist = u.distance_to(lat, lon)
            if dist > radius:
                continue
            out = u.to_dict()
            out['distance_km'] = dist
            results.append(out)
        else:
            results.append(u.to_dict())

    return jsonify(results)


@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json() or {}
    # prevent changing unique fields to ones that already exist
    if 'username' in data and data['username'] != user.username:
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'username already taken'}), 400
    if 'email' in data and data['email'] != user.email:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'email already taken'}), 400

    user.from_dict(data, new_user=False)
    if 'password' in data:
        user.set_password(data['password'])

    db.session.commit()
    return jsonify(user.to_dict())


@users_blueprint.route('/users/<int:user_id>/rate', methods=['POST'])
def rate_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json() or {}
    try:
        quality = float(data.get('quality', 0))
        reliability = float(data.get('reliability', 0))
    except (TypeError, ValueError):
        return jsonify({'error': 'quality and reliability must be numbers'}), 400

    if not (0 <= quality <= 5 and 0 <= reliability <= 5):
        return jsonify({'error': 'ratings must be between 0 and 5'}), 400

    user.update_rating(quality, reliability)
    db.session.commit()
    return jsonify(user.to_dict())
