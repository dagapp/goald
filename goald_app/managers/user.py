"""
Module for handling user records in db
"""

from bcrypt import gensalt, hashpw

from goald_app.managers.common import DoesNotExist, AlreadyExists, IncorrectData

from goald_app.models import User, Group, Goal, Event, Report

import dataclasses
import json
from dataclasses import dataclass

LENGTH_SALT = 29
LENGTH_HASH = 60

class dataclass_encoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

@dataclass
class UserResult:
    login: str
    name: str
    second_name: str

    def __init__(self, user: User):
        self.login = user.login
        self.name = user.name
        self.second_name = user.second_name

@dataclass
class EventResult:
    type: int
    text: str
    timestamp: str

    def __init__(self, event: Event):
        self.type = event.type
        self.text = event.text
        self.timestamp = str(event.timestamp)

@dataclass
class ReportResult:
    proof: str
    text: str

    def __init__(self, report: Report):
        self.proof = report.proof.url
        self.text = report.text

@dataclass
class GoalResult:
    name: str
    is_active: bool
    deadline: str
    alert_period: str
    events: list[EventResult]
    reports: list[ReportResult]

    def __init__(self, goal: Goal):
        self.name = goal.name
        self.is_active = goal.is_active
        self.deadline = str(goal.deadline)
        self.alert_period = str(goal.alert_period)
        self.events = [EventResult(event) for event in goal.events_goal.all()]
        self.reports = [ReportResult(report) for report in goal.reports_goal.all()]

@dataclass
class GroupResult:
    id: int
    tag: str
    name: str
    image: str
    users: list[UserResult]
    goals: list[GoalResult]
    events: list[EventResult]

    def __init__(self, group: Group):
        self.id = group.id
        self.tag = group.tag
        self.name = group.name
        self.image = group.image.url
        self.users = [UserResult(user) for user in group.users.all()]
        self.goals = [GoalResult(goal) for goal in group.goals_group.all().prefetch_related('events_goal', 'reports_goal')]
        self.events = [EventResult(event) for event in group.events_group.all()]


class UserManager:
    """
    Manager for handling
    """

    @staticmethod
    def get_all() -> any:
        """
        Get all users from the table
        """
        return User.objects.all()

    @staticmethod
    def get(*args, **kwds) -> any:
        """
        Get a users with given login from the table
        """
        if "user_id" in kwds:
            if "login" in kwds:
                try:
                    return User.objects.get(id=kwds["user_id"], login=kwds["login"])
                except User.DoesNotExist as e:
                    raise DoesNotExist from e

            try:
                return User.objects.get(id=kwds["user_id"])
            except User.DoesNotExist as e:
                raise DoesNotExist from e

        if "login" in kwds:
            try:
                return User.objects.get(login=kwds["login"])
            except User.DoesNotExist as e:
                raise DoesNotExist from e

        raise IncorrectData

    @staticmethod
    def exists(*args, **kwds) -> bool:
        """
        Check wheteher a user with given id exists
        """
        if "user_id" in kwds:
            if "login" in kwds:
                return User.objects.filter(
                    id=kwds["user_id"], login=kwds["login"]
                ).exists()

            return User.objects.filter(id=kwds["user_id"]).exists()

        if "login" in kwds:
            return User.objects.filter(login=kwds["login"]).exists()

        raise IncorrectData

    @staticmethod
    def auth(login: str, password: str) -> None:
        """
        Auth a user with given login and password
        """
        try:
            user = User.objects.get(login=login)

            salt = user.password[:LENGTH_SALT]
            salted_hash = hashpw(bytes(password, "utf-8"), salt)

            if salted_hash != user.password:
                raise IncorrectData
        except User.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def create(login: str, password: str) -> None:
        """
        Create a user with given login and password
        """
        if User.objects.filter(login=login).exists():
            raise AlreadyExists

        salt = gensalt()
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        User.objects.create(login=login, password=salted_hash)

    @staticmethod
    def change_password(user_id: int, password: str) -> None:
        """
        Change a user's password with given login and new password
        """
        try:
            user = User.objects.get(id=user_id)
            user.password = hashpw(
                bytes(password, "utf-8"), user.password[:LENGTH_SALT]
            )
            user.save()
        except User.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def delete(user_id: int) -> None:
        """
        Delete the user with given id
        """
        try:
            User.objects.filter(id=user_id).delete()
        except User.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def get_groups(user_id: int) -> list[GroupResult]:
        """
        Get all groups by given user_id
        """
        try:
            groups = User.objects.get(id=user_id).groups.all().prefetch_related('users', 'goals_group', 'events_group')
            return [GroupResult(group) for group in groups]
        except Group.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def get_group(user_id: int, group_id: int) -> GroupResult:
        """
        Get group by given user_id and group_id
        """
        try:
            group = User.objects.get(id=user_id).groups.all().prefetch_related('users', 'goals_group', 'events_group').get(id=group_id)
            return GroupResult(group)
        except Group.DoesNotExist as e:
            raise DoesNotExist from e
