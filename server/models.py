from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


# Platform Users


class Voter(db.Model, SerializerMixin):
    __tablename__ = "voters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True)
    street_line1 = db.Column(db.String)
    street_line2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String, db.ForeignKey("states.name"))
    postal_code = db.Column(db.String)
    county = db.Column(db.String)
    country = db.Column(db.String)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Voter {self.username}>"


class Admin(db.Model, SerializerMixin):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"))
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county = db.Column(db.String)

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Admin {self.username}>"


# Platform Accounts


class Account(db.Model, SerializerMixin):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county = db.Column(db.String)

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Account {self.id}>"


# Platform Jurisdictions


class State(db.Model, SerializerMixin):
    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    # add relationships
    counties = db.relationship("County", back_populates="state")

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<State {self.name}>"


class County(db.Model, SerializerMixin):
    __tablename__ = "counties"

    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    name = db.Column(db.String, nullable=False)

    # add relationships
    state = db.relationship("State", back_populates="counties")

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<County {self.name}>"


# Election Processes


class Election(db.Model, SerializerMixin):
    __tablename__ = "elections"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ballot_id = db.Column(db.Integer, db.ForeignKey("ballots.id"))
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String, nullable=False)
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"))

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Election {self.name}>"


class Ballot(db.Model, SerializerMixin):
    __tablename__ = "ballots"

    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey("elections.id"))

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Ballot {self.id}>"


class Candidate(db.Model, SerializerMixin):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ballot_id = db.Column(db.Integer, db.ForeignKey("ballots.id"))
    type = db.Column(db.String)
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"))
    affiliation = db.Column(db.String)

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Candidate {self.name}>"


class Legislation(db.Model, SerializerMixin):
    __tablename__ = "legislation"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ballot_id = db.Column(db.Integer, db.ForeignKey("ballots.id"))
    type = db.Column(db.String)
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"))

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Legislation {self.name}>"


# Elected Officials


class Representative(db.Model, SerializerMixin):
    __tablename__ = "representatives"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String, nullable=False)
    state = db.Column(db.String, db.ForeignKey("states.name"))
    county_id = db.Column(db.Integer, db.ForeignKey("counties.id"))
    affiliation = db.Column(db.String)

    # add relationships

    # add serialization rules

    # add validation

    def __repr__(self):
        return f"<Representative {self.name}>"
