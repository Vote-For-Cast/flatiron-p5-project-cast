#!/usr/bin/env python3

# Local imports
from config import db, app
from models import (
    State,
    County,
    Voter,
    Admin,
    Account,
    Legislation,
    Candidate,
    Representative,
    Election,
    Ballot,
)

# List of 50 US states and 3 real counties for each
us_states_with_counties = {
    "Alabama": ["Jefferson County", "Mobile County", "Madison County"],
    "Alaska": ["Anchorage", "Fairbanks North Star", "Matanuska-Susitna"],
    "Arizona": ["Maricopa County", "Pima County", "Pinal County"],
    "Arkansas": ["Pulaski County", "Benton County", "Washington County"],
    "California": ["Los Angeles County", "San Diego County", "Orange County"],
    "Colorado": ["Denver County", "El Paso County", "Arapahoe County"],
    "Connecticut": ["Fairfield County", "Hartford County", "New Haven County"],
    "Delaware": ["New Castle County", "Sussex County", "Kent County"],
    "Florida": ["Miami-Dade County", "Broward County", "Palm Beach County"],
    "Georgia": ["Fulton County", "Gwinnett County", "Cobb County"],
    "Hawaii": ["Honolulu County", "Hawaii County", "Maui County"],
    "Idaho": ["Ada County", "Canyon County", "Kootenai County"],
    "Illinois": ["Cook County", "DuPage County", "Lake County"],
    "Indiana": ["Marion County", "Lake County", "Allen County"],
    "Iowa": ["Polk County", "Linn County", "Scott County"],
    "Kansas": ["Johnson County", "Sedgwick County", "Shawnee County"],
    "Kentucky": ["Jefferson County", "Fayette County", "Kenton County"],
    "Louisiana": ["East Baton Rouge Parish", "Jefferson Parish", "Orleans Parish"],
    "Maine": ["Cumberland County", "York County", "Penobscot County"],
    "Maryland": ["Montgomery County", "Prince George's County", "Baltimore County"],
    "Massachusetts": ["Middlesex County", "Worcester County", "Suffolk County"],
    "Michigan": ["Wayne County", "Oakland County", "Macomb County"],
    "Minnesota": ["Hennepin County", "Ramsey County", "Dakota County"],
    "Mississippi": ["Hinds County", "Harrison County", "DeSoto County"],
    "Missouri": ["St. Louis County", "Jackson County", "St. Charles County"],
    "Montana": ["Yellowstone County", "Missoula County", "Gallatin County"],
    "Nebraska": ["Douglas County", "Lancaster County", "Sarpy County"],
    "Nevada": ["Clark County", "Washoe County", "Carson City"],
    "New Hampshire": ["Hillsborough County", "Rockingham County", "Merrimack County"],
    "New Jersey": ["Bergen County", "Middlesex County", "Essex County"],
    "New Mexico": ["Bernalillo County", "Doña Ana County", "Santa Fe County"],
    "New York": ["Kings County", "Queens County", "New York County"],
    "North Carolina": ["Mecklenburg County", "Wake County", "Guilford County"],
    "North Dakota": ["Cass County", "Burleigh County", "Grand Forks County"],
    "Ohio": ["Cuyahoga County", "Franklin County", "Hamilton County"],
    "Oklahoma": ["Oklahoma County", "Tulsa County", "Cleveland County"],
    "Oregon": ["Multnomah County", "Washington County", "Clackamas County"],
    "Pennsylvania": ["Philadelphia County", "Allegheny County", "Montgomery County"],
    "Rhode Island": ["Providence County", "Kent County", "Washington County"],
    "South Carolina": ["Greenville County", "Richland County", "Charleston County"],
    "South Dakota": ["Minnehaha County", "Pennington County", "Lincoln County"],
    "Tennessee": ["Shelby County", "Davidson County", "Knox County"],
    "Texas": ["Harris County", "Dallas County", "Tarrant County"],
    "Utah": ["Salt Lake County", "Utah County", "Davis County"],
    "Vermont": ["Chittenden County", "Rutland County", "Washington County"],
    "Virginia": ["Fairfax County", "Prince William County", "Loudoun County"],
    "Washington": ["King County", "Pierce County", "Snohomish County"],
    "West Virginia": ["Kanawha County", "Berkeley County", "Monongalia County"],
    "Wisconsin": ["Milwaukee County", "Dane County", "Waukesha County"],
    "Wyoming": ["Laramie County", "Natrona County", "Campbell County"],
}

if __name__ == "__main__":
    with app.app_context():
        print("Starting seed...")

        # Clear existing data from all tables
        Voter.query.delete()
        Admin.query.delete()
        Account.query.delete()
        Legislation.query.delete()
        Candidate.query.delete()
        Representative.query.delete()
        Election.query.delete()
        Ballot.query.delete()
        County.query.delete()
        State.query.delete()

        # Seed states and counties
        for state_name, counties in us_states_with_counties.items():
            state = State(name=state_name)
            db.session.add(state)
            db.session.flush()  # Flush to get the state id

            for county_name in counties:
                county = County(name=county_name, state_id=state.id)
                db.session.add(county)

        db.session.commit()

        print("Seeding completed.")
