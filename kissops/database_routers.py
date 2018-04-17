#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:database_routers.py
User:               Guodong
Create Date:        2016/12/8
Create Time:        11:42
 """

from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class ItomsRouter(object):
    """
    A router to control all database operations on models in the
    itoms application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label == 'itoms':
            return 'itoms_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the itoms app is involved.
        :param obj1
        :param obj2
        :param hints
        """
        if obj1._meta.app_label == 'itoms' or \
                obj2._meta.app_label == 'itoms':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the itoms app only appears in the 'itoms_db'
        database.
        :param db
        :param app_label
        :param model_name
        :param hints
        """
        if app_label == 'itoms':
            return db == 'itoms_db'
        return None


class CmdbRouter(object):
    """
    A router to control all database operations on models in the
    itoms application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label == 'cmdb':
            return 'cmdb_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the itoms app is involved.
        :param obj1
        :param obj2
        :param hints
        """
        if obj1._meta.app_label == 'cmdb' or obj2._meta.app_label == 'cmdb':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the itoms app only appears in the 'itoms_db'
        database.
        :param db
        :param app_label
        :param model_name
        :param hints
        """
        if app_label == 'cmdb':
            return db == 'cmdb_db'
        return None


class ClientprofileRouter(object):
    """
    A router to control all database operations on models in the
    itoms application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write itoms models go to itoms_db.
        :param model
        :param hints
        """
        if model._meta.app_label == 'clientprofile':
            return 'clientprofile_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the itoms app is involved.
        :param obj1
        :param obj2
        :param hints
        """
        if obj1._meta.app_label == 'clientprofile' or obj2._meta.app_label == 'clientprofile':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the itoms app only appears in the 'itoms_db'
        database.
        :param db
        :param app_label
        :param model_name
        :param hints
        """
        if app_label == 'clientprofile':
            return db == 'clientprofile_db'
        return None
