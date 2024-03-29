import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app= Flask(__name__)

@app.route("/")
def home():
    return"HOME PAGE, Precipitation, stations, tobs, filtered temp. summary "

@app.route("/api/v1.0/precipitation")
def precipitation():
    results=session.query(Measurement.station,(func.count(Measurement.station))).group_by(Measurement.station).order_by((func.count(Measurement.date)).desc()).all()

    session.close()
    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
    session.close()
    return jsonify(session.query(Station.station).all())

@app.route("/api/v1.0/tobs")
def tobs():
    session.close()
    return jsonify(session.query(Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date>= '2016-08-23').order_by((Measurement.tobs).desc()).all())

@app.route("/api/v1.0/<start>")
def start_date(start):
    result=session.query(func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.station=="USC00519281").filter(Measurement.date>=start).all()
    print(result)
    t_dic={"t_min":result[0][0], "t_max":result[0][1], "t_avg":result[0][2]}
    session.close()
    return jsonify(t_dic)

@app.route("/api/v1.0/<start>/<end>")
def start_date_end(start, end):
    result=session.query(func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.station=="USC00519281").filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    print(result)
    t_dic={"t_min":result[0][0], "t_max":result[0][1], "t_avg":result[0][2]}
    session.close()
    return jsonify(t_dic)

if __name__ == "__main__":
    app.run()