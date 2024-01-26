#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api, migrate

# Add your model imports
from models import (
    State,
    County,
    Voter,
    Admin,
    Account,
    Bill,
    Candidate,
    Representative,
    Election,
    Poll,
    Proposition,
    Campaign,
)

# Views go here!


@app.route("/")
def index():
    return "<h1>Project Server</h1>"


class Elections(Resource):
    def get(self):
        return make_response(
            [election.to_dict() for election in Election.query.all()],
            200,
        )

    def post(self):
        date = request.get_json()
        election = Election()
        try:
            election.name = name
            election.date = date
            election.election_type = election_type
            election.state = state
            election.county = county
            db.session.add(election)
            db.session.commit()
            return make_response(election.to_dict(), 201)
        except ValueError:
            return make_response({"error": "Invalid election"}, 400)


class ElectionById(Resource):
    def get(self, id):
        election = Election.query.get(id)
        if election:
            return make_response(election.to_dict(), 200)
        else:
            return make_response({"error": "Election not found"}, 404)

    def patch(self, id):
        election = Election.query.get(id)
        if election:
            try:
                election.name = name
                election.date = date
                election.election_type = election_type
                election.state = state
                election.county = county
                db.session.commit()
                return make_response(election.to_dict(), 200)
            except ValueError:
                return make_response({"error": "Invalid election"}, 400)
        else:
            return make_response({"error": "Election not found"}, 404)

    def delete(self, id):
        election = Election.query.get(id)
        if election:
            db.session.delete(election)
            db.session.commit()
            return make_response({"message": "Election deleted"}, 200)
        else:
            return make_response({"error": "Election not found"}, 404)


class Representatives(Resource):
    def get(self):
        return make_response(
            [representative.to_dict() for representative in Representative.query.all()],
            200,
        )


class RepresentativesByState(Resource):
    def get(self, state):
        representatives = Representative.query.filter_by(state=state).all()
        if representatives:
            return make_response(
                [representative.to_dict() for representative in representatives],
                200,
            )
        else:
            return make_response({"error": "Representatives not found"}, 404)


class Bills(Resource):
    def get(self):
        return make_response(
            [bill.to_dict() for bill in Bill.query.all()],
            200,
        )


class BillsByCode(Resource):
    def get(self, code):
        bills = Bill.query.filter_by(code=code).all()
        if bills:
            return make_response(
                [bill.to_dict() for bill in bills],
                200,
            )
        else:
            return make_response({"error": "Bills not found"}, 404)


api.add_resource(Elections, "/elections")
api.add_resource(ElectionById, "/elections/<int:id>")
api.add_resource(Representatives, "/representatives")
api.add_resource(RepresentativesByState, "/representatives/<string:state>")
api.add_resource(Bills, "/bills")
api.add_resource(BillsByCode, "/bills/<string:code>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
