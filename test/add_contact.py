# -*- coding: utf-8 -*-
import pytest
from fixture.application2 import Application
from model.data import Data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.new_contact(Data(firstname = "Иван", lastname = "Грозный", nickname = "Царь", title = "Директор", company = "Рога и Копыта", home_phone = "123456789", mobile_phone = "234567891", email = "ivan@roga-kopyta.ru"))
    app.logout()