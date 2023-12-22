"""
Module for handling interaction with db
"""

import dataclasses
import datetime
import json
import os
import random
import string

from dataclasses import dataclass
from typing import List, Dict, Tuple
from bcrypt import gensalt, hashpw

from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from goald_app.manager.exceptions import DoesNotExist, AlreadyExists, IncorrectData
from goald_app.models import User, Group, Goal, Event, Report, Duty


LENGTH_SALT = 29
LENGTH_HASH = 60


class DataclassEncoder(json.JSONEncoder):
    """
    class for encoding dataclasses in json
    """

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass
class UserResult:
    """
    dataclass for holding user record data
    """

    login: str
    name: str
    second_name: str
    duties: Dict[int, Tuple[int, int]]

    def __init__(self, user: User):
        self.login = user.login
        self.name = user.name
        self.second_name = user.second_name
        self.duties = {
                        duty.goal.id: (duty.current_value, duty.final_value)
                        for duty in user.duties_user.all()
                      }


@dataclass
class EventResult:
    """
    dataclass for holding event record data
    """

    type: int
    text: str
    timestamp: str

    def __init__(self, event: Event):
        self.type = event.type
        self.text = event.text
        self.timestamp = str(event.timestamp)


@dataclass
class ReportResult:
    """
    dataclass for holding report record data
    """

    proof: str
    text: str

    def __init__(self, report: Report):
        self.proof = report.proof.url
        self.text = report.text


@dataclass
class GoalResult:
    """
    dataclass for holding goal record data
    """

    name: str
    is_active: bool
    deadline: str
    alert_period: str
    current_value: int
    final_value: int
    events: List[EventResult]
    reports: List[ReportResult]

    def __init__(self, goal: Goal):
        self.name = goal.name
        self.is_active = goal.is_active
        self.deadline = str(goal.deadline)
        self.alert_period = str(goal.alert_period)
        self.current_value = sum(duty.current_value
                                 for duty in goal.duties_goal.all())
        self.final_value = sum(duty.final_value for duty in goal.duties_goal.all())
        self.events = [EventResult(event) for event in goal.events_goal.all()]
        self.reports = [ReportResult(report) for report in goal.reports_goal.all()]


@dataclass
class DutyResult:
    """
    dataclass for holding duty record data
    """
    final_value: int
    current_value: int
    deadline: str
    alert_period: str

    def __init__(self, duty: Duty):
        self.final_value = duty.final_value
        self.current_value = duty.current_value
        self.deadline = str(duty.deadline)
        self.alert_period = str(duty.alert_period)


@dataclass
class GroupResult:
    """
    dataclass for holding group record data
    """

    id: int
    tag: str
    name: str
    image: str
    users: List[UserResult]
    goals: List[GoalResult]
    events: List[EventResult]

    def __init__(self, group: Group):
        self.id = group.id
        self.tag = group.tag
        self.name = group.name
        self.image = group.image.url
        self.users = [UserResult(user) for user in group.users.all()]
        self.goals = [
            GoalResult(goal)
            for goal in group.goals_group.all().prefetch_related(
                "events_goal", "reports_goal"
            )
        ]
        self.events = [EventResult(event) for event in group.events_group.all()]


def get_report_record(report_id: int) -> Report:
    """
    Get a report with given report_id
    """
    try:
        return Report.objects.get(id=report_id)
    except Report.DoesNotExist as e:
        raise DoesNotExist(f"report with such id [{report_id}] does not exist") from e


def get_group_record(group_id: int) -> Group:
    """
    Get a group with given name from the table
    """
    try:
        return Group.objects.get(id=group_id)
    except Group.DoesNotExist as e:
        raise DoesNotExist(f"group with such id [{group_id}] does not exist") from e


def get_user_record(user_id: int = None, login: str = None) -> User:
    """
    Get a users with given login from the table
    """
    if user_id is not None:
        if login is not None:
            try:
                return User.objects.get(id=user_id, login=login)
            except User.DoesNotExist as e:
                raise DoesNotExist(
                    f"user with such id [{id}] " f"and login [{login}] does not exist"
                ) from e

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

    return None


