"""
Module for handling interaction with db
"""

from bcrypt import gensalt, hashpw

from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import datetime
import string
import random

from goald_app.manager.exceptions import DoesNotExist, AlreadyExists, IncorrectData

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


class Manager():
    """
    Manager for handling interaction with db
    """

    # ->users
    @staticmethod
    def get_user(user_id: int = None, login: str = None) -> any:
        """
        Get a users with given login from the table
        """
        if user_id is not None:
            if login is not None:
                try:
                    return User.objects.get(id=user_id, login=login)
                except User.DoesNotExist as e:
                    raise DoesNotExist(f"user with such id [{id}] "
                                       f"and login [{login}] does not exist") from e

        if user_id is not None:
            try:
                return User.objects.get(id=user_id)
            except User.DoesNotExist as e:
                raise DoesNotExist(f"user with such id [{id}] does not exist") from e

        if login is not None:
            try:
                return User.objects.get(login=login)
            except User.DoesNotExist as e:
                raise DoesNotExist(f"user with such login [{login}] does not exist") from e

    @staticmethod
    def get_user_groups(user_id: int) -> list[GroupResult]:
        """
        Get all groups by given user_id
        """
        try:
            groups = User.objects.get(id=user_id).groups.all().prefetch_related('users', 'goals_group', 'events_group')
            return [GroupResult(group) for group in groups]
        except Group.DoesNotExist as e:
            raise DoesNotExist(f"groups for current user [{user_id}] does not exist") from e

    @staticmethod
    def auth_user(login: str, password: str) -> None:
        """
        Auth a user with given login and password
        """
        try:
            user = Manager.get_user(login=login)
        except DoesNotExist as e:
            raise DoesNotExist(f"failed to get user: {e}") from e

        salt = user.password[:LENGTH_SALT]
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        if salted_hash != user.password:
            raise IncorrectData("wrong password")

    @staticmethod
    def create_user(login: str, password: str) -> None:
        """
        Create a user with given login and password
        """
        if User.objects.filter(login=login).exists():
            raise AlreadyExists(f"user with such login [{login}] already exists")

        salt = gensalt()
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        User.objects.create(login=login, password=salted_hash)

    @staticmethod
    def user_change_password(user_id: int, password: str) -> None:
        """
        Change a user's password with given login and new password
        """
        user = Manager.get_user(user_id=user_id)
        user.password = hashpw(
            bytes(password, "utf-8"), user.password[:LENGTH_SALT]
        )
        user.save()

    @staticmethod
    def delete_user(user_id: int) -> None:
        """
        Delete the user with given id
        """
        user = Manager.get_user(user_id=user_id)
        user.delete()

    # ->groups
    @staticmethod
    def group_exists(group_id: int) -> bool:
        """
        Check if group exists
        """
        return Group.objects.filter(id=group_id).exists()

    @staticmethod
    def get_group(group_id: int) -> any:
        """
        Get a group with given name from the table
        """
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist as e:
            raise DoesNotExist(f"group with such id [{group_id}] does not exist") from e

    @staticmethod
    def add_user_to_group(group_id: int, login: str) -> None:
        """
        Add user to a group
        """
        Manager.get_group(group_id=group_id).users.add(Manager.get_user(login=login))

    @staticmethod
    def create_group(
        name: str,
        image: str,
        leader_id: int,
        password: str = None,
        is_public: bool = True,
    ) -> None:
        """
        Create a group with given leader_id, name, image and is_public arguments
        """
        if Group.objects.filter(name=name).exists():
            raise AlreadyExists(f"group with such name [{name}] already exists")

        tag = "@" + "".join(
            name_ch
            if name_ch in string.ascii_letters or name_ch in string.digits
            else "_"
            for name_ch in name
        )
        while Group.objects.filter(tag=tag).exists():
            tag += random.choice(string.digits)

        group = Group.objects.create(
            tag=tag,
            is_public=is_public,
            name=name,
            password=password,
            image=image,
            leader=User.objects.get(id=leader_id),
        )

        Manager.add_user_to_group(id=leader_id)

    @staticmethod
    def get_user_groups(user_id: int) -> any:
        """
        Get all groups for given user_id
        """
        try:
            return Group.objects.filter(users__id=user_id)
        except Group.DoesNotExist as e:
            raise DoesNotExist("user has no groups") from e

    @staticmethod
    def get_user_group(user_id: int, group_id: int) -> any:
        """
        Get a group with given id for the user from the table
        """
        return Manager.get_user_groups(user_id=user_id).filter(id=group_id)

    # ->goals
    @staticmethod
    def get_user_goals(user_id: int) -> any:
        """
        Get all goals for given user_id
        """
        try:
            result = []
            groups = Group.objects.filter(users__id=user_id)
            for group in groups:
                result += Goal.objects.filter(group_id=group)

            return result

        except Group.DoesNotExist as e:
            raise DoesNotExist("user has no groups") from e
        except Goal.DoesNotExist as e:
            raise DoesNotExist("user has no goals") from e

    @staticmethod
    def create_goal(
        name: str,
        group_id: int,
        final_value: int = 0,
        deadline: datetime.datetime = None,
        alert_period: datetime.time = None,
        # supergoal_id: int,
    ) -> None:
        """
        Create a goal and start it
        """
        if not Manager.group_exists(id=group_id):
            raise DoesNotExist("group with such id [{group_id}] does not exist")

        group = Group.objects.get(id=group_id)

        if Goal.objects.filter(name=name, group=group).exists():
            raise AlreadyExists("goal with such name [{name}] exists in group")

        goal = Goal.objects.create(
            name=name,
            deadline=deadline,
            alert_period=alert_period,
            group=group,
            # supergoal_id=supergoal_id,
        )

        Duty.objects.create(
            final_value=final_value,
            current_value=final_value,
            deadline=deadline,
            alert_period=alert_period,
            user=group.leader,
            goal=goal,
        )

    # ->reports
    @staticmethod
    def create_report(goal_id: int, text: str, proof: str) -> None:
        """
        Create a report with given goal_id, text and proof
        """
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist(f"goal with such id [{goal_id}] does not exist")

        Report.objects.create(goal_id=goal_id, text=text, proof=proof)

    @staticmethod
    def report_exists(report_id: int) -> bool:
        """
        Check if report exists
        """
        return Report.objects.filter(report_id=report_id).exists()

    @staticmethod
    def get_report(report_id: int) -> any:
        """
        Get a report with given report_id
        """
        try:
            return Report.objects.get(id=report_id)
        except Report.DoesNotExist as e:
            raise DoesNotExist(f"report with such id [{report_id}] does not exist") from e

    @staticmethod
    def report_text(report_id: int, text: str = None) -> str:
        """
        Set/get a text value
        """
        report = Manager.ger_report(report_id=report_id)

        if text is not None:
            report.text = text
            report.save()

        return report.text

    # ->proof
    @staticmethod
    def update_proof(report_id: int, proof: str = None) -> str:
        """
        Set/get a proof value
        """
        Manager.report_exists(report_id=report_id)

        report = Manager.get_report(report_id=report_id)
        if proof is not None:
            report.proof = proof
            report.save()

        return report.proof

    # ->images
    @staticmethod
    def store_image(image: UploadedFile) -> str:
        """
        Store an image in a filesystem
        """
        storage_location = os.path.join(settings.MEDIA_ROOT, "group", "images")
        fs = FileSystemStorage(location=storage_location)
        fs.save(image.name, image)
        image_path = "group/images/" + image.name

        return image_path
