# Open States Skill for Mycroft

based off the OpenStates.org python library

This is a skill to add [Open States](https://openstates.org/) support to
[Mycroft](https://mycroft.ai). This skill currently supports searching for bills by state, Retrieving a list of state senators and house member by state, search committees by state, search districts by state.  Get information on a legislator via name search.  Some of the retrieved information is still in a rough state, and will be improved over time.

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
cd ~/.mycroft/skills
git clone https://github.com/eClarity/skill-openstates.git
workon mycroft
cd skill-openstates
pip install -r requirements.txt
```

You will then need to restart mycroft.

## Configuration

Config options coming soon.  Not currently needed for API key.


## Usage

Say something like "Hey Mycroft, government bills for "New York". 
 

## TODO
 * New intents for more detailed information
 * Improve dialogs
 * ...

## Contributing

All contributions welcome:

 * Fork
 * Write code
 * Submit merge request


