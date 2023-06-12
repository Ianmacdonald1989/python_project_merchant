from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import spending_repository, merchant_repository
from models.spending import Spending

spending_blueprint = Blueprint("spendings", __name__)

#index 
@spending_blueprint.route("/spendings")
def spendings():