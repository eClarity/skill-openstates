# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import us
import pyopenstates
pyopenstates.set_api_key('0e79f99b-a749-4ebc-961c-4801400294d2')

__author__ = 'eClarity'

LOGGER = getLogger(__name__)


class OpenStatesSkill(MycroftSkill):
    def __init__(self):
        super(OpenStatesSkill, self).__init__(name="OpenStatesSkill")
	self.name_given = False

    def initialize(self):
        search_bills_intent = IntentBuilder("SearchBillsIntent"). \
            require("SearchBillsKeyword").require("State").build()
        self.register_intent(search_bills_intent, self.handle_search_bills_intent)

        search_upper_legislator_intent = IntentBuilder("SearchUpperLegislatorIntent"). \
            require("SearchUpperLegislatorKeyword").require("State").build()
        self.register_intent(search_upper_legislator_intent, self.handle_search_upper_legislator_intent)

        search_committees_intent = IntentBuilder("SearchCommitteesIntent"). \
            require("SearchCommitteesKeyword").require("State").build()
        self.register_intent(search_committees_intent, self.handle_search_committees_intent)

        search_districts_intent = IntentBuilder("SearchDistrictsIntent"). \
            require("SearchDistrictsKeyword").require("State").build()
        self.register_intent(search_districts_intent, self.handle_search_districts_intent)

        search_name_intent = IntentBuilder("SearchNameIntent"). \
            require("SearchNameKeyword").require("FirstName").require("LastName").build()
        self.register_intent(search_name_intent, self.handle_search_name_intent)

    def handle_search_bills_intent(self, message):
	search = message.data.get("State").capitalize()
	name_to_abbr = us.states.mapping('name', 'abbr')
	name = name_to_abbr[search]
	response =  pyopenstates.search_bills(state=name,search_window="session")
	for i in response:
            self.speak(i['bill_id'])
	    self.speak(i['title'])

    def handle_search_upper_legislator_intent(self, message):
	self.name_given = True
	search = message.data.get("State").capitalize()
	name_to_abbr = us.states.mapping('name', 'abbr')
	name = name_to_abbr[search]
	response =  pyopenstates.search_legislators(state=name, chamber="upper")
	for i in response:
            self.speak(i['full_name'])
	self.speak("Would you like to know more about one of these senators?", expect_response=True)

    def handle_search_committees_intent(self, message):
	search = message.data.get("State").capitalize()
	name_to_abbr = us.states.mapping('name', 'abbr')
	name = name_to_abbr[search]
	response =  pyopenstates.search_committees(state=name)
	for i in response:
            self.speak(i['committee'])

    def handle_search_districts_intent(self, message):
	search = message.data.get("State").capitalize()
	name_to_abbr = us.states.mapping('name', 'abbr')
	name = name_to_abbr[search]
	response =  pyopenstates.search_districts(name, "upper")
	for i in response:
            self.speak(i['name'])

    def handle_search_name_intent(self, message):
	first = message.data.get("FirstName")
	last = message.data.get("LastName")
	response =  pyopenstates.search_legislators(first_name=first, last_name=last)
	for i in response:
	    fullname = i['full_name']
            self.speak(fullname)
            self.speak(i['email'])
            self.speak(i['state'])


    def stop(self):
        pass


def create_skill():
    return OpenStatesSkill()
