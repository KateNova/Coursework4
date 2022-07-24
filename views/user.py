from typing import Tuple, Any, Dict

from flask import request
from flask_restx import Namespace, Resource

from dao.model.user import User, UserSchema
from decorator import user_identification
from implemented import user_service

user_ns: Namespace = Namespace('user')
user_schema: UserSchema = UserSchema()


@user_ns.route('/')
class UserView(Resource):
    @user_identification
    def get(self, email: str) -> Tuple[Dict[str, Any], int]:
        user: User = user_service.get_by_email(email)
        return user_schema.dump(user), 200

    @user_identification
    def patch(self, email: str) -> Tuple[str, int]:
        user: User = user_service.get_by_email(email)
        date = request.json
        user_service.update(user.id, date)
        return '', 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @user_identification
    def put(self, email: str) -> Tuple[str, int]:
        user: User = user_service.get_by_email(email)
        data = request.json
        user_service.update_password(user.id, data)
        return '', 204
