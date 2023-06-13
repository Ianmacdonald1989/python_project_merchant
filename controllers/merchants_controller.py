from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import spending_repository, merchant_repository
from models.spending import Spending


spendings_blueprint = Blueprint("spendings", __name__)



#new
#'get'
#/spendings/new
@spendings_blueprint.route("/spendings/new", methods=['GET'])
def new_spending():
    merchants = merchant_repository.select_all()
    return render_template("spendings/new.html", all_merchants = merchants)

#create
#'post'
#/spendings

@spendings_blueprint.route("/spendings", methods=['POST'])
def create_spending():
    print("here")
    amount = request.form['Amount']
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']
    
    print(merchant_id)
    merchant = merchant_repository.select(merchant_id)
    print(merchant.id)
    spending = Spending(amount, tag, merchant)

    spending_repository.save(spending)
    return redirect('/spendings')
    
#index 
@spendings_blueprint.route("/spendings")
def spendings():
    spendings = spending_repository.select_all()
    return render_template("spendings/index.html", all_spendings = spendings)

#show
#'get'
#/spendings/<id>
@spendings_blueprint.route("/spendings/<id>", methods=['GET'])
def show_spending(id):
    spending = spending_repository.select(id)
    return render_template("spendings/show.html", spending = spending)

#edit 
#'get'
#/spending/<id>/edit 

@spendings_blueprint.route("/spendings/<id>/edit", methods=['GET'])
def edit_spending(id):
    spending = spending_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template('spendings/edit.html', spending = spending, all_merchants = merchants)

#update 
#'post' 
#/spendings/<id>/

@spendings_blueprint.route("/spendings/<id>/", methods = ['POST'])
def update_spendings(id):
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']    

    merchant = merchant_repository.select(merchant_id)
    spending = Spending(amount, tag, merchant, id)
    spending_repository.update(spending)
    return redirect('/spendings')


#delete 
#'delete'
#/spendings/<id>

@spendings_blueprint.route("/spendings/<id>/delete", methods=['POST'])
def delete_spendings(id):
    spending_repository.delete(id)
    return redirect('/spendings')


