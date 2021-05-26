### backstop-api-get

Example script to call Backstop APIs via GET.

## Setup Instructions

Requires:

Python 3

pipenv. If you don't have pipenv, install it: 
`pip3 install --user pipenv`
On Windows, you might want to add pipenv to your path, see https://www.jetbrains.com/help/pycharm/pipenv.html

Use pipenv to install the dependencies:
`pipenv install`


## Run:

backstopurl is the full URL to the API, example: https://mysite.backstopsolutions.com/backstop/api/system-info

username is your Backstop username

apitoken is your Backstop API token, which you can change on your Backstop User Profile page. The apitoken needs to be enclosed in single quotes on some operating systems.


On MacOS:
`pipenv run python3 BackstopApiGet.py -u backstopurl -n username -t 'apitoken'`


On Windows:
`pipenv run python BackstopApiGet.py -u backstopurl -n username -t apitoken`


or, edit the sample scripts, and run from there:

MacOS:`backstop-api-get.sh`

Windows:`backstop-api-get.cmd`
