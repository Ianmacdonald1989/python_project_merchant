from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import spending_repository, merchant_repository
from models.spending import Spending

spending_blueprint = Blueprint("spendings", __name__)

#index 
@spending_blueprint.route("/spendings")
def spendings():
    spendings=spending_repository.select_all()
    return render_template('/spendings/index.html', all_spendings = spendings)

#new
#'get'
#/spendings/new


#create
#'post'
#/spendings

#show
#'get'
#/spendings/<id>

#edit 
#'get'
#/spending/<id>/edit 

#update 
#'post' 
#/spendings/<id>/

#delete 
#'delete'
#/spendings/<id>
