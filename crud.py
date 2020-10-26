from flask import Flask, request, jsonify, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from classes.models.home_appliance import HomeAppliance
import os
import json
import copy


with open('secret.json') as f:
    SECRET = json.load(f)


DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartHomeAppliance(HomeAppliance, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _power_consumption = db.Column(db.Integer, unique=False)
    _hours_per_month_usage = db.Column(db.Float, unique=False)
    _repair_price = db.Column(db.Float, unique=False)
    _location_in_house = db.Column(db.String(32), unique=False)
    _appliance_name = db.Column(db.String(64), unique=False)
    _plugged_into_socket = db.Column(db.Boolean, unique=False)
    _connection_protocol = db.Column(db.String(32), unique=False)
    _data_transfer_amount = db.Column(db.Float, unique=False)

    def __init__(self, power_consumption=0, hours_per_month_usage=0.0,
                 repair_price=0.0, location_in_house='N/A',
                 appliance_name='N/A', plugged_into_socket=False,
                 connection_protocol='telnet', data_transfer_amount=0.0):
        super().__init__(power_consumption, hours_per_month_usage,
                         repair_price, location_in_house,
                         appliance_name, plugged_into_socket)
        self._connection_protocol = str(connection_protocol)
        self._data_transfer_amount = float(data_transfer_amount)


class SmartHomeApplianceSchema(ma.Schema):
    class Meta:
        fields = ('id', '_power_consumption', '_hours_per_month_usage',
                  '_repair_price', '_location_in_house', '_appliance_name',
                  '_plugged_into_socket', '_connection_protocol',
                  '_data_transfer_amount')


smart_home_appliance_schema = SmartHomeApplianceSchema()
smart_home_appliances_schema = SmartHomeApplianceSchema(many=True)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")


@app.route("/edit/<id>", methods=["GET"])
def edit(id):
    return render_template("edit.html", id=id)


@app.route("/smart_home_appliance", methods=["POST"])
def add_smart_home_appliance():
    if request.form.to_dict() == dict():
        request_form = request.json
    elif request.form.to_dict() != dict():
        request_form = request.form
    else:
        abort(404)
        return
    try:
        smart_home_appliance = SmartHomeAppliance(
            request_form['power_consumption'],
            request_form['hours_per_month_usage'],
            request_form['repair_price'],
            request_form['location_in_house'],
            request_form['appliance_name'],
            request_form['plugged_into_socket'],
            request_form['connection_protocol'],
            request_form['data_transfer_amount'])
    except (KeyError, TypeError):
        abort(404)
        return
    db.session.add(smart_home_appliance)
    db.session.commit()
    return smart_home_appliance_schema.jsonify(smart_home_appliance)


@app.route("/smart_home_appliance", methods=["GET"])
def get_smart_home_appliance():
    all_smart_home_appliance = SmartHomeAppliance.query.all()
    result = smart_home_appliances_schema.dump(all_smart_home_appliance)
    return jsonify({'smart_home_appliances': result})


@app.route("/smart_home_appliance/search/<search>", methods=["GET"])
def smart_home_appliance_search(search):
    smart_home_appliance = SmartHomeAppliance.query.filter(SmartHomeAppliance._appliance_name==search)
    if not smart_home_appliance:
        return jsonify({})
    result = smart_home_appliances_schema.dump(smart_home_appliance)
    return jsonify({'smart_home_appliances': result})


@app.route("/smart_home_appliance/<id>", methods=["GET"])
def smart_home_appliance_detail(id):
    smart_home_appliance = SmartHomeAppliance.query.get(id)
    if not smart_home_appliance:
        abort(404)
    return smart_home_appliance_schema.jsonify(smart_home_appliance)


@app.route("/smart_home_appliance/<id>", methods=["PUT", "POST"])
def smart_home_appliance_update(id):
    smart_home_appliance = SmartHomeAppliance.query.get(id)
    if not smart_home_appliance:
        abort(404)
    old_smart_home_appliance = copy.deepcopy(smart_home_appliance)
    if request.form.to_dict() == dict():
        request_form = request.json
    elif request.form.to_dict() != dict():
        request_form = request.form
    else:
        abort(404)
        return
    try:
        smart_home_appliance.power_consumption = int(request_form['power_consumption'])
        smart_home_appliance.hours_per_month_usage = float(request_form['hours_per_month_usage'])
        smart_home_appliance.repair_price = float(request_form['repair_price'])
        smart_home_appliance.location_in_house = str(request_form['location_in_house'])
        smart_home_appliance.appliance_name = str(request_form['appliance_name'])
        smart_home_appliance.plugged_into_socket = bool(int(request_form['plugged_into_socket']))
        smart_home_appliance.connection_protocol = str(request_form['connection_protocol'])
        smart_home_appliance.data_transfer_amount = float(request_form['data_transfer_amount'])
        db.session.commit()
    except (KeyError, TypeError):
        abort(404)
        return
    return smart_home_appliance_schema.jsonify(old_smart_home_appliance)


@app.route("/smart_home_appliance/<id>", methods=["DELETE"])
def smart_home_appliance_delete(id):
    smart_home_appliance = SmartHomeAppliance.query.get(id)
    if not smart_home_appliance:
        abort(404)
    db.session.delete(smart_home_appliance)
    db.session.commit()
    return smart_home_appliance_schema.jsonify(smart_home_appliance)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