class Manager:
    """
    Manager for handling interaction with db
    """

    # ->users
    @staticmethod
    def user_exists(user_id: int) -> bool:
        """
        Check if user exists
        """
        return User.objects.filter(id=user_id).exists()

    @staticmethod
    def get_user(user_id: int) -> UserResult:
        """
        Get user
        """
        try:
            user = get_user_record(user_id=user_id)
        except DoesNotExist:
            return UserResult(None)

        return UserResult(user)

    @staticmethod
    def get_user_groups(user_id: int) -> List[GroupResult]:
        """
        Get all groups by given user_id
        """
        try:
            groups = (
                User.objects.get(id=user_id)
                .groups.all()
                .prefetch_related("users", "goals_group", "events_group")
            )
            return [GroupResult(group) for group in groups]
        except Group.DoesNotExist as e:
            raise DoesNotExist(
                f"groups for current user [{user_id}] does not exist"
            ) from e

    @staticmethod
    def auth_user(login: str, password: str) -> int:
        """
        Auth a user with given login and password
        """
        try:
            user = get_user_record(login=login)
        except DoesNotExist as e:
            raise DoesNotExist(f"failed to get user: {e}") from e

        salt = user.password[:LENGTH_SALT]
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        if salted_hash != user.password:
            raise IncorrectData("wrong password")

        return user.id

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
        user = get_user_record(user_id=user_id)
        user.password = hashpw(bytes(password, "utf-8"), user.password[:LENGTH_SALT])
        user.save()

    @staticmethod
    def delete_user(user_id: int) -> None:
        """
        Delete the user with given id
        """
        user = get_user_record(user_id=user_id)
        user.delete()

    # ->groups
    @staticmethod
    def group_exists(group_id: int) -> bool:
        """
        Check if group exists
        """
        return Group.objects.filter(id=group_id).exists()

    @staticmethod
    def add_user_to_group(user_id: int, group_tag: str) -> None:
        """
        Add user to a group
        """
        Group.objects.get(tag=group_tag).users.add(get_user_record(user_id=user_id))
        # get_group_record(group_id=group_id).users.add(get_user_record(user_id=user_id))

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

        Manager.add_user_to_group(
            group_tag=group.tag, user_id=leader_id
        )

    @staticmethod
    def get_user_group(user_id: int, group_id: int) -> GroupResult:
        """
        Get a group with given id for the user from the table
        """
        try:
            return GroupResult(User.objects.get(id=user_id).groups.get(id=group_id))
        except User.DoesNotExist as e:
            raise DoesNotExist(f"user with id [{user_id}] does not exist") from e
        except Group.DoesNotExist as e:
            raise DoesNotExist(
                f"user with id [{user_id}]" f" has no groups with id [{group_id}]"
            ) from e

    @staticmethod
    def update_group_image(group_id: int, image: str) -> None:
        """
        Update group image
        """
        try:
            group = get_group_record(group_id=group_id)
        except DoesNotExist:
            return

        group.image = image
        group.save()

    # ->goals
    @staticmethod
    def get_user_goals(user_id: int) -> List[GoalResult]:
        """
        Get all goals for given user_id
        """
        try:
            result = []
            groups = Group.objects.filter(users__id=user_id)
            for group in groups:
                result += GoalResult(Goal.objects.get(group_id=group.id))

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
        if not Manager.group_exists(group_id=group_id):
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
    def get_report(report_id: int) -> ReportResult:
        """
        Get report
        """
        try:
            report = get_report_record(report_id=report_id)
        except DoesNotExist:
            return ReportResult(None)

        return ReportResult(report)

    @staticmethod
    def report_exists(report_id: int) -> bool:
        """
        Check if report exists
        """
        return Report.objects.filter(report_id=report_id).exists()

    @staticmethod
    def update_report_text(report_id: int, text: str = None) -> str:
        """
        Set/get a text value
        """
        Manager.report_exists(report_id=report_id)

        report = get_report_record(report_id=report_id)

        if text is not None:
            report.text = text
            report.save()

        return report.text

    @staticmethod
    def update_report_proof(report_id: int, proof: str = None) -> str:
        """
        Set/get a proof value
        """
        Manager.report_exists(report_id=report_id)

        report = get_report_record(report_id=report_id)

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

    @staticmethod
    def delegate_duty(
        user_id: int, goal_id: int, delegate_id: int, value: int
    ) -> None:
        """
        Delegate a duty to someone
        """
        try:
            group = Goal.objects.get(id=goal_id).group
            if user_id != group.leader.id:
                return

            if not group.users.filter(id=delegate_id).exists():
                raise DoesNotExist(f"user with such id [{delegate_id}] "
                                   f"is not a member of the group")

        except Goal.DoesNotExist as e:
            raise DoesNotExist("goal with such id [{goal_id}] does not exist") from e

        try:
            duty = Duty.objects.get(user_id=user_id, goal_id=goal_id)
            if duty.final_value < value:
                return

            try:
                Duty.objects.get(
                    user_id=delegate_id, goal_id=goal_id
                ).final_value += value
            except Duty.DoesNotExist:
                Duty.objects.create(
                    user_id=delegate_id, goal_id=goal_id, final_value=value
                )

            duty.final_value -= value

        except Duty.DoesNotExist as e:
            raise DoesNotExist(f"duty with such user_id [{user_id}] "
                               f"and goal_id [{goal_id}] does not exist") from e

    @staticmethod
    def pay_duty(user_id: int, goal_id: int, value: int) -> None:
        """
        Pay a some value
        """
        try:
            duty = Duty.objects.get(user_id=user_id, goal_id=goal_id)
            duty.current_value += value

            if duty.current_value >= duty.final_value:
                Duty.objects.delete(duty.id)

        except Duty.DoesNotExist as e:
            raise DoesNotExist(f"duty with such user_id [{user_id}] "
                               f"and goal_id [{goal_id}] does not exist") from e
