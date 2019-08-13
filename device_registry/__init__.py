from flask import Flask, g
from flask_restful import Resource, Api, reqparse

import markdown
import os
import shelve

from Test import DHCaseCategorization
from Test import DHCauseList
from Test import DHCaseStatus


app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/')
def index():


    with open(os.path.dirname(app.root_path)+'/README.md','r') as markdown_file:

        content = markdown_file.read()

        return markdown.markdown(content)


class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Success', 'data': devices}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Device registered', 'data': args}, 201

class dhcourtCategory(Resource):
    def get(self):
        print("controller->category")
        caseCategoryList = DHCaseCategorization.funcCaseCategory()
        return {'message': 'Success', 'data': caseCategoryList}, 200

class dhcourtCauseList(Resource):
    def post(self):
        print("controller->causelist")
        parser = reqparse.RequestParser()
        parser.add_argument('month', required=True)
        parser.add_argument('day',required=True)
        parser.add_argument('year',required=True)

        args = parser.parse_args()
        month = args.get('month')
        day = args.get('day')
        year =args.get('year')

        causeList = DHCauseList.funcCauseList(month,day,year)
        return {'message': 'Success', 'data': causeList}, 200


class dhcourtCaseStatusByCaseTypefirst(Resource):
    def post(self):
        print("controller->caseStatusByTypefirst")
        parser = reqparse.RequestParser()
        parser.add_argument('caseType', required=True)
        parser.add_argument('No', required=True)
        parser.add_argument('year', required=True)

        args = parser.parse_args()
        caseType = args.get('caseType')
        No = args.get('No')
        year = args.get('year')

        caseStatus = DHCaseStatus.funcCaseType(caseType, No, year)
        return {'message': 'Success', 'data': caseStatus}, 200


class dhcourtCaseStatusByCaseTypenext(Resource):
    def post(self):
        print("controller->caseStatusByTypenext")
        parser = reqparse.RequestParser()
        parser.add_argument('thisPage', required=True)
        parser.add_argument('nextPage', required=True)
        args = parser.parse_args()

        thisPage = args.get('thisPage')   # in %8 manner
        nextPage = args.get('nextPage')
        data=""
        pageno = 0
        if thisPage != "":
            data = DHCaseStatus.judgment(thisPage)
        else:
            pageno+=1
            print("next")
            data = DHCaseStatus.showStatusNext(pageno)

        return {'message': 'Success', 'data': data}, 200



class dhcourtCaseStatusByPetfirst(Resource):
    def post(self):
        print("controller->caseStatusByPetfirst")
        parser = reqparse.RequestParser()
        parser.add_argument('Pet', required=True)
        parser.add_argument('year', required=True)

        args = parser.parse_args()
        pet = args.get('Pet')
        year = args.get('year')

        caseStatus = DHCaseStatus.funcPetRes(pet,year)
        return {'message': 'Success', 'data': caseStatus}, 200


class dhcourtCaseStatusByAdvfirst(Resource):
    def post(self):
        print("controller->caseStatusByAdv")
        parser = reqparse.RequestParser()
        parser.add_argument('Adv', required=True)
        parser.add_argument('year', required=True)

        args = parser.parse_args()
        adv = args.get('Adv')
        year = args.get('year')

        caseStatus = DHCaseStatus.funAdvocate(adv,year)
        return {'message': 'Success', 'data': caseStatus}, 200




api.add_resource(DeviceList, '/devices')
api.add_resource(dhcourtCategory,'/DHCourtCategory')
api.add_resource(dhcourtCauseList,'/DHCauseList')
api.add_resource(dhcourtCaseStatusByCaseTypefirst,'/DHCaseStatus/Type')
api.add_resource(dhcourtCaseStatusByCaseTypenext,'/DHCaseStatus/Next')
api.add_resource(dhcourtCaseStatusByPetfirst,'/DHCaseStatus/Pet')
api.add_resource(dhcourtCaseStatusByAdvfirst,'/DHCaseStatus/Adv')



