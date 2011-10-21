###############################################################################
##
##  Copyright 2011 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import datetime
import time
import random

UTC_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def utcnow():
   now = datetime.datetime.utcnow()
   return now.strftime(UTC_TIMESTAMP_FORMAT)

def parseutc(s):
   try:
      return datetime.datetime.strptime(s, UTC_TIMESTAMP_FORMAT)
   except:
      return None

def newid():
   return ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_") for i in range(16)])