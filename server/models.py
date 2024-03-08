from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


# Platform Users and Accounts


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, server_default=db.func.now())

    # add relationships
    voter = db.relationship("Voter", back_populates="user")

    # add serialization rules
    serialize_rules = ("-voter.user",)

    # add validation

    def __repr__(self):
        return f"<User {self.username}>"


# Individual User Account Types (Roles)


class Voter(db.Model, SerializerMixin):
    __tablename__ = "voters"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_photo = db.Column(db.String)
    phone_number = db.Column(db.String)
    street_line1 = db.Column(db.String)
    street_line2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    postal_code = db.Column(db.String)
    county = db.Column(db.String)
    district = db.Column(db.String)
    country = db.Column(db.String)
    race = db.Column(db.String)
    ethnicity = db.Column(db.String)
    gender = db.Column(db.String)
    veteran_status = db.Column(db.String)
    birthdate = db.Column(db.Date)
    voter_registration_status = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, server_default=db.func.now())

    # add relationships
    user = db.relationship("User", back_populates="voter")

    # add serialization rules
    serialize_rules = ("-user.voter",)

    # add validation

    def __repr__(self):
        return f"<Voter {self.id}, {self.name}>"


# Political Jurisdictions


class Country(db.Model, SerializerMixin):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    # add relationships
    states = db.relationship("State", back_populates="country")
    counties = association_proxy("states", "counties")

    # add serialization rules
    serialize_rules = (
        "-states.country",
        "-counties.country",
    )

    # add validation

    def __repr__(self):
        return f"<Country {self.name}>"


class State(db.Model, SerializerMixin):
    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)

    # add relationships
    country = db.relationship("Country", back_populates="states")
    counties = db.relationship("County", back_populates="state")
    cities = association_proxy("counties", "cities")

    # add serialization rules
    serialize_rules = (
        "-counties.state",
        "-country.states",
        "-cities.state",
    )

    # add validation

    def __repr__(self):
        return f"<State {self.name}>"


class County(db.Model, SerializerMixin):
    __tablename__ = "counties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)

    # add relationships
    state = db.relationship("State", back_populates="counties")
    cities = db.relationship("City", back_populates="county")
    country = association_proxy("state", "country")

    # add serialization rules
    serialize_rules = (
        "-state.counties",
        "-country.counties",
        "-cities.county",
    )

    # add validation

    def __repr__(self):
        return f"<County {self.name}>"


class City(db.Model, SerializerMixin):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"), nullable=False)

    # add relationships
    county = db.relationship("County", back_populates="cities")
    state = association_proxy("county", "state")

    # add serialization rules
    serialize_rules = (
        "-county.cities",
        "-state.cities",
    )

    # add validation

    def __repr__(self):
        return f"<City {self.name}>"


# Elections and Election Information


class Election(db.Model, SerializerMixin):
    __tablename__ = "elections"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    deadlines_id = db.Column(db.Integer, db.ForeignKey("election_deadlines.id"))
    options_id = db.Column(db.Integer, db.ForeignKey("voting_options.id"))
    overview = db.Column(db.String)
    election_type = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    county = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, server_default=db.func.now())

    # add relationships
    options = db.relationship("Options", back_populates="election")
    deadlines = db.relationship("Deadlines", back_populates="election")

    # add serialization rules
    serialize_rules = (
        "-deadlines.election",
        "-options.election",
    )

    # add validation

    def __repr__(self):
        return f"<Election {self.name}>"


class Options(db.Model, SerializerMixin):
    __tablename__ = "voting_options"

    id = db.Column(db.Integer, primary_key=True)
    early_voting = db.Column(db.Boolean)
    vote_by_mail = db.Column(db.Boolean)
    in_person_voting = db.Column(db.Boolean)
    mobile_voting = db.Column(db.Boolean)
    online_voting = db.Column(db.Boolean)

    # add relationships
    election = db.relationship("Election", back_populates="options")

    # add serialization rules
    serialize_rules = ("-election.options",)

    # add validation

    def __repr__(self):
        return f"<Voting Option Set {self.id}>"


class Deadlines(db.Model, SerializerMixin):
    __tablename__ = "election_deadlines"

    id = db.Column(db.Integer, primary_key=True)
    voter_registration_deadline = db.Column(db.Date)
    mail_in_ballot_deployment_date = db.Column(db.Date)
    mail_in_ballot_return_opening = db.Column(db.Date)
    mail_in_ballot_return_deadline = db.Column(db.Date)
    mail_in_ballot_postmark_deadline = db.Column(db.Date)
    early_in_person_voting_opening = db.Column(db.Date)
    early_in_person_voting_deadline = db.Column(db.Date)
    in_person_election_date = db.Column(db.Date)

    # add relationships
    election = db.relationship("Election", back_populates="deadlines")

    # add serialization rules
    serialize_rules = ("-election.deadlines",)

    # add validation

    def __repr__(self):
        return f"<Election Deadline Set {self.id}>"
