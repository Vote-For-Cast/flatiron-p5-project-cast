#!/usr/bin/env python3

# Local imports
from config import db, app
from models import (
    User,
    State,
    County,
    City,
    Voter,
    Election,
    Country,
    Options,
    Deadlines,
)

# List of 50 US states and 3 real counties for each
us_states_with_county = {
    "Alabama": ["Jefferson County"],
    "Alaska": ["Anchorage"],
    "Arizona": ["Maricopa County"],
    "Arkansas": ["Pulaski County"],
    "California": ["Los Angeles County"],
    "Colorado": ["Denver County"],
    "Connecticut": ["Fairfield County"],
    "Delaware": ["New Castle County"],
    "Florida": ["Miami-Dade County"],
    "Georgia": ["Fulton County"],
    "Hawaii": ["Honolulu County"],
    "Idaho": ["Ada County"],
    "Illinois": ["Cook County"],
    "Indiana": ["Marion County"],
    "Iowa": ["Polk County"],
    "Kansas": ["Johnson County"],
    "Kentucky": ["Jefferson County"],
    "Louisiana": ["East Baton Rouge Parish"],
    "Maine": ["Cumberland County"],
    "Maryland": ["Montgomery County"],
    "Massachusetts": ["Middlesex County"],
    "Michigan": ["Wayne County"],
    "Minnesota": ["Hennepin County"],
    "Mississippi": ["Hinds County"],
    "Missouri": ["St. Louis County"],
    "Montana": ["Yellowstone County"],
    "Nebraska": ["Douglas County"],
    "Nevada": ["Clark County"],
    "New Hampshire": ["Hillsborough County"],
    "New Jersey": ["Bergen County"],
    "New Mexico": ["Bernalillo County"],
    "New York": ["Kings County"],
    "North Carolina": ["Mecklenburg County"],
    "North Dakota": ["Cass County"],
    "Ohio": ["Cuyahoga County"],
    "Oklahoma": ["Oklahoma County"],
    "Oregon": ["Multnomah County"],
    "Pennsylvania": ["Philadelphia County"],
    "Rhode Island": ["Providence County"],
    "South Carolina": ["Greenville County"],
    "South Dakota": ["Minnehaha County"],
    "Tennessee": ["Shelby County"],
    "Texas": ["Harris County"],
    "Utah": ["Salt Lake County"],
    "Vermont": ["Chittenden County"],
    "Virginia": ["Fairfax County"],
    "Washington": ["King County"],
    "West Virginia": ["Kanawha County"],
    "Wisconsin": ["Milwaukee County"],
    "Wyoming": ["Laramie County"],
}

if __name__ == "__main__":
    with app.app_context():
        print("Starting seed...")

        # Clear existing data from all tables
        User.query.delete()
        State.query.delete()
        County.query.delete()
        City.query.delete()
        Voter.query.delete()
        Election.query.delete()
        Country.query.delete()
        Options.query.delete()
        Deadlines.query.delete()
        Party.query.delete()

        # Seed states and counties
        for state_name, counties in us_states_with_county.items():
            state = State(name=state_name)
            db.session.add(state)
            db.session.flush()  # Flush to get the state id

            for county_name in counties:
                county = County(name=county_name, state_id=state.id)
                db.session.add(county)

        db.session.commit()

        print("Seeding completed.")
