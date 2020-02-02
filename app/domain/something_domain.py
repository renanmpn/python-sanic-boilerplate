# -*- coding: utf-8 -*-
from app import models, exceptions


class Entity(object):
    pass


class Something(Entity):
    repository = models.Something

    @classmethod
    def create_with_id(cls, something_id):
        db_instance = cls.repository.one_or_none(id=something_id)
        if db_instance is None:
            raise exceptions.NotFound('Could not find a something with id = {}'.format(something_id))
        return cls(db_instance=db_instance)

    @classmethod
    def create_with_instance(cls, db_instance):
        return cls(db_instance)

    @classmethod
    def create_a_new_something(cls, something_object):
        try:
            something_db = cls.repository.create_from_json(something_object)
            return cls.create_with_instance(something_db)
        except Exception as ex:
            raise ex

    def __init__(self, db_instance):
        self.db_instance = db_instance
        self.id = db_instance.id

    @property
    def name(self):
        return self.db_instance.name

    def as_dict(self, compact=True):
        something_dict = {
            'id': self.id,
            'piece_id': self.name
        }

        if not compact:
            something_dict.update({'more_thing': 'here'})

        return something_dict
